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

import platform
import psutil
import math
import re

class Evaluator():
    """ Static helper class to evaluate languages. """

    results = {}

    @classmethod
    def __init__(cls):
        pass

    @classmethod
    def _compute_average(cls, values):
        """ Computes average value. """
        return int((sum(values) / len(values)) * 1000) / 1000

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
    def _format_output(cls, outputs, results):
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

            try:
                if not name:
                    name = output[0][:-1]

                hanoi.append(get_time(output[1]))
                cycle.append(get_time(output[2]))
            except (AttributeError, IndexError):
                return 'FAIL - %s' % output

        avg_hanoi = cls._compute_average(hanoi)
        avg_cycle = cls._compute_average(cycle)
        std_hanoi = cls._compute_rel_deviation(avg_hanoi, hanoi)
        std_cycle = cls._compute_rel_deviation(avg_cycle, cycle)

        results.append((name, {'hanoi_times': hanoi,
                               'cycles_times': cycle,
                               'avg_hanoi': avg_hanoi,
                               'avg_cycle': avg_cycle,
                               'std_hanoi': std_hanoi,
                               'std_cycle': std_cycle}))

        if len(outputs) == 1:
            std_hanoi = ''
            std_cycle = ''
        else:
            std_hanoi = '(SD %.2f%%)' % std_hanoi
            std_cycle = '(SD %.2f%%)' % std_cycle

        text = '  %s:' % name
        text += '\n    Cycles: %.3fs %s' % (avg_cycle, std_cycle)
        text += '\n    Hanoi: %.3fs %s' % (avg_hanoi, std_hanoi)
        return text

    @classmethod
    def print_versions(cls, languages):
        """ Prints versions of evaluated languages. """

        text = 'Available compilers:\n'
        text += '*' * 60 + '\n'
        for lang in languages:
            if lang.available:
                text += '%s compiler: %s\n' % (lang.name, lang.version)
            else:
                text += '%s compiler: Not available\n' % lang.name

        return text

    @classmethod
    def print_system_info(cls):
        """ Prints actual system environment information. """

        text = 'System:\n'
        text += '*' * 60 + '\n'
        text += 'Operating System: %s\n' % platform.platform()
        text += 'Processor: %s\n' % platform.processor()
        text += 'Total memory: %.3fGB\n' % (float(psutil.
                                                  phymem_usage().
                                                  total) / 1024**3)
        return text

    @classmethod
    def compile_languages(cls, languages):
        """ Compiles languages into binary form. """

        print('Compiling results:')
        print('*' * 60)
        for lang in languages:
            if hasattr(lang, 'compile') and lang.available:
                print('Compiling %s...' % lang.name, end=' ')
                print(lang.compile())
        print('')

    @classmethod
    def test_languages(cls, languages, tests, average=1, timeout=None):
        """ Evaluates languages. """
        bad_output = '  %s:\n    Cycles: Dead (timeout)\n    Hanoi: Dead (timeout)'
        results = []

        print('Test results (%d evaluations):' % average)
        print('*' * 60)

        for i, test in enumerate(tests):
            params = ' '.join([str(i) for i in test])
            print('%d. Hanoi(disks=%d, sticks=%d); Cycles(iters=%d)' \
                  % (i + 1, test[0], test[1], test[2]))

            results.append({'disks': test[0], 'sticks': test[1],
                            'iters': test[2], 'results': []})

            for lang in languages:
                if lang.available:
                    output = []
                    for _ in range(average):
                        output.append(lang.evaluate_with_timeout(params,
                                                                 timeout))
                        if 'Killed' in output[-1]:
                            results[-1]['results'].append((lang.name, {}))
                            print(bad_output % lang.name)
                            break
                    else:
                        print(cls._format_output(output,
                                                 results[-1]['results']))
            print('')
        return results

    @classmethod
    def cleanup(cls, languages):
        """ Removes created binaries. """

        print('Cleaning up...', end=' ')
        for lang in languages:
            if lang.available:
                lang.clean_up()
        print('OK\n')
