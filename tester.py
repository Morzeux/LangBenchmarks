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

# TO DO:
#   - add parameters, usage
#   - add prerequisities check
#   - add Eratosen test
#   - add D, F#, Erlang, Lua

from evaluator.evaluator import Evaluator
from evaluator.docu_generator import DocuGenerator
from evaluator.languages import load_languages
from evaluator import config as C

def license():
    return """
Languages Benchmark Script Copyright (C) 2014 Stefan Smihla

This program comes with ABSOLUTELY NO WARRANTY.
This is free software, and you are welcome to redistribute it
under certain conditions of GNU General Public License.
""".strip()

def main():
    """ Main tester class. """
    print(license())
    print('')

    languages = load_languages()

    versions = Evaluator.print_versions(languages)
    print(versions)
    system_info = Evaluator.print_system_info()
    print(system_info)
    Evaluator.compile_languages(languages)
    results = Evaluator.test_languages(languages, C.TESTS,
                                       C.EVALUATIONS, C.TIMEOUT)
    print('*' * 60)
    DocuGenerator.generate_readme(versions, system_info, results)
    Evaluator.cleanup(languages)

if __name__ == "__main__":
    main()
