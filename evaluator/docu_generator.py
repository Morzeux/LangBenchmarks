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

import pygal
import os, sys
import copy
from evaluator.languages import Language
from evaluator import config as C

class DocuGenerator(object):
    """ This module generates README.md for GitHub."""

    README_TEMPLATE = """
# LangBenchmarks

This project is supposed for all people who are interested in difference
between performance for several programming languages. It can also serve
to compare syntax of many languages. As a bonus some functional a logical
programming languages are included as well. 

At now benchmark supports:

  * C
  * C++
  * Objective-C
  * C#
  * D
  * Pascal
  * Java
  * Scala
  * Lua
  * JavaScript
  * ActionScript
  * PHP
  * Ruby
  * Python
  * Perl
  * Bash
  * Prolog
  * Erlang
  * Common Lisp
  * Clojure
  * F#
  * Haskell
  * Scheme

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
        i += 1
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

![Bar graph results %d](%s)

![Box graph results %d](%s)

"""

    LICENSE = """
## License
```
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
```
"""

    RESULTS_DIR = 'results'

    @classmethod
    def save_graph(cls, graph, filename):
        """ Saves graphs in svg format. """

        svg_output = '%s/%s.svg' % (cls.RESULTS_DIR, filename)
        png_output = '%s/%s.png' % (cls.RESULTS_DIR, filename)
        graph.render_to_file(svg_output)
        Language.run_process('%s -f %s -e %s' % (C.INKSCAPE_PATH, svg_output,
                                                 png_output))
        os.remove(svg_output)
        return png_output

    @classmethod
    def create_tables(cls, results):
        """ Creates table in Markdown language. """

        def get_value(lang, value):
            """ Returns formatted value for table from results. """

            if lang[1].get(value) is None:
                return 'Dead'
            elif value.startswith('avg'):
                return '%.3fs' % lang[1].get(value)
            elif value.startswith('std'):
                return '%.2f%%' % lang[1].get(value)

        tables = []
        for test in results:
            header = ['Lang', 'Avg. cycles', 'Std. cycles',
                      'Avg. hanoi', 'Std. hanoi']
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
        """ Creates graphs from results. """

        graphs = []
        for i, test in enumerate(results):
            title = '%d. Test - disks: %d, iterations: %s' % (i + 1,
                                                              test['disks'],
                                                              test['iters'])

            bar_chart = pygal.Bar(legend_at_bottom=True,
                                  value_formatter=lambda x: '%.3fs' % x)
            bar_chart.title = '%s - linear bar chart' % title
            bar_chart.x_labels = [res[0] for res in test['results'] if res[1]]
            bar_chart.y_title = 'Time [s]'
            bar_chart.add('Cycle Test', [res[1]['avg_cycle'] \
                                         for res in test['results'] if res[1]])
            bar_chart.add('Hanoi Test', [res[1]['avg_hanoi'] \
                                         for res in test['results'] if res[1]])

            log_bar_chart = copy.deepcopy(bar_chart)
            log_bar_chart.title = '%s - logaritmic bar chart' % title
            log_bar_chart.config.logarithmic = True

            graphs.append((cls.save_graph(bar_chart, 'bar_graph%d' % (i + 1)),
                           cls.save_graph(log_bar_chart,
                                          'log_bar_graph%d' % (i + 1))))

        return graphs

    @classmethod
    def create_version_table(cls, versions):
        """ Creates table with versions of compilers and interpreters. """

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
        """ Creates table with system environment info. """

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
        """ Builds results section info. """

        tables = cls.create_tables(results)
        graphs = cls.create_graphs(results)

        text = ''
        for i, test in enumerate(results):
            j = i + 1
            res = cls.RESULTS_TEMPLATE % (j, test['disks'], test['iters'],
                                          tables[i], j, graphs[i][0],
                                          j, graphs[i][1])
            text += res.lstrip()

        return text

    @classmethod
    def generate_readme(cls, versions, system_info, results):
        """ Generates README.md in Markdown syntax with all necessary info. """
        if not C.INKSCAPE_PATH:
            print('Inkscape not found. README.md was skipped.')
            return

        print('Generating README.md...', end=' ')
        sys.stdout.flush()

        if not os.path.exists(cls.RESULTS_DIR):
            os.makedirs(cls.RESULTS_DIR)

        versions = cls.create_version_table(versions)
        system_info = cls.create_system_info_table(system_info)
        text = '%s%s%s\n' % (cls.README_TEMPLATE % (system_info, versions,
                                                    C.EVALUATIONS, C.TIMEOUT),
                             cls.build_results_section(results),
                             cls.LICENSE.strip())

        with open('README.md', 'w') as flw:
            flw.write(text)

        print('OK')
