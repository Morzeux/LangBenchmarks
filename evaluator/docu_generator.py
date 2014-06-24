# -*- coding: utf-8 -*-
'''
Created on 24.6.2014

@author: Morzeux
'''

import pygal, os
from evaluator import config as C

class DocuGenerator(object):
    
    URL = 'https://github.com/Morzeux/LangBenchmarks/tree/master/%s'
    
    README_TEMPLATE = """
# LangBenchmarks

This project is supposed for all people who are interested in difference
between performance for several programming languages. It can also serve
to compare syntax of many languages. As a bonus some functional a logical
programming languages are included as well. 

At now benchmark supports:

  * C
  * Objective-C
  * C#
  * Java
  * Pascal
  * JavaScript
  * PHP
  * Ruby
  * Python
  * Perl
  * Bash
  * Prolog
  * Common Lisp

More languages like Lua, Haskell, Scala, Clojure are comming soon...

If you have idea how to improve this script, or which language to add, feel
free to commit it :)

## Benchmark overview

Evaluation was simple. Two performance tests are written in several programming
languages and their computation speed is compared.

### Cycle test

This test evaluated speed of code in simple loop with variable iterations with
while clause.

```python
def cycle(n):
    i = 0
    while i < n:
        i += 1;
```

### Hanoi test

Test for extended recursion to solving Hanoi towers puzzle. To make it more
complex, six sticks are used instead of three with variable count of discs.

```python
def hanoi(n, start, dest, sticks):
    if n == 0:
        return
    
    temp = sticks - start - dest
    hanoi(n - 1, start, temp, sticks)
    hanoi(n - 1, temp, dest, sticks)
```

## Installation

Simply clone this repository. To set proper configuration for evaluated
languages, you need to edit `config.py` module located in `evaluator` package.

## Results

Here are my results obtained on my Apple Machine. Reason I used Apple was
environment, where I could use together C# (through Mono), Objective-C,
Bash and where I would use Swift in future.

### Environment

%s

### Compilers & Interpreters

%s

### Performance Tests

In performance tests, scripts were executed %d times with %d seconds timeout.
After this timeout script was killed. After executions, their times average
value were computed together with standard deviation. This values was used
to construct tables and graphs.
"""

    RESULTS_TEMPLATE = """
#### Test %d. - Discs %d, Iterations %d
    
%s
    
![alt text](%s "Bar graph results %d")

![alt text](%s "Box graph results %d")

"""

    RESULTS_DIR = 'results'

    @classmethod
    def _get_graph_filename(cls, filename, val):
        return '%s/%s' % (cls.RESULTS_DIR, filename % (val + 1))

    @classmethod
    def create_tables(cls, results):
        def get_value(lang, value):
            if lang[1].get(value) is None:
                return 'Dead'
            elif value.startswith('avg'):
                return '%.3fs' % lang[1].get(value)
            elif value.startswith('std'):
                return '%.3f%%' % lang[1].get(value)
        
        tables = []
        for test in results:
            header = ['Lang', 'Avg. cycles', 'Std. cycles', 'Avg. hanoi', 'Std. hanoi']
            sec_header = [':-----:' for _ in range(len(header))]
            table = [header, sec_header]
            for lang in test['results']:
                table.append([lang[0],
                              get_value(lang, 'avg_cycle'),
                              get_value(lang, 'std_cycle'),
                              get_value(lang, 'avg_hanoi'),
                              get_value(lang, 'std_hanoi')])
            
            table = '\n'.join(['| %s |' % ' | '.join(row) for row in table])
            tables.append(table.strip())
        return tables

    @classmethod
    def create_graphs(cls, results):

        graphs = []
        for i, test in enumerate(results):
            title = '%d. Test - disks: %d, iterations: %s' % (i + 1,
                                                              test['disks'],
                                                              test['iters'])

            bar_chart = pygal.Bar()
            bar_chart.title = title
            bar_chart.x_labels = [res[0] for res in test['results'] if res[1]]
            bar_chart.y_title = 'Time [s]'
            bar_chart.add('Cycle Test', [res[1]['avg_cycle'] \
                                         for res in test['results'] if res[1]])
            bar_chart.add('Hanoi Test', [res[1]['avg_hanoi'] \
                                         for res in test['results'] if res[1]])

            box_plot = pygal.Box()
            box_plot.title = title
            for res in test['results']:
                if res[1]:
                    box_plot.add(res[0], [res[1]['avg_cycle'],
                                          res[1]['avg_hanoi']])

            graphs.append((cls._get_graph_filename('bar_graph%d.svg', i),
                           cls._get_graph_filename('box_graph%d.svg', i)))
            bar_chart.render_to_file(graphs[-1][0])
            box_plot.render_to_file(graphs[-1][1])

        return graphs

    @classmethod
    def create_version_table(cls, versions):
        header = ['Language', 'Available Version']
        sec_header = [':-----:' for _ in range(len(header))]
        table = [header, sec_header]
        for line in versions.splitlines()[2:]:
            line = line.split(':')
            line[0] = line[0].replace(' compiler', '')
            line[1] = line[1].strip()
            table.append(line)

        return '\n'.join(['| %s |' % ' | '.join(row) for row in table]).strip()

    @classmethod
    def create_system_info_table(cls, system_info):
        header = ['Info', '']
        sec_header = [':-----:' for _ in range(2)]
        table = [header, sec_header]
        for line in system_info.splitlines()[2:]:
            line = line.split(':')
            line[0] = line[0].strip()
            line[1] = line[1].strip()
            table.append(line)

        return '\n'.join(['| %s |' % ' | '.join(row) for row in table]).strip()

    @classmethod
    def build_results_section(cls, results):
        tables = cls.create_tables(results)
        graphs = cls.create_graphs(results)

        text = ''
        for i, test in enumerate(results):
            j = i + 1
            res = cls.RESULTS_TEMPLATE % (j, test['disks'], test['iters'],
                                          tables[i], cls.URL % graphs[i][0],
                                          j, cls.URL % graphs[i][1], j)
            text += res.lstrip()

        return text

    @classmethod
    def generate_readme(cls, versions, system_info, results):
        if not os.path.exists(cls.RESULTS_DIR):
            os.makedirs(cls.RESULTS_DIR)

        versions = cls.create_version_table(versions)
        system_info = cls.create_system_info_table(system_info)
        text = '%s%s' % (cls.README_TEMPLATE % (system_info, versions,
                                                C.EVALUATIONS, C.TIMEOUT),
                         cls.build_results_section(results))

        with open('README.md', 'w') as flw:
            flw.write(text)
