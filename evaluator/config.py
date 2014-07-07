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

import os, shutil, shlex

def safe_path(path):
    """ Convert path to safe path. """
    path = shutil.which(os.path.normpath(path))
    return shlex.quote(path) if path else None

EVALUATIONS = 2
TIMEOUT = 2
TESTS = [#(15, 6, 1000000),
         (20, 6, 10000000),
         (25, 6, 100000000),
         (30, 6, 1000000000)]

INKSCAPE_PATH = safe_path(\
    '/Applications/Inkscape.app/Contents/Resources/bin/inkscape')

class Language(object):
    """ Default config when not set. """

    NAME = None
    PROGRAM = None
    VERSION = None
    COMPILE = None
    RUN = None
    CLEAN = []
    ORDER = -1

    @classmethod
    def help(cls):
        """ Prints config help. """
        print("You have to specify these params for every evaluated language:")
        print("")
        print("NAME - name of language which will be displayed in results")
        print("PROGRAM - path where compiler / interpreter can be found")
        print("VERSION - command to detect version of compiler / interpreter")
        print("COMPILE - command to compile source code")
        print("RUN - command to execute source code")
        print("CLEAN - files which will be deleted after finish")
        print("ORDER - order to display")

    @classmethod
    def useless_method(cls):
        """ This method is completely useless. """
        pass

class CLanguage(Language):
    """ C Language config. """

    NAME = 'C'
    PROGRAM = safe_path('cc')
    VERSION = '%s --version' % PROGRAM
    COMPILE = '%s -Wall sources/c_test.c -o c_test' % PROGRAM
    RUN = './c_test'
    CLEAN = ['c_test']
    ORDER = 1

class CppLanguage(Language):
    """ C++ Language config. """

    NAME = 'C++'
    PROGRAM = safe_path('gcc')
    VERSION = '%s --version' % PROGRAM
    COMPILE = '%s -Wall sources/cpp_test.cpp -o cpp_test -lstdc++' % PROGRAM
    RUN = './cpp_test'
    CLEAN = ['cpp_test']
    ORDER = 2

class ObjCLanguage(Language):
    """ Objective-C Language config. """

    NAME = 'Objective-C'
    PROGRAM = safe_path('gcc')
    VERSION = '%s --version' % PROGRAM
    COMPILE = '%s -o objc_test -Wall -std=c99 sources/objc_test.m\
        -framework Foundation -lobjc' % PROGRAM
    RUN = './objc_test'
    CLEAN = ['objc_test']
    ORDER = 3

class CSLanguage(Language):
    """ C# Language config. """

    NAME = 'C#'
    PROGRAM = safe_path('mcs')
    VERSION = '%s --version' % PROGRAM
    COMPILE = '%s sources/csharp_test.cs' % PROGRAM
    RUN = 'mono sources/csharp_test.exe'
    CLEAN = ['sources/csharp_test.exe']
    ORDER = 4

class DLanguage(Language):
    """ D Language config. """

    NAME = 'D'
    PROGRAM = safe_path('dmd')
    VERSION = '%s --help' % PROGRAM
    COMPILE = '%s sources/d_test.d -ofd_test' % PROGRAM
    RUN = './d_test'
    CLEAN = ['d_test', 'd_test.o']
    ORDER = 5

class PascalLanguage(Language):
    """ Pascal Language config. """

    NAME = 'Pascal'
    PROGRAM = safe_path('fpc')
    VERSION = '%s -h' % PROGRAM
    COMPILE = '%s sources/pascal_test.pas' % PROGRAM
    RUN = 'sources/pascal_test'
    CLEAN = ['sources/pascal_test', 'sources/pascal_test.o']
    ORDER = 6

class JavaLanguage(Language):
    """ Java Language config. """

    NAME = 'Java'
    PROGRAM = safe_path('javac')
    VERSION = '%s -version' % PROGRAM
    COMPILE = '%s sources/java_test.java -d .' % PROGRAM
    RUN = 'java java_test'
    CLEAN = ['java_test.class']
    ORDER = 7

class ScalaLanguage(Language):
    """ Scala Language config. """

    NAME = 'Scala'
    PROGRAM = safe_path('/Applications/scala-2.11.1/bin/scala')
    VERSION = '%s -version' % PROGRAM
    RUN = '%s sources/scala_test.scala' % PROGRAM
    ORDER = 8

class LuaLanguage(Language):
    """ Lua Language config. """

    NAME = 'Lua'
    PROGRAM = safe_path('lua')
    VERSION = '%s -v' % PROGRAM
    RUN = '%s sources/lua_test.lua' % PROGRAM
    ORDER = 9

class JavaScriptLanguage(Language):
    """ JavaScript Language config. """

    NAME = 'JavaScript (node.js)'
    PROGRAM = safe_path('node')
    VERSION = '%s --version' % PROGRAM
    RUN = '%s sources/js_test.js' % PROGRAM
    ORDER = 10

class ActionScriptLanguage(Language):
    """ ActionScript Language config. """

    NAME = 'ActionScript3'
    PROGRAM = safe_path('/Applications/redtamarin_0/redshell')
    VERSION = '%s -Dversion' % PROGRAM
    RUN = '%s sources/actionscript_test.as --' % PROGRAM
    ORDER = 11

class PHPLanguage(Language):
    """ PHP Language config. """

    NAME = 'PHP'
    PROGRAM = safe_path('/usr/local/php5-5.5.13-20140530-105025/bin/php')
    VERSION = '%s --version' % PROGRAM
    RUN = '%s sources/php_test.php' % PROGRAM
    ORDER = 12

class RubyLanguage(Language):
    """ Ruby Language config. """

    NAME = 'Ruby'
    PROGRAM = safe_path('ruby')
    VERSION = '%s --version' % PROGRAM
    RUN = '%s sources/ruby_test.rb' % PROGRAM
    ORDER = 13

class PythonLanguage(Language):
    """ Python Language config. """

    NAME = 'Python'
    PROGRAM = safe_path('python3')
    VERSION = '%s --version' % PROGRAM
    RUN = '%s sources/python_test.py' % PROGRAM
    ORDER = 14

class PerlLanguage(Language):
    """ Perl Language config. """

    NAME = 'Perl'
    PROGRAM = safe_path('perl')
    VERSION = '%s --version' % PROGRAM
    RUN = '%s sources/perl_test.pl' % PROGRAM
    ORDER = 15

class BashLanguage(Language):
    """ Bash Language config. """

    NAME = 'Bash'
    PROGRAM = safe_path('bash')
    VERSION = 'bash --version'
    RUN = 'sources/bash_test.sh'
    ORDER = 16

class PrologLanguage(Language):
    """ Prolog Language config. """

    NAME = 'Prolog'
    PROGRAM = safe_path('/Applications/SWI-Prolog.app/Contents/MacOS/swipl')
    VERSION = '%s --version' % PROGRAM
    RUN = '%s sources/prolog_test.pl --' % PROGRAM
    CLEAN = ['sources/prolog_test.pl˜']
    ORDER = 17

class ErlLanguage(Language):
    """ Erlang Language config. """

    NAME = 'Erlang'
    PROGRAM = safe_path('escript')
    VERSION = '%s +V' % safe_path('erl')
    RUN = '%s sources/erlang_test.erl' % PROGRAM
    ORDER = 18

class CLispLanguage(Language):
    """ Common Lisp Language config. """

    NAME = 'Common Lisp'
    PROGRAM = safe_path('clisp')
    VERSION = '%s --version' % PROGRAM
    RUN = '%s sources/clisp_test.lisp' % PROGRAM
    ORDER = 19

class ClojureLanguage(Language):
    """ Clojure Language config. """

    NAME = 'Clojure'
    PROGRAM = 'java -cp /Applications/clojure-1.6.0/clojure-1.6.0.jar'
    VERSION = 'Clojure 1.6.0'
    RUN = '%s clojure.main sources/clojure_test.clj' % PROGRAM
    ORDER = 20

class FSLanguage(Language):
    """ F# Language config. """

    NAME = 'F#'
    PROGRAM = safe_path('fsharpc')
    VERSION = '%s --help' % PROGRAM
    COMPILE = '%s sources/fsharp_test.fs' % PROGRAM
    RUN = 'mono fsharp_test.exe'
    CLEAN = ['fsharp_test.exe']
    ORDER = 21

class HaskellLanguage(Language):
    """ Haskell Language config. """

    NAME = 'Haskell'
    PROGRAM = safe_path('runhaskell')
    VERSION = 'ghc --version'
    RUN = '%s sources/haskell_test.hs' % PROGRAM
    ORDER = 22

class SchemeLanguage(Language):
    """ Scheme Language config. """

    NAME = 'Scheme'
    PROGRAM = safe_path(\
        '/Applications/MIT:GNU Scheme.app/Contents/Resources/mit-scheme')
    VERSION = '%s --version' % PROGRAM
    RUN = '%s --quiet --load externals/format.scm < sources/scheme_test.scm \
        --args' % PROGRAM
    ORDER = 23
