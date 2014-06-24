'''
Created on 8.6.2014

@author: Stefan Smihla
'''

from evaluator.evaluator import Evaluator
from evaluator.docu_generator import DocuGenerator
from evaluator.languages import load_languages
from evaluator import config as C

def main():
    """ Main tester class. """
    languages = load_languages()

    versions = Evaluator.print_versions(languages)
    print(versions)
    system_info = Evaluator.print_system_info()
    print(system_info)
    Evaluator.compile_languages(languages)
    results = Evaluator.test_languages(languages, C.TESTS,
                                       C.EVALUATIONS, C.TIMEOUT)
    DocuGenerator.generate_readme(versions, system_info, results)
    Evaluator.cleanup(languages)

if __name__ == "__main__":
    main()
