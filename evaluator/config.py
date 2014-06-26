'''
Created on Jun 20, 2014

@author: Stefan Smihla
'''
import os, platform, shutil

if platform.system() == 'Windows':
    import win32api

def safe_path(path):
    """ Convert path to safe path. """
    path = shutil.which(os.path.normpath(path))
    if path and platform.system() == 'Windows':
        return win32api.GetShortPathName(path)
    else:
        return path

EVALUATIONS = 5
TIMEOUT = 120
TESTS = [(15, 6, 1000000),
         (20, 6, 10000000),
         (25, 6, 100000000),
         (30, 6, 1000000000)]

INKSCAPE_PATH = safe_path('/Applications/Inkscape.app/Contents/Resources/bin/inkscape')

class Language(object):
    """ Default config when not set. """

    NAME = None # Name of language - this name will be displayed in results
    PROGRAM = None # Path where compiler / interpreter can be found
    VERSION = None # What command I should execute if I want to check version?
    COMPILE = None # Command to compile source code
    RUN = None # Command to execute source code
    CLEAN = [] # Files which will be deleted after tests finish
    ORDER = -1 # Order to display

class CLanguage(Language):
    """ C Language config. """

    NAME = 'C'
    PROGRAM = safe_path('cc')
    VERSION = '%s --version' % PROGRAM
    COMPILE = '%s -Wall sources/c_test.c -o c_test' % PROGRAM
    RUN = './c_test'
    CLEAN = ['c_test']
    ORDER = 1

class ObjCLanguage(Language):
    """ Objective-C Language config. """

    NAME = 'Objective-C'
    PROGRAM = safe_path('gcc')
    VERSION = '%s --version' % PROGRAM
    COMPILE = '%s -o objc_test -Wall -std=c99 sources/objc_test.m -framework Foundation -lobjc' % PROGRAM
    RUN = './objc_test'
    CLEAN = ['objc_test']
    ORDER = 2

class CSLanguage(Language):
    """ C# Language config. """

    NAME = 'C#'
    PROGRAM = safe_path('mcs')
    VERSION = '%s --version' % PROGRAM
    COMPILE = '%s sources/csharp_test.cs' % PROGRAM
    RUN = 'mono sources/csharp_test.exe'
    CLEAN = ['sources/csharp_test.exe']
    ORDER = 3

class PascalLanguage(Language):
    """ Pascal Language config. """

    NAME = 'Pascal'
    PROGRAM = safe_path('fpc')
    VERSION = '%s -h' % PROGRAM
    COMPILE = '%s sources/pascal_test.pas' % PROGRAM
    RUN = 'sources/pascal_test'
    CLEAN = ['sources/pascal_test', 'sources/pascal_test.o']
    ORDER = 4

class JavaLanguage(Language):
    """ Java Language config. """

    NAME = 'Java'
    PROGRAM = safe_path('javac')
    VERSION = '%s -version' % PROGRAM
    COMPILE = '%s sources/java_test.java -d .' % PROGRAM
    RUN = 'java java_test'
    CLEAN = ['java_test.class']
    ORDER = 5

class JavaScriptLanguage(Language):
    """ JavaScript Language config. """

    NAME = 'JavaScript (node.js)'
    PROGRAM = safe_path('node')
    VERSION = '%s --version' % PROGRAM
    RUN = '%s sources/js_test.js' % PROGRAM
    ORDER = 6

class PHPLanguage(Language):
    """ PHP Language config. """

    NAME = 'PHP'
    PROGRAM = safe_path('/usr/local/php5-5.5.13-20140530-105025/bin/php')
    VERSION = '%s --version' % PROGRAM
    RUN = '%s sources/php_test.php' % PROGRAM
    ORDER = 7

class RubyLanguage(Language):
    """ Ruby Language config. """

    NAME = 'Ruby'
    PROGRAM = safe_path('ruby')
    VERSION = '%s --version' % PROGRAM
    RUN = '%s sources/ruby_test.rb' % PROGRAM
    ORDER = 8

class PythonLanguage(Language):
    """ Python Language config. """

    NAME = 'Python'
    PROGRAM = safe_path('python3')
    VERSION = '%s --version' % PROGRAM
    RUN = '%s sources/python_test.py' % PROGRAM
    ORDER = 9

class PerlLanguage(Language):
    """ Perl Language config. """

    NAME = 'Perl'
    PROGRAM = safe_path('perl')
    VERSION = '%s --version' % PROGRAM
    RUN = '%s sources/perl_test.pl' % PROGRAM
    ORDER = 10

class BashLanguage(Language):
    """ Bash Language config. """

    NAME = 'Bash'
    PROGRAM = safe_path('bash')
    VERSION = 'bash --version'
    RUN = 'sources/bash_test.sh'
    ORDER = 11

class PrologLanguage(Language):
    """ Prolog Language config. """

    NAME = 'Prolog'
    PROGRAM = safe_path('/Applications/SWI-Prolog.app/Contents/MacOS/swipl')
    VERSION = '%s --version' % PROGRAM
    RUN = '%s sources/prolog_test.pl' % PROGRAM
    CLEAN = ['sources/prolog_test.pl˜']
    ORDER = 12

class CLispLanguage(Language):
    """ Common Lisp Language config. """

    NAME = 'Common Lisp'
    PROGRAM = safe_path('clisp')
    VERSION = '%s --version' % PROGRAM
    RUN = '%s sources/clisp_test.lisp' % PROGRAM
    ORDER = 13
