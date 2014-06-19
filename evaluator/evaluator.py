'''
Created on 8.6.2014

@author: Stefan Smihla
'''

import platform
import psutil
import math
import re

class Evaluator():
    """ Static helper class to evaluate languages. """

    @classmethod
    def __init__(cls):
        pass

    @classmethod
    def _compute_average(cls, values):
        """ Computes average value. """
        return sum(values) / len(values)

    @classmethod
    def _compute_deviation(cls, values, average):
        """ Computes standard deviation. """
        return math.sqrt(sum([math.pow(val - average, 2) \
                              for val in values]) / len(values))

    @classmethod
    def _compute_rel_deviation(cls, average, values):
        """ Computes relative deviation. """
        deviation = cls._compute_deviation(values, average)
        return (deviation / average) * 100 if average else 0

    @classmethod
    def _format_output(cls, outputs):
        """ Formats output from scripts outputs. """

        def get_time(line):
            """ Regex parse time value from output. """
            return float(re.match(r'.*\s(\d+\.\d+)s\.', line).groups()[0])

        name = None
        hanoi = []
        cycle = []
        for output in outputs:
            output = [line.strip() for line in output.
                      replace(',', '.').split('\n')]

            if not name:
                name = output[0][:-1]

            hanoi.append(get_time(output[1]))
            cycle.append(get_time(output[2]))

        avg_hanoi = cls._compute_average(hanoi)
        avg_cycle = cls._compute_average(cycle)
        std_hanoi = cls._compute_rel_deviation(avg_hanoi, hanoi)
        std_cycle = cls._compute_rel_deviation(avg_cycle, cycle)

        text = '  %s:' % name
        text += '\n    Hanoi: %.3fs (SD %.2f%%)' % (avg_hanoi, std_hanoi)
        text += '\n    Cycles: %.3fs (SD %.2f%%)' % (avg_cycle, std_cycle)
        return text

    @classmethod
    def print_versions(cls, languages):
        """ Prints versions of evaluated languages. """

        print('Available compilers:')
        print('*' * 60)
        for lang in languages:
            if lang.version:
                print('%s compiler: %s' % (lang.name, lang.version))
            else:
                print('%s compiler: Not available' % lang.name)
        print('')

    @classmethod
    def print_system_info(cls):
        """ Prints actual system environment information. """

        print('System:')
        print('*' * 60)
        print('Operating System: %s' % platform.platform())
        print('Processor: %s' % platform.processor())
        print('Total memory: %.3fGB' % (float(psutil.
                                              phymem_usage().total) / 1024**3))
        print('')

    @classmethod
    def compile_languages(cls, languages):
        """ Compiles languages into binary form. """

        print('Compiling results:')
        print('*' * 60)
        for lang in languages:
            if hasattr(lang, 'compile'):
                print('Compiling %s...' % lang.name, end=' ')
                print(lang.compile())
        print('')

    @classmethod
    def test_languages(cls, languages, tests, average=1, timeout=None):
        """ Evaluates languages. """
        bad_output = '  %s:\n    Hanoi: Killed\n    Cycles: Killed'

        print('Test results (%d evaluations):' % average)
        print('*' * 60)

        for i, test in enumerate(tests):
            params = ' '.join([str(i) for i in test])
            print('%d. Hanoi(disks=%d, sticks=%d); Cycles(iters=%d)' \
                  % (i + 1, test[0], test[1], test[2]))

            for lang in languages:
                if lang.version:
                    output = []
                    for _ in range(average):
                        output.append(lang.evaluate_with_timeout(params,
                                                                 timeout))
                        if 'Killed' in output[-1]:
                            print(bad_output % lang.name)
                            break
                    else:
                        print(cls._format_output(output))
            print('')

    @classmethod
    def cleanup(cls, languages):
        """ Removes created binaries. """

        print('*' * 60)
        print('Cleaning up...', end=' ')
        for lang in languages:
            lang.clean_up()
        print('OK\n')
