'''
Created on 8.6.2014

@author: Stefan Smihla
'''

from evaluator.evaluator import Evaluator
from evaluator.languages import load_languages

CONFIG = 'config.ini'
EVALUATIONS = 5
TIMEOUT = 1800
TESTS = [(10, 6, 1000),
         (15, 6, 100000),
         (20, 6, 10000000),
         (25, 6, 100000000),
         (30, 6, 1000000000),
         (32, 6, 4294967295)]

def main():
    """ Main tester class. """
    languages = load_languages(CONFIG)

    Evaluator.print_versions(languages)
    Evaluator.print_system_info()
    Evaluator.compile_languages(languages)
    Evaluator.test_languages(languages, TESTS, EVALUATIONS, TIMEOUT)
    Evaluator.cleanup(languages)

if __name__ == "__main__":
    main()
