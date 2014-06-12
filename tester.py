from evaluator.evaluator import Evaluator
from evaluator.languages import load_languages

CONFIG = 'config.ini'

def main():
    languages = load_languages(CONFIG)
    tests = [
             (10, 6, 1000),
             (15, 6, 100000),
             (20, 6, 10000000),
             (25, 6, 100000000),
             (30, 6, 1000000000),
             (32, 6, 4294967295)
            ]
    
    Evaluator.print_versions(languages)
    Evaluator.print_system_info()
    
    Evaluator.compile_languages(languages)
    Evaluator.test_languages(languages, tests, 1, 600)
    Evaluator.cleanup(languages)
    print()

if __name__ == "__main__":
    main()
