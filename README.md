
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
| C# | 0.004s | 15.81% | 0.000s | 0.00% |
| D | 0.002s | 22.36% | 0.000s | 0.00% |
| Pascal | 0.002s | 31.62% | 0.000s | 0.00% |
| Java | 0.004s | 11.18% | 0.001s | 44.72% |
| Scala | 0.004s | 91.52% | 0.001s | 44.72% |
| Lua | 0.146s | 7.24% | 0.008s | 13.69% |
| JavaScript | 0.001s | 77.46% | 0.003s | 94.28% |
| ActionScript3 | 0.004s | 19.36% | 0.017s | 3.72% |
| PHP | 0.164s | 6.25% | 0.125s | 3.04% |
| Ruby | 0.028s | 3.91% | 0.008s | 9.68% |
| Python | 0.134s | 5.06% | 0.026s | 14.39% |
| Perl | 0.113s | 2.91% | 0.054s | 2.62% |
| Bash | 26.610s | 4.45% | 4.356s | 4.08% |
| Prolog | 0.053s | 4.85% | 0.014s | 137.88% |
| Erlang | 5.607s | 5.94% | 1.321s | 9.91% |
| Common Lisp | 1.607s | 9.66% | 0.147s | 12.12% |
| Clojure | 0.113s | 27.57% | 0.034s | 14.53% |
| F# | 0.001s | 77.46% | 0.000s | 0.00% |
| Haskell | 1.331s | 5.62% | 0.116s | 4.48% |
| Scheme | 0.647s | 3.23% | 0.073s | 1.73% |

![Bar graph results 1](results/bar_graph1.png)

![Box graph results 1](results/log_bar_graph1.png)

#### Test 2. - Discs 20, Iterations 10000000
    
| Lang | Avg. cycles | Std. cycles | Avg. hanoi | Std. hanoi |
| :-----: | :-----: | :-----: | :-----: | :-----: |
| C | 0.037s | 38.87% | 0.011s | 14.08% |
| C++ | 0.028s | 4.23% | 0.010s | 4.47% |
| Objective-C | 0.028s | 3.57% | 0.017s | 0.00% |
| C# | 0.044s | 1.76% | 0.010s | 4.47% |
| D | 0.030s | 16.06% | 0.015s | 52.15% |
| Pascal | 0.028s | 6.78% | 0.011s | 16.26% |
| Java | 0.012s | 16.67% | 0.007s | 37.80% |
| Scala | 0.015s | 42.58% | 0.010s | 26.08% |
| Lua | 1.409s | 1.62% | 0.249s | 8.22% |
| JavaScript | 0.012s | 7.45% | 0.019s | 3.33% |
| ActionScript3 | 0.047s | 2.33% | 0.573s | 2.73% |
| PHP | 2.018s | 30.20% | 5.011s | 17.71% |
| Ruby | 0.281s | 0.69% | 0.261s | 7.10% |
| Python | 1.291s | 1.80% | 0.716s | 2.39% |
| Perl | 1.116s | 1.27% | 1.727s | 3.51% |
| Bash | Dead | Dead | Dead | Dead |
| Prolog | 0.514s | 0.46% | 0.622s | 4.67% |
| Erlang | 50.018s | 2.44% | 38.377s | 1.44% |
| Common Lisp | 13.307s | 0.44% | 3.672s | 0.56% |
| Clojure | 0.133s | 6.68% | 0.184s | 22.80% |
| F# | 0.012s | 3.73% | 0.011s | 5.75% |
| Haskell | 13.092s | 3.50% | 3.733s | 3.29% |
| Scheme | 6.160s | 2.99% | 2.315s | 1.79% |

![Bar graph results 2](results/bar_graph2.png)

![Box graph results 2](results/log_bar_graph2.png)

#### Test 3. - Discs 25, Iterations 100000000
    
| Lang | Avg. cycles | Std. cycles | Avg. hanoi | Std. hanoi |
| :-----: | :-----: | :-----: | :-----: | :-----: |
| C | 0.282s | 3.69% | 0.310s | 0.32% |
| C++ | 0.279s | 0.64% | 0.314s | 0.53% |
| Objective-C | 0.275s | 0.96% | 0.548s | 6.65% |
| C# | 0.442s | 0.20% | 0.320s | 4.50% |
| D | 0.276s | 1.40% | 0.382s | 3.73% |
| Pascal | 0.282s | 1.69% | 0.359s | 2.71% |
| Java | 0.089s | 15.17% | 0.154s | 0.50% |
| Scala | 0.084s | 1.77% | 0.199s | 4.25% |
| Lua | 13.092s | 2.22% | 7.120s | 0.88% |
| JavaScript | 0.125s | 7.93% | 0.542s | 1.38% |
| ActionScript3 | 0.447s | 0.41% | 17.199s | 0.23% |
| PHP | Dead | Dead | Dead | Dead |
| Ruby | 2.789s | 0.39% | 7.860s | 0.78% |
| Python | 12.768s | 0.24% | 22.458s | 0.27% |
| Perl | 10.985s | 0.50% | 53.007s | 1.80% |
| Bash | Dead | Dead | Dead | Dead |
| Prolog | 5.101s | 0.58% | 19.397s | 0.79% |
| Erlang | Dead | Dead | Dead | Dead |
| Common Lisp | Dead | Dead | Dead | Dead |
| Clojure | 0.864s | 10.27% | 1.582s | 0.56% |
| F# | 0.121s | 0.74% | 0.314s | 2.46% |
| Haskell | Dead | Dead | Dead | Dead |
| Scheme | Dead | Dead | Dead | Dead |

![Bar graph results 3](results/bar_graph3.png)

![Box graph results 3](results/log_bar_graph3.png)

#### Test 4. - Discs 30, Iterations 1000000000
    
| Lang | Avg. cycles | Std. cycles | Avg. hanoi | Std. hanoi |
| :-----: | :-----: | :-----: | :-----: | :-----: |
| C | 2.856s | 0.53% | 10.265s | 0.41% |
| C++ | 2.846s | 0.66% | 10.264s | 0.75% |
| Objective-C | 2.810s | 1.78% | 17.021s | 0.66% |
| C# | 4.458s | 0.31% | 10.116s | 0.22% |
| D | 2.777s | 0.99% | 12.010s | 0.43% |
| Pascal | 2.815s | 0.49% | 11.409s | 0.36% |
| Java | 0.811s | 0.23% | 4.435s | 0.18% |
| Scala | 0.816s | 2.12% | 5.933s | 0.33% |
| Lua | Dead | Dead | Dead | Dead |
| JavaScript | 1.239s | 1.62% | 18.915s | 3.60% |
| ActionScript3 | Dead | Dead | Dead | Dead |
| PHP | Dead | Dead | Dead | Dead |
| Ruby | Dead | Dead | Dead | Dead |
| Python | Dead | Dead | Dead | Dead |
| Perl | Dead | Dead | Dead | Dead |
| Bash | Dead | Dead | Dead | Dead |
| Prolog | Dead | Dead | Dead | Dead |
| Erlang | Dead | Dead | Dead | Dead |
| Common Lisp | Dead | Dead | Dead | Dead |
| Clojure | 7.135s | 5.34% | 48.583s | 2.86% |
| F# | 1.223s | 1.23% | 9.906s | 0.57% |
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
