'''
Created on 8.6.2014

@author: Stefan Smihla
'''

import configparser
import os, subprocess
import platform
from threading import Thread

if platform.system() == 'Windows':
    import win32api

SOURCE_DIR = 'sources'

def load_languages(config_file):
    """ Loads languages from configuration file. """
    config = configparser.ConfigParser()
    config.read(config_file)

    languages = []
    for lang in config.sections():
        lang_class = globals().get(config.get(lang, 'class'))
        languages.append(lang_class(config[lang]))

    return languages

class Language(object):
    """ Abstract language class. """

    _stdout = ''

    @classmethod
    def set_output(cls, stdout):
        """ Sets output value. """
        cls._stdout = stdout

    @classmethod
    def get_stdout(cls):
        """ Returns output value. """
        return cls._stdout

    @classmethod
    def run_process(cls, command):
        """ Run process and saves it output. """
        cls.set_output(subprocess.Popen(command,
                                        universal_newlines=True,
                                        stderr=subprocess.STDOUT,
                                        stdout=subprocess.PIPE,
                                        shell=True).stdout.read().strip())
        return cls.get_stdout()

    @classmethod
    def safe_path(cls, path):
        """ Convert path to safe path. """
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
        except (AttributeError, IndexError, ValueError):
            self.version = None

    def check_version(self, param='--version'):
        """ Checks version of compiler. """
        return self.run_process('%s %s' % (self.path,
                                           param)).splitlines()[0].strip()

    def evaluate(self, args):
        """ Evaluates script. """
        pass

    def evaluate_with_timeout(self, args, timeout=None):
        """ Kills process after timeout. """
        self.set_output(None)
        evaluation = Thread(target=self.evaluate, args=(args, ))
        evaluation.start()
        evaluation.join(timeout)
        return self.get_stdout() if self.get_stdout() \
            else '%s:\nKilled' % (self.name)

    def clean_up(self):
        """ Cleans up compiled files. """
        if hasattr(self, 'output') and os.path.isfile(self.output):
            os.remove(self.output)

class CLanguage(Language):
    """ C Language class. """

    def compile(self):
        """ Compiles C file to binary. """
        result = self.run_process('%s %s %s %s' % (self.path, self.source,
                                                   self.config, self.output))
        return 'OK' if not result else 'FAIL: %s' % result

    def evaluate(self, args):
        """ Evaluates script. """
        return self.run_process('%s %s' % (self.output, args))

class CSLanguage(Language):
    """ C# Language class. """

    def check_version(self, param='-help'):
        """ Checks C# version. """
        return super(CSLanguage, self).check_version(param)

    def compile(self):
        """ Compiles CS file to binary. """
        result = self.run_process('%s %s%s %s' % (self.path, self.config,
                                                  self.output, self.source))
        return 'OK' if len(result.splitlines()) == 4 else 'FAIL: %s' % result

    def evaluate(self, args):
        """ Evaluates script. """
        return self.run_process('%s %s' % (self.output, args))

class PascalLanguage(Language):
    """ Pascal Language class. """

    def check_version(self, param='-h'):
        """ Checks Pascal version. """
        return super(PascalLanguage, self).check_version(param)

    def compile(self):
        """ Compiles Java file to binary. """
        result = self.run_process('%s %s' % (self.path, self.source))
        return 'OK' if len(result.splitlines()) == 6 else 'FAIL:\n%s' % result

    def evaluate(self, args):
        """ Evaluates script. """
        return self.run_process('%s %s' % (os.path.join('sources',
                                                        self.output), args))

    def clean_up(self):
        """ Cleans up Pascal Script. """
        output = os.path.join('sources', '.'.join(self.output.split('.')[:-1]))
        for ext in ['o', 'exe']:
            if os.path.isfile('%s.%s' % (output, ext)):
                os.remove('%s.%s' % (output, ext))

class JavaLanguage(Language):
    """ Java Language class. """

    def check_version(self, param='-version'):
        """ Checks Java version. """
        return super(JavaLanguage, self).check_version(param)

    def compile(self):
        """ Compiles Java file to binary. """
        result = self.run_process('%s %s %s' % (self.path, self.source,
                                                self.config))
        return 'OK' if not result else 'FAIL:\n%s' % result

    def evaluate(self, args):
        """ Evaluates script. """
        path = os.path.join(os.path.split(self.path)[0], 'java')
        output = '.'.join(self.output.split('.')[:-1])
        return self.run_process('%s %s %s' % (path, output, args))

class JavaScriptLanguage(Language):
    """ JavaScript Language class. """

    def evaluate(self, args):
        """ Evaluates script. """
        return self.run_process('%s %s %s' % (self.path, self.source, args))

class PHPLanguage(Language):
    """ PHP Language class. """

    def evaluate(self, args):
        """ Evaluates script. """
        return self.run_process('%s %s %s' % (self.path, self.source, args))

class RubyLanguage(Language):
    """ Ruby Language class. """

    def evaluate(self, args):
        """ Evaluates script. """
        return self.run_process('%s %s %s' % (self.path, self.source, args))

class PythonLanguage(Language):
    """ Python Language class. """

    def evaluate(self, args):
        """ Evaluates script. """
        return self.run_process('%s %s %s' % (self.path, self.source, args))

class PrologLanguage(Language):
    """ Prolog Language class. """

    def evaluate(self, args):
        """ Evaluates script. """
        return self.run_process('%s %s -- %s' % (self.path, self.source, args))

class CLispLanguage(Language):
    """ Common Lisp Language class. """

    def evaluate(self, args):
        """ Evaluates script. """
        return self.run_process('%s %s %s' % (self.path, self.source, args))
