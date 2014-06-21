'''
Created on 8.6.2014

@author: Stefan Smihla
'''

import configparser
import os, subprocess, signal
import platform, shutil
import inspect
from evaluator import config
from threading import Thread

if platform.system() == 'Windows':
    import win32api

SOURCE_DIR = 'sources'

def load_languages():
    """ Loads languages from configuration file. """

    languages = []
    for name, lang in sorted(inspect.getmembers(config, inspect.isclass), key=lambda x: x[1].ORDER):
        if name not in ['CompiledLanguage', 'Language']:
            lang_class = globals().get(name)
            languages.append(lang_class(lang))    

    return languages

class Language(object):
    """ Abstract language class. """

    _stdout = ''
    _process = None

    @classmethod
    def set_output(cls, stdout):
        """ Sets output value. """
        cls._stdout = stdout

    @classmethod
    def get_stdout(cls):
        """ Returns output value. """
        return cls._stdout

    @classmethod
    def set_process(cls, process):
        """ Sets process. """
        cls._process = process

    @classmethod
    def get_process(cls):
        """ Returns process value. """
        return cls._process

    @classmethod
    def run_process(cls, command):
        """ Run process and saves it output. """
        cls.set_process(subprocess.Popen(command,
                                        universal_newlines=True,
                                        stderr=subprocess.STDOUT,
                                        stdout=subprocess.PIPE,
                                        shell=True,
                                        preexec_fn=os.setsid))
        cls.set_output(cls.get_process().stdout.read().strip())
        return cls.get_stdout()
        
    def safe_output(self, output=None):
        if not output:
            output = self.output

        if os.path.dirname(output):
            return output
        else:
            return os.path.join('.', output)

    def __init__(self, config_lang):
        self.name = config_lang.NAME
        self.program = config_lang.PROGRAM
        self.available = shutil.which(self.program)
        
        if not self.available:
            return
        
        self.version_cmd = config_lang.VERSION
        self.compile_cmd = config_lang.COMPILE
        self.run_cmd = config_lang.RUN
        self.clean = config_lang.CLEAN
        self.version = self.check_version(config_lang.VERSION)

    def check_version(self, version):
        """ Checks version of compiler. """
        return self.run_process(version).splitlines()[0].strip()

    def evaluate(self, args):
        """ Evaluates script. """
        return self.run_process('%s %s' % (self.run_cmd, args))

    def evaluate_with_timeout(self, args, timeout=None):
        """ Kills process after timeout. """
        self.set_output(None)
        evaluation = Thread(target=self.evaluate, args=(args, ))
        evaluation.start()
        evaluation.join(timeout)
        if self.get_stdout():
            return self.get_stdout()
        else:
            os.killpg(self.get_process().pid, signal.SIGTERM)
            self.set_process(None)
            return '%s:\nKilled' % self.name

    def clean_up(self):
        """ Cleans up compiled files. """
        for filename in self.clean:
            if os.path.isfile(filename):
                os.remove(filename)

class CompiledLanguage(Language):

    def compile(self):
        result = self.run_process(self.compile_cmd)
        return 'OK' if not result else 'FAIL: %s' % result

class CLanguage(CompiledLanguage):
    """ C Language class. """
    pass

class ObjCLanguage(CompiledLanguage):
    """ Objective-C Language class. """
    
    def check_version(self, version):
        """ Checks version of compiler. """
        return self.run_process(version).splitlines()[1].strip()

class CSLanguage(CompiledLanguage):
    """ C# Language class. """
    pass

class PascalLanguage(CompiledLanguage):
    """ Pascal Language class. """

    def compile(self):
        """ Compiles Pascal file to binary. """
        result = self.run_process(self.compile_cmd)
        return 'OK' if len(result.splitlines()) in [6, 7] else 'FAIL:\n%s' % result

class JavaLanguage(CompiledLanguage):
    """ Java Language class. """
    pass

class JavaScriptLanguage(Language):
    """ JavaScript Language class. """
    pass

class PHPLanguage(Language):
    """ PHP Language class. """
    pass

class RubyLanguage(Language):
    """ Ruby Language class. """
    pass

class PerlLanguage(Language):
    """ Perl Language class. """
    pass

class BashLanguage(Language):
    """ Bash Language class. """
    pass

class RubyLanguage(Language):
    """ Ruby Language class. """
    pass

class PythonLanguage(Language):
    """ Python Language class. """
    pass

class PrologLanguage(Language):
    """ Prolog Language class. """

    def evaluate(self, args):
        """ Evaluates script. """
        return self.run_process('%s -- %s' % (self.run_cmd, args))

class CLispLanguage(Language):
    """ Common Lisp Language class. """
    pass