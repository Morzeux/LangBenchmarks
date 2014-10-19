
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
LangBenchamrk script is written in Python 3.4.x and there is dependency for
third-party pygal modul. This is need only to generate README.md file.

## Results

Here are my results obtained on my Apple Machine. Reason I used Apple was
environment, where I could use together C# (through Mono), Objective-C,
Bash and where I would use Swift in future.

### Environment

| Info |  |
| :-----: | :-----: |
| Operating System | Darwin-13.2.0-x86_64-i386-64bit |
| Processor | i386 |
| Total memory | 4.000GB |

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
| Common Lisp | GNU CLISP 2.49 (2010-07-07) (built on stefans-mac.local [192.168.240.128]) |
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
| C | 0.002s | 38.73% | 0.000s | 0.00% |
| C++ | 0.002s | 22.36% | 0.000s | 0.00% |
| Objective-C | 0.002s | 22.36% | 0.000s | 0.00% |
| C# | 0.002s | 0.00% | 0.000s | 0.00% |
| D | 0.003s | 68.31% | 0.000s | 0.00% |
| Pascal | 0.001s | 77.46% | 0.000s | 0.00% |
| Java | 0.002s | 38.73% | 0.000s | 0.00% |
| Scala | 0.004s | 41.83% | 0.002s | 63.25% |
| Lua | 0.068s | 4.83% | 0.003s | 25.82% |
| JavaScript | 0.001s | 0.00% | 0.001s | 63.25% |
| ActionScript3 | 0.004s | 33.54% | 0.012s | 9.86% |
| PHP | 0.081s | 15.42% | 0.087s | 5.34% |
| Ruby | 0.023s | 16.73% | 0.005s | 17.89% |
| Python | 0.092s | 1.82% | 0.015s | 2.98% |
| Perl | 0.058s | 3.86% | 0.032s | 5.59% |
| Bash | 18.054s | 8.86% | 3.054s | 6.27% |
| Prolog | 0.036s | 6.92% | 0.002s | 124.50% |
| Erlang | 2.179s | 2.74% | 0.726s | 1.57% |
| Common Lisp | 0.866s | 0.65% | 0.067s | 4.11% |
| Clojure | 0.059s | 42.61% | 0.027s | 17.29% |
| F# | 0.001s | 0.00% | 0.000s | 0.00% |
| Haskell | 0.846s | 6.23% | 0.069s | 4.15% |
| Scheme | 0.412s | 5.69% | 0.042s | 6.30% |

![Bar graph results 1](results/bar_graph1.png)

![Box graph results 1](results/log_bar_graph1.png)

#### Test 2. - Discs 20, Iterations 10000000
    
| Lang | Avg. cycles | Std. cycles | Avg. hanoi | Std. hanoi |
| :-----: | :-----: | :-----: | :-----: | :-----: |
| C | 0.024s | 3.23% | 0.006s | 10.54% |
| C++ | 0.024s | 3.23% | 0.006s | 0.00% |
| Objective-C | 0.024s | 3.23% | 0.010s | 0.00% |
| C# | 0.027s | 7.22% | 0.008s | 0.00% |
| D | 0.024s | 0.00% | 0.008s | 0.00% |
| Pascal | 0.023s | 3.89% | 0.008s | 9.68% |
| Java | 0.005s | 8.94% | 0.004s | 22.36% |
| Scala | 0.006s | 19.72% | 0.006s | 27.89% |
| Lua | 0.711s | 4.70% | 0.117s | 2.48% |
| JavaScript | 0.005s | 15.49% | 0.013s | 7.69% |
| ActionScript3 | 0.039s | 3.80% | 0.372s | 4.92% |
| PHP | 0.680s | 2.80% | 2.609s | 5.17% |
| Ruby | 0.213s | 1.51% | 0.182s | 4.41% |
| Python | 0.916s | 0.88% | 0.475s | 0.94% |
| Perl | 0.536s | 1.46% | 0.970s | 0.62% |
| Bash | Dead | Dead | Dead | Dead |
| Prolog | 0.356s | 2.15% | 0.303s | 4.08% |
| Erlang | 21.695s | 5.25% | 24.125s | 4.87% |
| Common Lisp | 8.775s | 1.01% | 2.164s | 0.73% |
| Clojure | 0.115s | 40.04% | 0.129s | 22.60% |
| F# | 0.006s | 32.49% | 0.005s | 8.94% |
| Haskell | 8.270s | 1.03% | 2.240s | 4.23% |
| Scheme | 4.201s | 4.44% | 2.723s | 96.49% |

![Bar graph results 2](results/bar_graph2.png)

![Box graph results 2](results/log_bar_graph2.png)

#### Test 3. - Discs 25, Iterations 100000000
    
| Lang | Avg. cycles | Std. cycles | Avg. hanoi | Std. hanoi |
| :-----: | :-----: | :-----: | :-----: | :-----: |
| C | 0.247s | 1.88% | 0.211s | 11.09% |
| C++ | 0.248s | 2.06% | 0.204s | 5.04% |
| Objective-C | 0.253s | 3.49% | 0.323s | 1.65% |
| C# | 0.264s | 2.03% | 0.278s | 2.83% |
| D | 0.246s | 3.69% | 0.270s | 1.45% |
| Pascal | 0.241s | 1.54% | 0.284s | 1.54% |
| Java | 0.037s | 5.27% | 0.108s | 0.59% |
| Scala | 0.038s | 8.81% | 0.113s | 10.06% |
| Lua | 6.828s | 3.39% | 3.812s | 2.37% |
| JavaScript | 0.072s | 29.63% | 0.392s | 3.06% |
| ActionScript3 | 0.381s | 0.98% | 11.767s | 1.19% |
| PHP | 6.860s | 2.49% | 83.065s | 1.48% |
| Ruby | 2.159s | 0.52% | 5.863s | 2.39% |
| Python | 9.722s | 4.39% | 15.699s | 2.10% |
| Perl | 5.680s | 2.34% | 32.973s | 2.56% |
| Bash | Dead | Dead | Dead | Dead |
| Prolog | 3.621s | 4.22% | 10.231s | 1.08% |
| Erlang | Dead | Dead | Dead | Dead |
| Common Lisp | Dead | Dead | Dead | Dead |
| Clojure | 17.908s | 163.57% | 1.228s | 4.55% |
| F# | 0.060s | 9.01% | 0.185s | 3.16% |
| Haskell | Dead | Dead | Dead | Dead |
| Scheme | 39.938s | 0.53% | 41.735s | 1.61% |

![Bar graph results 3](results/bar_graph3.png)

![Box graph results 3](results/log_bar_graph3.png)

#### Test 4. - Discs 30, Iterations 1000000000
    
| Lang | Avg. cycles | Std. cycles | Avg. hanoi | Std. hanoi |
| :-----: | :-----: | :-----: | :-----: | :-----: |
| C | 2.503s | 0.52% | 6.693s | 1.75% |
| C++ | 2.545s | 3.90% | 6.993s | 12.45% |
| Objective-C | 2.554s | 4.41% | 10.515s | 1.28% |
| C# | 2.708s | 2.70% | 8.995s | 1.15% |
| D | 2.543s | 5.48% | 9.108s | 4.17% |
| Pascal | 2.469s | 1.99% | 9.500s | 3.63% |
| Java | 0.358s | 1.36% | 3.039s | 0.25% |
| Scala | 0.363s | 3.45% | 3.114s | 2.04% |
| Lua | Dead | Dead | Dead | Dead |
| JavaScript | 0.545s | 2.04% | 12.983s | 3.18% |
| ActionScript3 | Dead | Dead | Dead | Dead |
| PHP | Dead | Dead | Dead | Dead |
| Ruby | Dead | Dead | Dead | Dead |
| Python | Dead | Dead | Dead | Dead |
| Perl | Dead | Dead | Dead | Dead |
| Bash | Dead | Dead | Dead | Dead |
| Prolog | Dead | Dead | Dead | Dead |
| Erlang | Dead | Dead | Dead | Dead |
| Common Lisp | Dead | Dead | Dead | Dead |
| Clojure | 9.506s | 83.35% | 36.818s | 1.29% |
| F# | 0.539s | 1.74% | 5.990s | 0.87% |
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
