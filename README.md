
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
| Operating System | Linux-4.5.4-1-ARCH-x86_64-with-arch |
| Processor | Intel(R) Core(TM) i5-4200M CPU @ 2.50GHz |
| Total memory | 3.864GB |

### Compilers & Interpreters

| Language | Available Version |
| :-----: | :-----: |
| C | cc (GCC) 6.1.1 20160501 |
| C++ | Copyright (C) 2016 Free Software Foundation, Inc. |
| Objective-C | Copyright (C) 2016 Free Software Foundation, Inc. |
| C# | Mono C# compiler version 4.4.0.0 |
| D | DMD64 D Compiler v2.071.0 |
| Pascal | Free Pascal Compiler version 3.0.0 [2015/11/26] for x86_64 |
| Java | javac 1.8.0_92 |
| Scala | Scala code runner version 2.11.8 -- Copyright 2002-2016, LAMP/EPFL |
| Lua | Lua 5.3.2  Copyright (C) 1994-2015 Lua.org, PUC-Rio |
| JavaScript (node.js) | v6.2.1 |
| ActionScript3 | shell 2.1 release build cyclone |
| Go | go version go1.6.2 linux/amd64 |
| PHP | PHP 7.0.7 (cli) (built |  May 25 2016 18 | 40 | 26) ( NTS ) |
| Ruby | ruby 2.3.1p112 (2016-04-26 revision 54768) [x86_64-linux] |
| Pypy | PyPy 5.1.1 with GCC 6.1.1 20160501 |
| Python | Python 3.5.1 |
| Perl | This is perl 5, version 22, subversion 2 (v5.22.2) built for x86_64-linux-thread-multi |
| Bash | GNU bash, version 4.3.42(1)-release (x86_64-unknown-linux-gnu) |
| Prolog | SWI-Prolog version 7.2.3 for x86_64-linux |
| Erlang | Erlang (SMP,ASYNC_THREADS,HIPE) (BEAM) emulator version 7.3.1 |
| Common Lisp | GNU CLISP 2.49 (2010-07-07) (built on foutrelis) |
| Clojure | Clojure 1.7.0 |
| F# | F# Compiler for F# 4.0 (Open Source Edition) |
| Haskell | The Glorious Glasgow Haskell Compilation System, version 7.10.3 |
| Scheme | MIT/GNU Scheme microcode 15.3 |
| Swift | Swift version 3.0-dev (LLVM 8fcf602916, Clang cf0a734990, Swift 000d413a62) |

### Performance Tests

In performance tests, scripts were executed 5 times with 120 seconds timeout.
After this timeout script was killed. After executions, their times average
value were computed together with standard deviation. This values was used
to construct tables and graphs.
#### Test 1. - Discs 20, Iterations 10000000
    
| Lang | Avg. cycles | Std. cycles | Avg. hanoi | Std. hanoi |
| :-----: | :-----: | :-----: | :-----: | :-----: |
| C# | 0.003s | 33.33% | 0.005s | 0.00% |
| Java | 0.005s | 12.65% | 0.003s | 29.81% |
| Go | 0.003s | 33.33% | 0.006s | 14.91% |
| Scala | 0.009s | 69.39% | 0.008s | 30.62% |
| JavaScript | 0.005s | 17.89% | 0.012s | 9.13% |
| F# | 0.023s | 3.89% | 0.004s | 0.00% |
| Pascal | 0.022s | 4.98% | 0.007s | 12.78% |
| D | 0.023s | 0.00% | 0.007s | 11.07% |
| C | 0.023s | 2.75% | 0.008s | 0.00% |
| C++ | 0.024s | 1.86% | 0.008s | 0.00% |
| Swift | 0.024s | 9.86% | 0.008s | 7.91% |
| Objective-C | 0.039s | 1.62% | 0.012s | 6.45% |
| Pypy | 0.007s | 12.78% | 0.051s | 15.16% |
| Clojure | 0.069s | 7.19% | 0.079s | 14.31% |
| PHP | 0.137s | 13.15% | 0.123s | 3.65% |
| ActionScript3 | 0.041s | 6.07% | 0.298s | 12.80% |
| Ruby | 0.215s | 0.88% | 0.140s | 7.78% |
| Lua | 0.468s | 5.45% | 0.082s | 3.45% |
| Prolog | 0.301s | 0.83% | 0.258s | 1.52% |
| Python | 0.738s | 12.98% | 0.452s | 12.97% |
| Perl | 0.516s | 5.16% | 0.824s | 7.07% |
| Scheme | 3.567s | 0.78% | 1.121s | 0.39% |
| Common Lisp | 5.090s | 0.37% | 1.303s | 0.56% |
| Haskell | 6.274s | 2.19% | 1.611s | 1.79% |
| Erlang | 11.336s | 0.59% | 11.102s | 0.25% |
| Bash | 71.177s | 3.85% | 36.944s | 3.22% |

![Bar graph results 1](results/bar_graph1.png)

![Box graph results 1](results/log_bar_graph1.png)

#### Test 2. - Discs 25, Iterations 100000000
    
| Lang | Avg. cycles | Std. cycles | Avg. hanoi | Std. hanoi |
| :-----: | :-----: | :-----: | :-----: | :-----: |
| Scala | 0.037s | 3.20% | 0.097s | 5.98% |
| Java | 0.041s | 6.17% | 0.105s | 0.95% |
| Go | 0.034s | 2.28% | 0.167s | 0.54% |
| C# | 0.035s | 6.52% | 0.168s | 1.16% |
| Pypy | 0.066s | 0.68% | 0.246s | 2.49% |
| F# | 0.255s | 6.51% | 0.131s | 7.98% |
| JavaScript | 0.050s | 3.69% | 0.379s | 0.50% |
| Pascal | 0.230s | 0.39% | 0.242s | 0.67% |
| C | 0.232s | 0.55% | 0.250s | 0.62% |
| C++ | 0.238s | 1.11% | 0.250s | 0.59% |
| D | 0.234s | 0.38% | 0.259s | 0.42% |
| Swift | 0.241s | 5.37% | 0.279s | 6.19% |
| Objective-C | 0.393s | 0.23% | 0.401s | 0.88% |
| Clojure | 0.339s | 35.63% | 0.779s | 33.08% |
| PHP | 1.216s | 0.65% | 3.696s | 1.28% |
| Ruby | 2.125s | 0.45% | 4.193s | 0.74% |
| Lua | 4.437s | 4.33% | 2.476s | 2.37% |
| ActionScript3 | 0.366s | 0.73% | 7.679s | 1.55% |
| Prolog | 3.051s | 1.61% | 8.607s | 0.31% |
| Python | 6.182s | 0.75% | 11.394s | 1.16% |
| Perl | 4.602s | 0.61% | 22.569s | 0.33% |
| Scheme | 38.516s | 3.59% | 38.337s | 1.28% |
| Common Lisp | 53.757s | 1.88% | 43.513s | 1.92% |
| Bash | Dead | Dead | Dead | Dead |
| Erlang | Dead | Dead | Dead | Dead |
| Haskell | Dead | Dead | Dead | Dead |

![Bar graph results 2](results/bar_graph2.png)

![Box graph results 2](results/log_bar_graph2.png)

#### Test 3. - Discs 30, Iterations 1000000000
    
| Lang | Avg. cycles | Std. cycles | Avg. hanoi | Std. hanoi |
| :-----: | :-----: | :-----: | :-----: | :-----: |
| Scala | 0.455s | 17.25% | 4.290s | 18.25% |
| Java | 0.490s | 10.01% | 4.689s | 15.53% |
| C# | 0.334s | 3.06% | 5.776s | 6.83% |
| Go | 0.357s | 1.46% | 5.958s | 0.70% |
| F# | 2.634s | 3.76% | 4.459s | 4.78% |
| Pascal | 2.352s | 2.39% | 8.204s | 5.01% |
| C | 2.377s | 2.64% | 8.473s | 4.10% |
| C++ | 2.432s | 1.87% | 8.472s | 4.12% |
| D | 2.427s | 2.24% | 8.600s | 2.32% |
| Swift | 2.428s | 1.29% | 9.850s | 5.16% |
| JavaScript | 0.546s | 1.75% | 13.225s | 1.33% |
| Objective-C | 4.018s | 2.34% | 13.214s | 2.65% |
| Pypy | 0.698s | 2.69% | 18.794s | 10.12% |
| Clojure | 4.410s | 39.09% | 30.696s | 24.79% |
| Lua | Dead | Dead | Dead | Dead |
| ActionScript3 | Dead | Dead | Dead | Dead |
| PHP | Dead | Dead | Dead | Dead |
| Ruby | Dead | Dead | Dead | Dead |
| Python | Dead | Dead | Dead | Dead |
| Perl | Dead | Dead | Dead | Dead |
| Bash | Dead | Dead | Dead | Dead |
| Prolog | Dead | Dead | Dead | Dead |
| Erlang | Dead | Dead | Dead | Dead |
| Common Lisp | Dead | Dead | Dead | Dead |
| Haskell | Dead | Dead | Dead | Dead |
| Scheme | Dead | Dead | Dead | Dead |

![Bar graph results 3](results/bar_graph3.png)

![Box graph results 3](results/log_bar_graph3.png)

#### Test 4. - Discs 32, Iterations 2147483647
    
| Lang | Avg. cycles | Std. cycles | Avg. hanoi | Std. hanoi |
| :-----: | :-----: | :-----: | :-----: | :-----: |
| Scala | 0.783s | 4.30% | 13.863s | 9.66% |
| Java | 0.834s | 2.59% | 14.179s | 3.56% |
| F# | 5.206s | 2.53% | 16.583s | 5.85% |
| C# | 0.710s | 0.44% | 21.859s | 3.22% |
| Go | 0.761s | 3.68% | 24.921s | 2.65% |
| C++ | 5.346s | 0.87% | 35.498s | 2.65% |
| D | 5.400s | 1.64% | 35.456s | 3.64% |
| Pascal | 5.329s | 1.03% | 36.235s | 2.40% |
| C | 5.275s | 0.82% | 36.312s | 2.69% |
| Swift | 5.177s | 4.57% | 37.737s | 4.17% |
| JavaScript | 1.203s | 6.14% | 55.168s | 5.43% |
| Pypy | 1.484s | 5.09% | 62.439s | 12.42% |
| Objective-C | 8.734s | 0.66% | 58.495s | 2.22% |
| Lua | Dead | Dead | Dead | Dead |
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
| Haskell | Dead | Dead | Dead | Dead |
| Scheme | Dead | Dead | Dead | Dead |

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
