
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
  * ActionScript3
  * Swift
  * Go
  * PHP
  * Ruby
  * Pypy
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

Simply clone this repository. All other instructions, packages and etc. are described in
install/install.txt file. Recommended operation system is Arch based distribution which contains
almost every required language.

## Results

Here are my results obtained on my virtual Arch Linux Machine. Arch provides rich bleeding edge
repository which is well suitable for maintaining fresh versions of languages.

### Environment

| Info |  |
| :-----: | :-----: |
| Operating System | Linux-4.5.1-1-ARCH-x86_64-with-arch |
| Processor | Intel(R) Core(TM) i5-4200M CPU @ 2.50GHz |
| Total memory | 3.864GB |

### Compilers & Interpreters

| Language | Available Version |
| :-----: | :-----: |
| C | cc (GCC) 5.3.0 |
| C++ | Copyright (C) 2015 Free Software Foundation, Inc. |
| Objective-C | Copyright (C) 2015 Free Software Foundation, Inc. |
| C# | Mono C# compiler version 4.4.0.0 |
| D | DMD64 D Compiler v2.071.0 |
| Pascal | Free Pascal Compiler version 3.0.0 [2015/11/26] for x86_64 |
| Java | javac 1.8.0_92 |
| Scala | Scala code runner version 2.11.8 -- Copyright 2002-2016, LAMP/EPFL |
| Lua | Lua 5.3.2  Copyright (C) 1994-2015 Lua.org, PUC-Rio |
| JavaScript (node.js) | v6.0.0 |
| ActionScript3 | shell 2.1 release build cyclone |
| Go | Not available |
| PHP | PHP 7.0.6 (cli) (built |  Apr 27 2016 19 | 14 | 24) ( NTS ) |
| Ruby | ruby 2.3.0p0 (2015-12-25 revision 53290) [x86_64-linux] |
| Pypy | PyPy 5.1.0 with GCC 5.3.0 |
| Python | Python 3.5.1 |
| Perl | This is perl 5, version 22, subversion 1 (v5.22.1) built for x86_64-linux-thread-multi |
| Bash | GNU bash, version 4.3.42(1)-release (x86_64-unknown-linux-gnu) |
| Prolog | SWI-Prolog version 7.2.3 for x86_64-linux |
| Erlang | Erlang (SMP,ASYNC_THREADS,HIPE) (BEAM) emulator version 7.3.1 |
| Common Lisp | GNU CLISP 2.49 (2010-07-07) (built on foutrelis) |
| Clojure | Clojure 1.7.0 |
| F# | F# Compiler for F# 4.0 (Open Source Edition) |
| Haskell | The Glorious Glasgow Haskell Compilation System, version 7.10.3 |
| Scheme | MIT/GNU Scheme microcode 15.3 |
| Swift | Swift version 3.0-dev (LLVM 752e1430fc, Clang 1e6cba3ce3, Swift 56052cfe61) |

### Performance Tests

In performance tests, scripts were executed 5 times with 120 seconds timeout.
After this timeout script was killed. After executions, their times average
value were computed together with standard deviation. This values was used
to construct tables and graphs.
#### Test 1. - Discs 20, Iterations 10000000
    
| Lang | Avg. cycles | Std. cycles | Avg. hanoi | Std. hanoi |
| :-----: | :-----: | :-----: | :-----: | :-----: |
| C | 0.023s | 3.37% | 0.008s | 0.00% |
| C++ | 0.024s | 0.00% | 0.008s | 0.00% |
| Objective-C | 0.039s | 1.62% | 0.012s | 7.45% |
| C# | 0.003s | 21.08% | 0.005s | 0.00% |
| D | 0.023s | 2.75% | 0.008s | 0.00% |
| Pascal | 0.022s | 3.52% | 0.008s | 5.59% |
| Java | 0.005s | 8.94% | 0.004s | 0.00% |
| Scala | 0.007s | 27.85% | 0.011s | 59.75% |
| Lua | 0.453s | 3.51% | 0.080s | 3.31% |
| JavaScript | 0.005s | 12.65% | 0.012s | 6.45% |
| ActionScript3 | 0.036s | 1.76% | 0.239s | 1.44% |
| PHP | 0.125s | 6.18% | 0.110s | 0.57% |
| Ruby | 0.211s | 0.56% | 0.130s | 1.85% |
| Pypy | 0.007s | 0.00% | 0.040s | 2.96% |
| Python | 0.607s | 0.29% | 0.353s | 1.04% |
| Perl | 0.477s | 3.44% | 0.691s | 0.82% |
| Bash | 69.918s | 1.12% | 36.853s | 1.27% |
| Prolog | 0.304s | 2.99% | 0.258s | 1.59% |
| Erlang | 11.822s | 0.92% | 11.830s | 0.86% |
| Common Lisp | 5.245s | 0.64% | 1.339s | 0.40% |
| Clojure | 0.081s | 9.66% | 0.087s | 18.08% |
| F# | 0.023s | 3.89% | 0.004s | 0.00% |
| Haskell | 6.584s | 1.98% | 1.738s | 6.69% |
| Scheme | 3.754s | 2.17% | 1.253s | 9.92% |
| Swift | 0.023s | 2.75% | 0.008s | 5.59% |

![Bar graph results 1](results/bar_graph1.png)

![Box graph results 1](results/log_bar_graph1.png)

#### Test 2. - Discs 25, Iterations 100000000
    
| Lang | Avg. cycles | Std. cycles | Avg. hanoi | Std. hanoi |
| :-----: | :-----: | :-----: | :-----: | :-----: |
| C | 0.237s | 3.37% | 0.258s | 2.47% |
| C++ | 0.239s | 1.39% | 0.256s | 1.61% |
| Objective-C | 0.405s | 3.02% | 0.408s | 2.75% |
| C# | 0.036s | 6.33% | 0.179s | 11.09% |
| D | 0.242s | 5.10% | 0.273s | 4.90% |
| Pascal | 0.233s | 2.05% | 0.273s | 14.57% |
| Java | 0.039s | 12.67% | 0.104s | 0.86% |
| Scala | 0.042s | 21.05% | 0.109s | 20.57% |
| Lua | 4.663s | 6.23% | 2.553s | 1.09% |
| JavaScript | 0.051s | 5.75% | 0.381s | 2.88% |
| ActionScript3 | 0.373s | 2.00% | 7.817s | 0.69% |
| PHP | 1.290s | 5.26% | 3.676s | 0.40% |
| Ruby | 2.162s | 0.57% | 4.279s | 0.48% |
| Pypy | 0.067s | 0.67% | 0.259s | 4.38% |
| Python | 6.321s | 1.06% | 11.726s | 1.10% |
| Perl | 4.874s | 2.02% | 23.449s | 3.12% |
| Bash | Dead | Dead | Dead | Dead |
| Prolog | 3.100s | 1.58% | 8.854s | 0.75% |
| Erlang | Dead | Dead | Dead | Dead |
| Common Lisp | 56.513s | 3.82% | 47.276s | 3.81% |
| Clojure | 0.516s | 4.20% | 0.834s | 10.43% |
| F# | 0.245s | 10.34% | 0.127s | 14.20% |
| Haskell | Dead | Dead | Dead | Dead |
| Scheme | 38.110s | 1.83% | 39.408s | 5.48% |
| Swift | 0.242s | 9.39% | 0.295s | 9.10% |

![Bar graph results 2](results/bar_graph2.png)

![Box graph results 2](results/log_bar_graph2.png)

#### Test 3. - Discs 30, Iterations 1000000000
    
| Lang | Avg. cycles | Std. cycles | Avg. hanoi | Std. hanoi |
| :-----: | :-----: | :-----: | :-----: | :-----: |
| C | 2.417s | 0.43% | 8.515s | 0.58% |
| C++ | 2.470s | 0.89% | 8.346s | 1.01% |
| Objective-C | 4.047s | 0.32% | 13.642s | 1.37% |
| C# | 0.363s | 7.05% | 5.922s | 3.16% |
| D | 2.451s | 0.37% | 8.623s | 0.87% |
| Pascal | 2.423s | 1.84% | 8.302s | 2.97% |
| Java | 0.368s | 3.51% | 3.116s | 4.42% |
| Scala | 0.386s | 7.60% | 3.115s | 4.79% |
| Lua | Dead | Dead | Dead | Dead |
| JavaScript | 0.529s | 2.47% | 12.686s | 1.19% |
| ActionScript3 | Dead | Dead | Dead | Dead |
| PHP | Dead | Dead | Dead | Dead |
| Ruby | Dead | Dead | Dead | Dead |
| Pypy | 0.699s | 2.63% | 17.428s | 8.40% |
| Python | Dead | Dead | Dead | Dead |
| Perl | Dead | Dead | Dead | Dead |
| Bash | Dead | Dead | Dead | Dead |
| Prolog | Dead | Dead | Dead | Dead |
| Erlang | Dead | Dead | Dead | Dead |
| Common Lisp | Dead | Dead | Dead | Dead |
| Clojure | 3.684s | 37.55% | 31.387s | 42.02% |
| F# | 2.405s | 1.34% | 3.992s | 3.41% |
| Haskell | Dead | Dead | Dead | Dead |
| Scheme | Dead | Dead | Dead | Dead |
| Swift | 2.384s | 1.09% | 9.159s | 2.48% |

![Bar graph results 3](results/bar_graph3.png)

![Box graph results 3](results/log_bar_graph3.png)

#### Test 4. - Discs 32, Iterations 2147483647
    
| Lang | Avg. cycles | Std. cycles | Avg. hanoi | Std. hanoi |
| :-----: | :-----: | :-----: | :-----: | :-----: |
| C | 5.162s | 1.80% | 33.340s | 1.25% |
| C++ | 5.264s | 1.77% | 33.666s | 2.30% |
| Objective-C | 8.634s | 0.25% | 52.900s | 0.45% |
| C# | 0.723s | 1.63% | 22.250s | 0.47% |
| D | 5.191s | 0.13% | 33.853s | 0.35% |
| Pascal | 5.096s | 0.41% | 32.315s | 0.45% |
| Java | 0.804s | 6.80% | 11.835s | 1.14% |
| Scala | 0.755s | 2.12% | 11.678s | 1.05% |
| Lua | Dead | Dead | Dead | Dead |
| JavaScript | 1.184s | 14.48% | 50.665s | 3.86% |
| ActionScript3 | Dead | Dead | Dead | Dead |
| PHP | Dead | Dead | Dead | Dead |
| Ruby | Dead | Dead | Dead | Dead |
| Pypy | 1.501s | 3.38% | 52.912s | 1.63% |
| Python | Dead | Dead | Dead | Dead |
| Perl | Dead | Dead | Dead | Dead |
| Bash | Dead | Dead | Dead | Dead |
| Prolog | Dead | Dead | Dead | Dead |
| Erlang | Dead | Dead | Dead | Dead |
| Common Lisp | Dead | Dead | Dead | Dead |
| Clojure | Dead | Dead | Dead | Dead |
| F# | 5.200s | 0.73% | 15.846s | 1.49% |
| Haskell | Dead | Dead | Dead | Dead |
| Scheme | Dead | Dead | Dead | Dead |
| Swift | 5.366s | 4.06% | 43.269s | 12.13% |

![Bar graph results 4](results/bar_graph4.png)

![Box graph results 4](results/log_bar_graph4.png)

## License
```
Programming Languages Benchmark Script.
Copyright (C) 2014-2016 Stefan Smihla

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
