'''
Created on 8.6.2014

@author: Stefan Smihla
'''

from evaluator.evaluator import Evaluator
from evaluator.languages import load_languages
from evaluator import config as C

def main():
    """ Main tester class. """
    languages = load_languages()

    Evaluator.print_versions(languages)
    Evaluator.print_system_info()
    Evaluator.compile_languages(languages)
    Evaluator.test_languages(languages, C.TESTS, C.EVALUATIONS, C.TIMEOUT)
    Evaluator.cleanup(languages)

if __name__ == "__main__":
    main()
