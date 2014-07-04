
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
  * PHP
  * Ruby
  * Python
  * Perl
  * Bash
  * Prolog
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

| Info |  |
| :-----: | :-----: |
| Operating System | Darwin-13.2.0-x86_64-i386-64bit |
| Processor | i386 |
| Total memory | 2.000GB |

### Compilers & Interpreters

| Language | Available Version |
| :-----: | :-----: |
| C | Apple LLVM version 5.1 (clang-503.0.40) (based on LLVM 3.4svn) |
| C++ | Apple LLVM version 5.1 (clang-503.0.40) (based on LLVM 3.4svn) |
| Objective-C | Apple LLVM version 5.1 (clang-503.0.40) (based on LLVM 3.4svn) |
| C# | Mono C# compiler version 3.4.0.0 |
| D | DMD64 D Compiler v2.065 |
| Pascal | Free Pascal Compiler version 2.6.4 [2014/02/26] for i386 |
| Java | javac 1.8.0_05 |
| Scala | Scala code runner version 2.11.1 -- Copyright 2002-2013, LAMP/EPFL |
| Lua | Lua 5.2.3  Copyright (C) 1994-2013 Lua.org, PUC-Rio |
| JavaScript (node.js) | v0.10.29 |
| PHP | PHP 5.5.13 (cli) (built |  May 30 2014 10 | 43 | 29) |
| Ruby | ruby 2.0.0p451 (2014-02-24 revision 45167) [universal.x86_64-darwin13] |
| Python | Python 3.4.1 |
| Perl | This is perl 5, version 16, subversion 3 (v5.16.3) built for darwin-thread-multi-2level |
| Bash | GNU bash, version 3.2.51(1)-release (x86_64-apple-darwin13) |
| Prolog | SWI-Prolog version 6.6.6 for x86_64-darwin13.1.0 |
| Common Lisp | GNU CLISP 2.49 (2010-07-07) (built 3612292961) (memory 3612293171) |
| Clojure | Clojure 1.6.0 |
| F# | F# Compiler for F# 3.1 (Open Source Edition) |
| Haskell | The Glorious Glasgow Haskell Compilation System, version 7.6.3 |
| Scheme | MIT/GNU Scheme microcode 15.3 |

### Performance Tests

In performance tests, scripts were executed 5 times with 120 seconds timeout.
After this timeout script was killed. After executions, their times average
value were computed together with standard deviation. This values was used
to construct tables and graphs.
#### Test 1. - Discs 15, Iterations 1000000
    
| Lang | Avg. cycles | Std. cycles | Avg. hanoi | Std. hanoi |
| :-----: | :-----: | :-----: | :-----: | :-----: |
| C | 0.003s | 0.00% | 0.000s | 0.00% |
| C++ | 0.003s | 0.00% | 0.000s | 0.00% |
| Objective-C | 0.003s | 0.00% | 0.001s | 0.00% |
| C# | 0.004s | 22.36% | 0.000s | 0.00% |
| D | 0.002s | 0.00% | 0.000s | 0.00% |
| Pascal | 0.003s | 97.75% | 0.000s | 0.00% |
| Java | 0.004s | 15.81% | 0.001s | 0.00% |
| Scala | 0.005s | 30.98% | 0.002s | 54.77% |
| Lua | 0.134s | 2.93% | 0.007s | 9.04% |
| JavaScript | 0.002s | 0.00% | 0.001s | 100.00% |
| PHP | 0.156s | 1.99% | 0.137s | 9.63% |
| Ruby | 0.028s | 3.57% | 0.008s | 17.68% |
| Python | 0.126s | 3.62% | 0.021s | 4.26% |
| Perl | 0.110s | 1.91% | 0.056s | 18.59% |
| Bash | 29.762s | 11.29% | 4.674s | 11.92% |
| Prolog | 0.053s | 5.27% | 0.005s | 35.78% |
| Common Lisp | 1.410s | 2.35% | 0.126s | 5.39% |
| Clojure | 0.074s | 38.51% | 0.033s | 9.68% |
| F# | 0.001s | 44.72% | 0.001s | 0.00% |
| Haskell | 1.356s | 3.31% | 0.121s | 4.10% |
| Scheme | 0.688s | 4.03% | 0.077s | 3.34% |

![Bar graph results 1](results/bar_graph1.png)

![Box graph results 1](results/log_bar_graph1.png)

#### Test 2. - Discs 20, Iterations 10000000
    
| Lang | Avg. cycles | Std. cycles | Avg. hanoi | Std. hanoi |
| :-----: | :-----: | :-----: | :-----: | :-----: |
| C | 0.032s | 12.10% | 0.011s | 16.26% |
| C++ | 0.029s | 2.18% | 0.011s | 17.72% |
| Objective-C | 0.031s | 11.90% | 0.018s | 8.61% |
| C# | 0.045s | 3.44% | 0.009s | 9.94% |
| D | 0.028s | 7.32% | 0.011s | 5.75% |
| Pascal | 0.028s | 5.30% | 0.010s | 10.00% |
| Java | 0.011s | 4.07% | 0.006s | 24.72% |
| Scala | 0.011s | 9.09% | 0.008s | 13.69% |
| Lua | 1.378s | 3.11% | 0.244s | 8.76% |
| JavaScript | 0.013s | 9.10% | 0.019s | 3.33% |
| PHP | 1.664s | 2.81% | 4.139s | 0.80% |
| Ruby | 0.304s | 8.21% | 0.267s | 8.53% |
| Python | 1.301s | 1.16% | 0.724s | 0.56% |
| Perl | 1.148s | 2.09% | 1.763s | 1.19% |
| Bash | Dead | Dead | Dead | Dead |
| Prolog | 0.545s | 4.31% | 0.614s | 2.31% |
| Common Lisp | 16.654s | 15.09% | 4.356s | 20.46% |
| Clojure | 0.149s | 10.71% | 0.195s | 14.03% |
| F# | 0.012s | 11.79% | 0.011s | 9.96% |
| Haskell | 12.705s | 1.04% | 3.722s | 0.98% |
| Scheme | 6.368s | 2.47% | 2.383s | 1.82% |

![Bar graph results 2](results/bar_graph2.png)

![Box graph results 2](results/log_bar_graph2.png)

#### Test 3. - Discs 25, Iterations 100000000
    
| Lang | Avg. cycles | Std. cycles | Avg. hanoi | Std. hanoi |
| :-----: | :-----: | :-----: | :-----: | :-----: |
| C | 0.559s | 42.68% | 0.553s | 50.73% |
| C++ | 0.288s | 2.82% | 0.316s | 0.66% |
| Objective-C | 0.281s | 1.68% | 0.543s | 1.67% |
| C# | 0.449s | 1.02% | 0.327s | 4.56% |
| D | 0.282s | 0.67% | 0.387s | 3.51% |
| Pascal | 0.287s | 3.67% | 0.352s | 1.85% |
| Java | 0.083s | 1.52% | 0.158s | 2.62% |
| Scala | 0.085s | 1.74% | 0.196s | 5.89% |
| Lua | 13.688s | 1.86% | 7.906s | 16.04% |
| JavaScript | 0.127s | 3.13% | 0.575s | 3.62% |
| PHP | Dead | Dead | Dead | Dead |
| Ruby | 3.067s | 11.89% | 8.640s | 10.14% |
| Python | 13.367s | 7.43% | 25.024s | 10.76% |
| Perl | 13.058s | 18.20% | 55.989s | 4.80% |
| Bash | Dead | Dead | Dead | Dead |
| Prolog | 9.450s | 15.30% | 21.587s | 8.83% |
| Common Lisp | Dead | Dead | Dead | Dead |
| Clojure | 3.838s | 145.34% | 1.655s | 1.60% |
| F# | 0.124s | 1.08% | 0.317s | 3.50% |
| Haskell | Dead | Dead | Dead | Dead |
| Scheme | Dead | Dead | Dead | Dead |

![Bar graph results 3](results/bar_graph3.png)

![Box graph results 3](results/log_bar_graph3.png)

#### Test 4. - Discs 30, Iterations 1000000000
    
| Lang | Avg. cycles | Std. cycles | Avg. hanoi | Std. hanoi |
| :-----: | :-----: | :-----: | :-----: | :-----: |
| C | 3.453s | 28.48% | 11.015s | 8.45% |
| C++ | 3.059s | 9.30% | 11.422s | 15.96% |
| Objective-C | 2.877s | 1.46% | 20.990s | 3.98% |
| C# | 4.593s | 0.70% | 10.478s | 0.91% |
| D | 2.932s | 0.81% | 13.157s | 6.06% |
| Pascal | 3.088s | 10.02% | 15.679s | 18.43% |
| Java | 0.866s | 1.68% | 5.822s | 37.38% |
| Scala | 0.869s | 2.03% | 6.344s | 1.49% |
| Lua | Dead | Dead | Dead | Dead |
| JavaScript | 1.806s | 36.63% | 20.997s | 6.90% |
| PHP | Dead | Dead | Dead | Dead |
| Ruby | Dead | Dead | Dead | Dead |
| Python | Dead | Dead | Dead | Dead |
| Perl | Dead | Dead | Dead | Dead |
| Bash | Dead | Dead | Dead | Dead |
| Prolog | Dead | Dead | Dead | Dead |
| Common Lisp | Dead | Dead | Dead | Dead |
| Clojure | 9.045s | 28.41% | 49.609s | 2.03% |
| F# | 1.231s | 1.64% | 11.738s | 21.34% |
| Haskell | Dead | Dead | Dead | Dead |
| Scheme | Dead | Dead | Dead | Dead |

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
