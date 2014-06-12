'''
Created on 8.6.2014

@author: Morzeux
'''

import platform
import psutil
import math
import os
import re

class Evaluator():

    @classmethod
    def _compute_average(cls, values):
        return sum(values) / len(values)
    
    @classmethod
    def _compute_deviation(cls, values, average):
        return math.sqrt(sum([math.pow(val - average, 2) for val in values]) / len(values))
    
    @classmethod
    def _compute_rel_deviation(cls, average, deviation):
        return (deviation / average) * 100 if average else 0

    @classmethod
    def _format_output(cls, outputs):
        def get_time(line):
            try:
                return float(re.match(r'.*\s(\d+\.\d+)s\.', line).groups()[0])
            except:
                return False
        
        name = None
        hanoi = []
        cycle = []
        for output in outputs:
            output = [line.strip() for line in output.replace(',', '.').split('\n')]
            if not name:
                name = output[0][:-1]
                
            hanoi.append(get_time(output[1]))
            cycle.append(get_time(output[2]))
        
        avg_hanoi = cls._compute_average(hanoi)
        avg_cycle = cls._compute_average(cycle)
        std_hanoi = cls._compute_rel_deviation(avg_hanoi, cls._compute_deviation(hanoi, avg_hanoi))
        std_cycle = cls._compute_rel_deviation(avg_cycle, cls._compute_deviation(cycle, avg_cycle))
        
        text = '  %s:' % name
        text += '\n    Hanoi: %.3fs (SD %.2f%%)' % (avg_hanoi, std_hanoi)
        text += '\n    Cycles: %.3fs (SD %.2f%%)' % (avg_cycle, std_cycle)
        return text

    @classmethod
    def print_versions(cls, languages):
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
        print('System:')
        print('*' * 60)        
        print('Operating System: %s' % platform.platform())
        print('Processor: %s' % platform.processor())
        print('Total memory: %.3fGB' % (float(psutil.phymem_usage().total) / 1024**3))
        print('')

    @classmethod
    def compile_languages(cls, languages):
        print('Compiling results:')
        print('*' * 60)
        for lang in languages:
            if hasattr(lang, 'compile'):
                print('Compiling %s...' % lang.name, end=' ')
                print(lang.compile())
        print('')

    @classmethod
    def test_languages(cls, languages, tests, average=1, timeout=None):
        print('Test results (%d evaluations):' % average)
        print('*' * 60)
        
        for i, test in enumerate(tests):
            params = ' '.join([str(i) for i in test])
            print('%d. Hanoi(disks=%d, sticks=%d); Cycles(iters=%d)' % (i + 1, test[0], test[1], test[2]))
            for lang in languages:
                if lang.version:
                    output = []
                    for _ in range(average):
                        output.append(lang.evaluate_with_timeout(params, timeout))
                        if 'Killed' in output[-1]:
                            print('  %s:\n    Hanoi: Killed\n    Cycles: Killed' % lang.name)
                            break
                    else:
                        print(cls._format_output(output))
            print('')

        print('')

    @classmethod
    def cleanup(cls, languages):
        print('*' * 60)
        print('Cleaning up...', end=' ')
        for lang in languages:
            if hasattr(lang, 'output') and os.path.isfile(lang.output):
                os.remove(lang.output)
        print('OK\n')
