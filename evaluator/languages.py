# -*- coding: utf-8 -*-
"""
Programming Languages Benchmark Script.
Copyright (C) 2014-2016 Stefan Smihla

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
"""

import os
import inspect

from evaluator.process_manager import ProcessManager
from evaluator import config


def load_languages():
    """ Loads languages from configuration file. """

    def is_language_cls(class_obj):
        """ Checks if concrete Language class. """
        return inspect.getmro(class_obj)[1].__name__ == 'Language'

    languages = []
    members = [cls for cls in inspect.getmembers(config, inspect.isclass)]
    members = sorted([cls for cls in members if is_language_cls(cls[1])], key=lambda x: x[1].ORDER)
    for name, lang in members:
        lang_class = globals().get(name) or Language
        languages.append(lang_class(lang))

    return languages


class Language(object):
    """ Abstract language class. """

    def __init__(self, config_lang):
        self.skip = False
        self.name = config_lang.NAME
        self.program = config_lang.PROGRAM

        if not self.program:
            return

        self.version_cmd = config_lang.VERSION
        self.compile_cmd = config_lang.COMPILE
        self.run_cmd = config_lang.RUN
        self.clean = config_lang.CLEAN
        self.version = self.check_version(config_lang.VERSION)

    @classmethod
    def run_process(cls, command, timeout=None):
        """ Runs safely process. """
        return ProcessManager.run_process(command, timeout)

    def is_skipped(self):
        """ Checks if language was previously skipped. """
        return self.skip

    def is_available(self):
        """ Checks if compiler is available """
        return True if self.program else False

    def is_compilable(self):
        """ Checks if language is compilable. """
        return True if self.compile_cmd else False

    def check_version(self, version):
        """ Checks version of compiler. """
        return self.run_process(version).splitlines()[0].strip()

    def compile(self):
        """ Compile source code into binary. """
        result = self.run_process(self.compile_cmd)
        return 'OK' if not result else 'FAIL: %s' % result

    def evaluate(self, args, timeout=None):
        """ Evaluates script. """
        return self.run_process('%s %s' % (self.run_cmd, args), timeout)

    def clean_up(self):
        """ Cleans up compiled files. """
        for filename in self.clean:
            if os.path.isfile(filename):
                os.remove(filename)

#  ######### Languages that needs to run slighly different ##########


class CppLanguage(Language):
    """ C++ Language class. """

    def check_version(self, version):
        """ Checks version of compiler. """
        return self.run_process(version).splitlines()[1].strip()


class ObjCLanguage(Language):
    """ Objective-C Language class. """

    def check_version(self, version):
        """ Checks version of compiler. """
        return self.run_process(version).splitlines()[1].strip()


class PascalLanguage(Language):
    """ Pascal Language class. """

    def compile(self):
        """ Compiles Pascal file to binary. """
        result = self.run_process(self.compile_cmd)
        return 'OK' if 'lines compiled, ' in result else 'FAIL:\n%s' % result


class ClojureLanguage(Language):
    """ Clojure Language class. """

    def check_version(self, version):
        return version


class FSLanguage(Language):
    """ F# Language class. """

    def compile(self):
        """ Compile source code into binary. """
        result = self.run_process(self.compile_cmd)
        return 'OK' if len(result) != 2 else 'FAIL: %s' % result
