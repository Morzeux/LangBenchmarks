
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
| ActionScript3 | shell 1.4 release build cyclone |
| PHP | PHP 5.5.13 (cli) (built |  May 30 2014 10 | 43 | 29) |
| Ruby | ruby 2.0.0p451 (2014-02-24 revision 45167) [universal.x86_64-darwin13] |
| Python | Python 3.4.1 |
| Perl | This is perl 5, version 16, subversion 3 (v5.16.3) built for darwin-thread-multi-2level |
| Bash | GNU bash, version 3.2.51(1)-release (x86_64-apple-darwin13) |
| Prolog | SWI-Prolog version 6.6.6 for x86_64-darwin13.1.0 |
| Erlang | Erlang (SMP,ASYNC_THREADS,HIPE) (BEAM) emulator version 6.1 |
| Common Lisp | GNU CLISP 2.49 (2010-07-07) (built 3612292961) (memory 3612293171) |
| Clojure | Clojure 1.6.0 |
| F# | F# Compiler for F# 3.1 (Open Source Edition) |
| Haskell | The Glorious Glasgow Haskell Compilation System, version 7.6.3 |
| Scheme | MIT/GNU Scheme microcode 15.3 |

### Performance Tests

In performance tests, scripts were executed 2 times with 2 seconds timeout.
After this timeout script was killed. After executions, their times average
value were computed together with standard deviation. This values was used
to construct tables and graphs.
#### Test 1. - Discs 20, Iterations 10000000
    
| Lang | Avg. cycles | Std. cycles | Avg. hanoi | Std. hanoi |
| :-----: | :-----: | :-----: | :-----: | :-----: |
| C | 0.028s | 2.53% | 0.010s | 0.00% |
| C++ | 0.029s | 2.44% | 0.010s | 7.07% |
| Objective-C | 0.031s | 0.00% | 0.019s | 8.32% |
| C# | 0.049s | 4.08% | 0.010s | 0.00% |
| D | 0.030s | 3.33% | 0.012s | 8.33% |
| Pascal | 0.028s | 5.65% | 0.010s | 0.00% |
| Java | 0.012s | 16.67% | 0.008s | 8.84% |
| Scala | Dead | Dead | Dead | Dead |
| Lua | 1.369s | 1.86% | 0.234s | 0.68% |
| JavaScript | 0.017s | 23.53% | 0.021s | 12.14% |
| ActionScript | 0.047s | 1.50% | 0.567s | 1.15% |
| PHP | Dead | Dead | Dead | Dead |
| Ruby | 0.287s | 0.35% | 0.264s | 2.65% |
| Python | Dead | Dead | Dead | Dead |
| Perl | Dead | Dead | Dead | Dead |
| Bash | Dead | Dead | Dead | Dead |
| Prolog | 0.515s | 0.00% | 0.595s | 1.68% |
| Erlang | Dead | Dead | Dead | Dead |
| Common Lisp | Dead | Dead | Dead | Dead |
| Clojure | Dead | Dead | Dead | Dead |
| F# | 0.013s | 0.00% | 0.011s | 0.00% |
| Haskell | Dead | Dead | Dead | Dead |
| Scheme | Dead | Dead | Dead | Dead |

![Bar graph results 1](results/bar_graph1.png)

![Box graph results 1](results/log_bar_graph1.png)

#### Test 2. - Discs 25, Iterations 100000000
    
| Lang | Avg. cycles | Std. cycles | Avg. hanoi | Std. hanoi |
| :-----: | :-----: | :-----: | :-----: | :-----: |
| C | 0.290s | 0.88% | 0.322s | 2.02% |
| C++ | 0.296s | 0.34% | 0.335s | 2.24% |
| Objective-C | 0.286s | 0.35% | 0.552s | 1.18% |
| C# | 0.458s | 0.15% | 0.319s | 0.22% |
| D | 0.297s | 3.20% | 0.385s | 1.18% |
| Pascal | 0.289s | 1.04% | 0.373s | 1.88% |
| Java | 0.085s | 1.86% | 0.159s | 0.63% |
| Scala | Dead | Dead | Dead | Dead |
| Lua | Dead | Dead | Dead | Dead |
| JavaScript | 0.125s | 1.26% | 0.584s | 0.12% |
| ActionScript3 | Dead | Dead | Dead | Dead |
| PHP | Dead | Dead | Dead | Dead |
| Ruby | Dead | Dead | Dead | Dead |
| Python | Dead | Dead | Dead | Dead |
| Perl | Dead | Dead | Dead | Dead |
| Bash | Dead | Dead | Dead | Dead |
| Prolog | Dead | Dead | Dead | Dead |
| Erlang | Dead | Dead | Dead | Dead |
| Common Lisp | Dead | Dead | Dead | Dead |
| Clojure | Dead | Dead | Dead | Dead |
| F# | 0.129s | 4.65% | 0.314s | 2.71% |
| Haskell | Dead | Dead | Dead | Dead |
| Scheme | Dead | Dead | Dead | Dead |

![Bar graph results 2](results/bar_graph2.png)

![Box graph results 2](results/log_bar_graph2.png)

#### Test 3. - Discs 30, Iterations 1000000000
    
| Lang | Avg. cycles | Std. cycles | Avg. hanoi | Std. hanoi |
| :-----: | :-----: | :-----: | :-----: | :-----: |
| C | Dead | Dead | Dead | Dead |
| C++ | Dead | Dead | Dead | Dead |
| Objective-C | Dead | Dead | Dead | Dead |
| C# | Dead | Dead | Dead | Dead |
| D | Dead | Dead | Dead | Dead |
| Pascal | Dead | Dead | Dead | Dead |
| Java | Dead | Dead | Dead | Dead |
| Scala | Dead | Dead | Dead | Dead |
| Lua | Dead | Dead | Dead | Dead |
| JavaScript (node.js) | Dead | Dead | Dead | Dead |
| ActionScript3 | Dead | Dead | Dead | Dead |
| PHP | Dead | Dead | Dead | Dead |
| Ruby | Dead | Dead | Dead | Dead |
| Python | Dead | Dead | Dead | Dead |
| Perl | Dead | Dead | Dead | Dead |
| Bash | Dead | Dead | Dead | Dead |
| Prolog | Dead | Dead | Dead | Dead |
| Erlang | Dead | Dead | Dead | Dead |
| Common Lisp | Dead | Dead | Dead | Dead |
| Clojure | Dead | Dead | Dead | Dead |
| F# | Dead | Dead | Dead | Dead |
| Haskell | Dead | Dead | Dead | Dead |
| Scheme | Dead | Dead | Dead | Dead |

![Bar graph results 3](results/bar_graph3.png)

![Box graph results 3](results/log_bar_graph3.png)

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
