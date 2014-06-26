
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

| Info |  |
| :-----: | :-----: |
| Operating System | Darwin-13.2.0-x86_64-i386-64bit |
| Processor | i386 |
| Total memory | 2.000GB |

### Compilers & Interpreters

| Language | Available Version |
| :-----: | :-----: |
| C | Apple LLVM version 5.1 (clang-503.0.40) (based on LLVM 3.4svn) |
| Objective-C | Apple LLVM version 5.1 (clang-503.0.40) (based on LLVM 3.4svn) |
| C# | Mono C# compiler version 3.4.0.0 |
| Pascal | Free Pascal Compiler version 2.6.4 [2014/02/26] for i386 |
| Java | javac 1.8.0_05 |
| JavaScript (node.js) | v0.10.29 |
| PHP | PHP 5.5.13 (cli) (built |  May 30 2014 10 | 43 | 29) |
| Ruby | ruby 2.0.0p451 (2014-02-24 revision 45167) [universal.x86_64-darwin13] |
| Python | Python 3.4.1 |
| Perl | This is perl 5, version 16, subversion 3 (v5.16.3) built for darwin-thread-multi-2level |
| Bash | GNU bash, version 3.2.51(1)-release (x86_64-apple-darwin13) |
| Prolog | SWI-Prolog version 6.6.6 for x86_64-darwin13.1.0 |
| Common Lisp | GNU CLISP 2.49 (2010-07-07) (built 3612292961) (memory 3612293171) |

### Performance Tests

In performance tests, scripts were executed 5 times with 120 seconds timeout.
After this timeout script was killed. After executions, their times average
value were computed together with standard deviation. This values was used
to construct tables and graphs.
#### Test 1. - Discs 15, Iterations 1000000
    
| Lang | Avg. cycles | Std. cycles | Avg. hanoi | Std. hanoi |
| :-----: | :-----: | :-----: | :-----: | :-----: |
| C | 0.003s | 74.54% | 0.000s | 0.00% |
| Objective-C | 0.003s | 0.00% | 0.001s | 0.00% |
| C# | 0.005s | 40.00% | 0.000s | 0.00% |
| Pascal | 0.003s | 29.81% | 0.000s | 0.00% |
| Java | 0.003s | 21.08% | 0.001s | 0.00% |
| JavaScript | 0.001s | 77.46% | 0.002s | 0.00% |
| PHP | 0.156s | 1.77% | 0.133s | 11.64% |
| Ruby | 0.027s | 3.31% | 0.007s | 11.07% |
| Python | 0.131s | 6.14% | 0.022s | 4.55% |
| Perl | 0.111s | 2.01% | 0.053s | 5.13% |
| Bash | 26.570s | 3.87% | 4.540s | 14.15% |
| Prolog | 0.053s | 8.00% | 0.005s | 54.41% |
| Common Lisp | 1.452s | 4.52% | 0.137s | 16.48% |

![Bar graph results 1](results/bar_graph1.png)

![Box graph results 1](results/log_bar_graph1.png)

#### Test 2. - Discs 20, Iterations 10000000
    
| Lang | Avg. cycles | Std. cycles | Avg. hanoi | Std. hanoi |
| :-----: | :-----: | :-----: | :-----: | :-----: |
| C | 0.027s | 4.68% | 0.010s | 4.47% |
| Objective-C | 0.028s | 3.57% | 0.017s | 2.63% |
| C# | 0.044s | 2.87% | 0.010s | 6.32% |
| Pascal | 0.028s | 3.19% | 0.010s | 10.95% |
| Java | 0.011s | 5.75% | 0.007s | 12.78% |
| JavaScript | 0.012s | 9.13% | 0.019s | 4.08% |
| PHP | 1.631s | 3.74% | 4.305s | 4.04% |
| Ruby | 0.316s | 5.22% | 0.279s | 6.37% |
| Python | 1.512s | 18.63% | 0.774s | 4.74% |
| Perl | 1.141s | 1.08% | 1.674s | 1.48% |
| Bash | Dead | Dead | Dead | Dead |
| Prolog | 0.949s | 58.89% | 1.191s | 59.66% |
| Common Lisp | 17.246s | 17.91% | 4.957s | 44.24% |

![Bar graph results 2](results/bar_graph2.png)

![Box graph results 2](results/log_bar_graph2.png)

#### Test 3. - Discs 25, Iterations 100000000
    
| Lang | Avg. cycles | Std. cycles | Avg. hanoi | Std. hanoi |
| :-----: | :-----: | :-----: | :-----: | :-----: |
| C | 0.288s | 3.26% | 0.324s | 2.38% |
| Objective-C | 0.283s | 1.55% | 0.551s | 3.85% |
| C# | 0.447s | 0.69% | 0.324s | 4.87% |
| Pascal | 0.287s | 1.69% | 0.367s | 2.00% |
| Java | 0.084s | 1.06% | 0.158s | 1.52% |
| JavaScript | 0.125s | 2.99% | 0.573s | 4.04% |
| PHP | Dead | Dead | Dead | Dead |
| Ruby | 3.197s | 19.56% | 9.831s | 20.25% |
| Python | 13.610s | 10.15% | 23.961s | 10.21% |
| Perl | 12.690s | 17.53% | 63.436s | 13.12% |
| Bash | Dead | Dead | Dead | Dead |
| Prolog | 6.723s | 27.51% | 20.057s | 1.30% |
| Common Lisp | Dead | Dead | Dead | Dead |

![Bar graph results 3](results/bar_graph3.png)

![Box graph results 3](results/log_bar_graph3.png)

#### Test 4. - Discs 30, Iterations 1000000000
    
| Lang | Avg. cycles | Std. cycles | Avg. hanoi | Std. hanoi |
| :-----: | :-----: | :-----: | :-----: | :-----: |
| C | 2.881s | 2.00% | 11.838s | 14.88% |
| Objective-C | 2.926s | 2.83% | 20.272s | 9.46% |
| C# | 5.765s | 21.54% | 13.811s | 28.42% |
| Pascal | 3.015s | 5.93% | 15.240s | 19.90% |
| Java | 0.838s | 3.87% | 5.082s | 11.49% |
| JavaScript | 1.368s | 12.25% | 21.462s | 8.63% |
| PHP | Dead | Dead | Dead | Dead |
| Ruby | Dead | Dead | Dead | Dead |
| Python | Dead | Dead | Dead | Dead |
| Perl | Dead | Dead | Dead | Dead |
| Bash | Dead | Dead | Dead | Dead |
| Prolog | Dead | Dead | Dead | Dead |
| Common Lisp | Dead | Dead | Dead | Dead |

![Bar graph results 4](results/bar_graph4.png)

![Box graph results 4](results/log_bar_graph4.png)

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
