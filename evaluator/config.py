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

class Language(object):
    NAME = None
    PROGRAM = None
    VERSION = None
    COMPILE = None
    RUN = None
    CLEAN = []
    ORDER = -1
    
class CLanguage(Language):
    NAME = 'C'
    PROGRAM = safe_path('cc')
    VERSION = '%s --version' % PROGRAM
    COMPILE = '%s -Wall sources/c_test.c -o c_test' % PROGRAM 
    RUN = './c_test'
    CLEAN = ['c_test']
    ORDER = 1

class ObjCLanguage(Language):
    NAME = 'Objective-C'
    PROGRAM = safe_path('gcc')
    VERSION = '%s --version' % PROGRAM
    COMPILE = '%s -o objc_test -Wall -std=c99 sources/objc_test.m -framework Foundation -lobjc' % PROGRAM 
    RUN = './objc_test'
    CLEAN = ['objc_test']
    ORDER = 2

class CSLanguage(Language):
    NAME = 'C#'
    PROGRAM = safe_path('mcs')
    VERSION = '%s --version' % PROGRAM
    COMPILE = '%s sources/csharp_test.cs' % PROGRAM 
    RUN = 'mono sources/csharp_test.exe'
    CLEAN = ['sources/csharp_test.exe']
    ORDER = 3

class PascalLanguage(Language):
    NAME = 'Pascal'
    PROGRAM = safe_path('fpc')
    VERSION = '%s -h' % PROGRAM
    COMPILE = '%s sources/pascal_test.pas' % PROGRAM 
    RUN = 'sources/pascal_test'
    CLEAN = ['sources/pascal_test', 'sources/pascal_test.o']
    ORDER = 4

class JavaLanguage(Language):
    NAME = 'Java'
    PROGRAM = safe_path('javac')
    VERSION = '%s -version' % PROGRAM
    COMPILE = '%s sources/java_test.java -d .' % PROGRAM 
    RUN = 'java java_test'
    CLEAN = ['java_test.class']
    ORDER = 5

class JavaScriptLanguage(Language):
    NAME = 'JavaScript (node.js)'
    PROGRAM = safe_path('node')
    VERSION = '%s --version' % PROGRAM
    RUN = '%s sources/js_test.js' % PROGRAM
    ORDER = 6

class PHPLanguage(Language):
    NAME = 'PHP'
    PROGRAM = safe_path('/usr/local/php5-5.5.13-20140530-105025/bin/php')
    VERSION = '%s --version' % PROGRAM
    RUN = '%s sources/php_test.php' % PROGRAM
    ORDER = 7

class RubyLanguage(Language):
    NAME = 'Ruby'
    PROGRAM = safe_path('ruby')
    VERSION = '%s --version' % PROGRAM
    RUN = '%s sources/ruby_test.rb' % PROGRAM
    ORDER = 8

class PythonLanguage(Language):
    NAME = 'Python'
    PROGRAM = safe_path('python3')
    VERSION = '%s --version' % PROGRAM
    RUN = '%s sources/python_test.py' % PROGRAM
    ORDER = 9

class PerlLanguage(Language):
    NAME = 'Perl'
    PROGRAM = safe_path('perl')
    VERSION = '%s --version' % PROGRAM
    RUN = '%s sources/perl_test.pl' % PROGRAM
    ORDER = 10

class BashLanguage(Language):
    NAME = 'Bash'
    PROGRAM = safe_path('bash')
    VERSION = 'bash --version'
    RUN = 'sources/bash_test.sh'
    ORDER = 11

class PrologLanguage(Language):
    NAME = 'Prolog'
    PROGRAM = safe_path('/Applications/SWI-Prolog.app/Contents/MacOS/swipl')
    VERSION = '%s --version' % PROGRAM
    RUN = '%s sources/prolog_test.pl' % PROGRAM
    CLEAN = ['sources/prolog_test.pl˜']
    ORDER = 12

class CLispLanguage(Language):
    NAME = 'Common Lisp'
    PROGRAM = safe_path('clisp')
    VERSION = '%s --version' % PROGRAM
    RUN = '%s sources/clisp_test.lisp' % PROGRAM
    ORDER = 13
