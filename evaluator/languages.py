# -*- coding: utf-8 -*-
'''
Programming Languages Benchmark Script.
Copyright (C) 2014 Stefan Smihla

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.
'''

import os, subprocess, signal
import platform
import inspect
from evaluator import config
from threading import Thread

SOURCE_DIR = 'sources'

def load_languages():
    """ Loads languages from configuration file. """

    languages = []
    for name, lang in sorted(inspect.getmembers(config, inspect.isclass),
                             key=lambda x: x[1].ORDER):

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
    def build_proc_params(cls):
        """ Build args depended on OS. """

        params = {'universal_newlines': True,
                  'stderr': subprocess.STDOUT,
                  'stdout': subprocess.PIPE,
                  'shell': True}

        if platform.system() != 'Windows':
            params['preexec_fn'] = os.setsid

        return params

    @classmethod
    def run_process(cls, command):
        """ Run process and saves it output. """
        cls.set_process(subprocess.Popen(command, **cls.build_proc_params()))
        cls.set_output(cls.get_process().stdout.read().strip())
        return cls.get_stdout()

    def __init__(self, config_lang):
        self.name = config_lang.NAME
        self.program = config_lang.PROGRAM
        self.available = True if self.program else False

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
            if platform.system() == 'Windows':
                subprocess.Popen('TASKKILL /F /PID %s /T' \
                                 % self.get_process().pid,
                                 stdout=subprocess.DEVNULL,
                                 stderr=subprocess.DEVNULL)
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
    """ Class for compiled languages. """

    def compile(self):
        """ Compile source code into binary. """

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
        return 'OK' if len(result.splitlines()) in [6, 7] \
                    else 'FAIL:\n%s' % result

class JavaLanguage(CompiledLanguage):
    """ Java Language class. """
    pass

class JavaScriptLanguage(Language):
    """ JavaScript Language class. """
    pass

class PHPLanguage(Language):
    """ PHP Language class. """
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

class ClojureLanguage(Language):
    """ Clojure Language class. """
    
    def check_version(self, version):
        return version

class HaskellLanguage(Language):
    """ Haskell Language class. """
    pass
