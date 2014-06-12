'''
Created on 8.6.2014

@author: Morzeux
'''

import configparser
import os, subprocess
import platform
from threading import Thread

if platform.system() == 'Windows':
    import win32api

SOURCE_DIR = 'sources'

def load_languages(config_file):
    config = configparser.ConfigParser()
    config.read(config_file)

    languages = []
    for lang in config.sections():
        LangClass = globals().get(config.get(lang, 'class'))
        languages.append(LangClass(config[lang]))

    return languages

class Language(object):

    _stdout = ''

    @classmethod
    def set_output(cls, stdout):
        cls._stdout = stdout
        
    @classmethod
    def get_stdout(cls):
        return cls._stdout

    @classmethod
    def run_process(cls, command):
        cls.set_output(subprocess.Popen(command,
                                universal_newlines=True,
                                stderr=subprocess.STDOUT,
                                stdout=subprocess.PIPE,
                                shell=True).stdout.read().strip())
        return cls.get_stdout()

    @classmethod
    def safe_path(cls, path):
        path = os.path.normpath(path)
        if platform.system() == 'Windows':
            return win32api.GetShortPathName(path)
        else:
            return path

    def __init__(self, section):
        self.name = section.name
        self.path = self.safe_path(section.get('path'))
        self.source = os.path.join(SOURCE_DIR, section.get('source'))
        self.config = section.get('config')
        self.output = section.get('output')

        try:
            self.version = self.check_version()
        except:
            self.version = None

    def check_version(self, param='--version'):
        return self.run_process('%s %s' % (self.path, param)).splitlines()[0].strip()
    
    def evaluate(self, args):
        pass
    
    def evaluate_with_timeout(self, args, timeout=None):
        self.set_output(None)
        evaluation = Thread(target=self.evaluate, args=(args, ))
        evaluation.start()
        evaluation.join(timeout)
        return self.get_stdout() if self.get_stdout() else '%s:\nKilled' % (self.name) 

class C_Language(Language):
    
    def compile(self):
        result = self.run_process('%s %s %s %s' % (self.path, self.source, self.config, self.output))
        return 'OK' if not result else 'FAIL: %s' % result
    
    def evaluate(self, args):
        return self.run_process('%s %s' % (self.output, args))

class CS_Language(Language):
    
    def check_version(self):
        return super(CS_Language, self).check_version('-help')
    
    def compile(self):
        result = self.run_process('%s %s%s %s' % (self.path, self.config, self.output, self.source))
        return 'OK' if len(result.splitlines()) == 4 else 'FAIL: %s' % result   
    
    def evaluate(self, args):
        return self.run_process('%s %s' % (self.output, args))

class Java_Language(Language):

    def check_version(self):
        return super(Java_Language, self).check_version('-version')
    
    def compile(self):
        result = self.run_process('%s %s %s' % (self.path, self.source, self.config))
        return 'OK' if not result else 'FAIL:\n%s' % result
    
    def evaluate(self, args):
        path = os.path.join(os.path.split(self.path)[0], 'java')
        output = '.'.join(self.output.split('.')[:-1])
        return self.run_process('%s %s %s' % (path, output, args))
    
class JavaScript_Language(Language):
    
    def evaluate(self, args):
        return self.run_process('%s %s %s' % (self.path, self.source, args))
    
class PHP_Language(Language):
    
    def evaluate(self, args):
        return self.run_process('%s %s %s' % (self.path, self.source, args))

class Ruby_Language(Language):
    
    def evaluate(self, args):
        return self.run_process('%s %s %s' % (self.path, self.source, args))

class Python_Language(Language):
    
    def evaluate(self, args):
        return self.run_process('%s %s %s' % (self.path, self.source, args))

class Prolog_Language(Language):

    def evaluate(self, args):
        return self.run_process('%s %s -- %s' % (self.path, self.source, args))
    
class CLisp_Language(Language):
    
    def evaluate(self, args):
        return self.run_process('%s %s %s' % (self.path, self.source, args))
