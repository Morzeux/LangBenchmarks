
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
| Operating System | Darwin-13.4.0-x86_64-i386-64bit |
| Processor | i386 |
| Total memory | 4.000GB |

### Compilers & Interpreters

| Language | Available Version |
| :-----: | :-----: |
| C | Apple LLVM version 6.0 (clang-600.0.54) (based on LLVM 3.5svn) |
| C++ | Apple LLVM version 6.0 (clang-600.0.54) (based on LLVM 3.5svn) |
| Objective-C | Apple LLVM version 6.0 (clang-600.0.54) (based on LLVM 3.5svn) |
| C# | Mono C# compiler version 3.4.0.0 |
| D | DMD64 D Compiler v2.065 |
| Pascal | Free Pascal Compiler version 2.6.4 [2014/02/26] for i386 |
| Java | javac 1.8.0_05 |
| Scala | Scala code runner version 2.11.1 -- Copyright 2002-2013, LAMP/EPFL |
| Lua | Lua 5.2.3  Copyright (C) 1994-2013 Lua.org, PUC-Rio |
| JavaScript (node.js) | v0.10.29 |
| ActionScript3 | shell 1.4 release build cyclone |
| PHP | PHP 5.5.13 (cli) (built |  May 30 2014 10 | 43 | 29) |
| Ruby | ruby 2.0.0p481 (2014-05-08 revision 45883) [universal.x86_64-darwin13] |
| Python | Python 3.4.1 |
| Perl | This is perl 5, version 16, subversion 3 (v5.16.3) built for darwin-thread-multi-2level |
| Bash | GNU bash, version 3.2.53(1)-release (x86_64-apple-darwin13) |
| Prolog | SWI-Prolog version 6.6.6 for x86_64-darwin13.1.0 |
| Erlang | Erlang (SMP,ASYNC_THREADS,HIPE) (BEAM) emulator version 6.1 |
| Common Lisp | GNU CLISP 2.49 (2010-07-07) (built on stefans-mac.local [192.168.240.128]) |
| Clojure | Clojure 1.6.0 |
| F# | F# Compiler for F# 3.1 (Open Source Edition) |
| Haskell | The Glorious Glasgow Haskell Compilation System, version 7.6.3 |
| Scheme | MIT/GNU Scheme microcode 15.3 |
| Swift | Swift version 1.1 (swift-600.0.54.20) |

### Performance Tests

In performance tests, scripts were executed 5 times with 120 seconds timeout.
After this timeout script was killed. After executions, their times average
value were computed together with standard deviation. This values was used
to construct tables and graphs.
#### Test 1. - Discs 15, Iterations 1000000
    
| Lang | Avg. cycles | Std. cycles | Avg. hanoi | Std. hanoi |
| :-----: | :-----: | :-----: | :-----: | :-----: |
| C | 0.002s | 0.00% | 0.000s | 0.00% |
| C++ | 0.002s | 31.62% | 0.000s | 0.00% |
| Objective-C | 0.002s | 22.36% | 0.000s | 0.00% |
| C# | 0.002s | 22.36% | 0.000s | 0.00% |
| D | 0.002s | 0.00% | 0.000s | 0.00% |
| Pascal | 0.001s | 63.25% | 0.000s | 0.00% |
| Java | 0.002s | 31.62% | 0.000s | 0.00% |
| Scala | 0.003s | 49.44% | 0.001s | 100.00% |
| Lua | 0.069s | 2.75% | 0.003s | 36.51% |
| JavaScript | 0.001s | 0.00% | 0.001s | 77.46% |
| ActionScript3 | 0.004s | 11.18% | 0.012s | 10.54% |
| PHP | 0.071s | 6.48% | 0.082s | 9.54% |
| Ruby | 0.020s | 5.00% | 0.005s | 8.94% |
| Python | 0.090s | 1.41% | 0.014s | 6.39% |
| Perl | 0.051s | 1.52% | 0.028s | 5.30% |
| Bash | 15.038s | 3.93% | 2.737s | 5.26% |
| Prolog | 0.032s | 2.42% | 0.001s | 118.32% |
| Erlang | 2.115s | 4.93% | 0.684s | 1.34% |
| Common Lisp | 0.835s | 0.74% | 0.064s | 2.32% |
| Clojure | 0.061s | 29.01% | 0.021s | 24.84% |
| F# | 0.001s | 0.00% | 0.000s | 0.00% |
| Haskell | 0.825s | 3.00% | 0.069s | 3.61% |
| Scheme | 0.406s | 5.48% | 0.042s | 7.06% |
| Swift | 0.000s | 0.00% | 0.000s | 0.00% |

![Bar graph results 1](results/bar_graph1.png)

![Box graph results 1](results/log_bar_graph1.png)

#### Test 2. - Discs 20, Iterations 10000000
    
| Lang | Avg. cycles | Std. cycles | Avg. hanoi | Std. hanoi |
| :-----: | :-----: | :-----: | :-----: | :-----: |
| C | 0.024s | 0.00% | 0.006s | 0.00% |
| C++ | 0.024s | 0.00% | 0.006s | 0.00% |
| Objective-C | 0.024s | 0.00% | 0.009s | 7.03% |
| C# | 0.025s | 4.00% | 0.008s | 0.00% |
| D | 0.023s | 2.75% | 0.008s | 0.00% |
| Pascal | 0.023s | 6.15% | 0.008s | 11.18% |
| Java | 0.005s | 0.00% | 0.004s | 0.00% |
| Scala | 0.007s | 18.07% | 0.007s | 62.92% |
| Lua | 0.692s | 3.89% | 0.116s | 3.87% |
| JavaScript | 0.005s | 12.65% | 0.013s | 6.88% |
| ActionScript3 | 0.038s | 1.18% | 0.361s | 2.33% |
| PHP | 0.668s | 7.03% | 2.439s | 0.22% |
| Ruby | 0.207s | 1.54% | 0.182s | 2.95% |
| Python | 0.885s | 0.96% | 0.457s | 0.94% |
| Perl | 0.554s | 9.40% | 0.956s | 3.37% |
| Bash | Dead | Dead | Dead | Dead |
| Prolog | 0.329s | 0.64% | 0.283s | 0.99% |
| Erlang | 20.465s | 5.11% | 22.694s | 3.28% |
| Common Lisp | 8.420s | 1.10% | 2.083s | 2.60% |
| Clojure | 0.090s | 5.67% | 0.125s | 11.62% |
| F# | 0.005s | 0.00% | 0.006s | 18.26% |
| Haskell | 8.405s | 2.85% | 2.206s | 1.50% |
| Scheme | 4.116s | 7.90% | 1.324s | 5.59% |
| Swift | 0.004s | 27.39% | 0.006s | 21.08% |

![Bar graph results 2](results/bar_graph2.png)

![Box graph results 2](results/log_bar_graph2.png)

#### Test 3. - Discs 25, Iterations 100000000
    
| Lang | Avg. cycles | Std. cycles | Avg. hanoi | Std. hanoi |
| :-----: | :-----: | :-----: | :-----: | :-----: |
| C | 0.244s | 1.10% | 0.205s | 3.58% |
| C++ | 0.242s | 1.00% | 0.196s | 0.79% |
| Objective-C | 0.243s | 1.04% | 0.314s | 1.79% |
| C# | 0.258s | 0.49% | 0.269s | 1.13% |
| D | 0.238s | 0.53% | 0.265s | 1.05% |
| Pascal | 0.236s | 0.57% | 0.281s | 0.80% |
| Java | 0.036s | 3.04% | 0.107s | 1.18% |
| Scala | 0.035s | 2.21% | 0.100s | 3.19% |
| Lua | 6.711s | 2.86% | 3.810s | 2.45% |
| JavaScript | 0.053s | 1.46% | 0.385s | 2.31% |
| ActionScript3 | 0.375s | 0.38% | 11.407s | 1.34% |
| PHP | 6.362s | 1.56% | 77.227s | 0.67% |
| Ruby | 2.097s | 3.12% | 5.732s | 2.07% |
| Python | 8.976s | 0.70% | 14.602s | 1.46% |
| Perl | 5.215s | 0.33% | 29.576s | 0.51% |
| Bash | Dead | Dead | Dead | Dead |
| Prolog | 3.355s | 2.78% | 9.337s | 1.13% |
| Erlang | Dead | Dead | Dead | Dead |
| Common Lisp | Dead | Dead | Dead | Dead |
| Clojure | 0.790s | 37.19% | 1.109s | 0.48% |
| F# | 0.051s | 2.48% | 0.175s | 0.81% |
| Haskell | Dead | Dead | Dead | Dead |
| Scheme | 38.769s | 2.21% | 39.019s | 1.21% |
| Swift | 0.039s | 4.44% | 0.162s | 2.56% |

![Bar graph results 3](results/bar_graph3.png)

![Box graph results 3](results/log_bar_graph3.png)

#### Test 4. - Discs 30, Iterations 1000000000
    
| Lang | Avg. cycles | Std. cycles | Avg. hanoi | Std. hanoi |
| :-----: | :-----: | :-----: | :-----: | :-----: |
| C | 2.514s | 1.14% | 6.694s | 3.64% |
| C++ | 2.489s | 0.50% | 6.729s | 3.28% |
| Objective-C | 2.521s | 1.31% | 10.419s | 1.74% |
| C# | 2.678s | 3.19% | 8.885s | 2.30% |
| D | 2.429s | 0.98% | 8.628s | 0.49% |
| Pascal | 2.411s | 1.20% | 9.213s | 0.94% |
| Java | 0.346s | 1.29% | 2.949s | 1.71% |
| Scala | 0.344s | 0.29% | 2.996s | 1.30% |
| Lua | Dead | Dead | Dead | Dead |
| JavaScript | 0.528s | 1.75% | 12.754s | 5.43% |
| ActionScript3 | Dead | Dead | Dead | Dead |
| PHP | Dead | Dead | Dead | Dead |
| Ruby | Dead | Dead | Dead | Dead |
| Python | Dead | Dead | Dead | Dead |
| Perl | Dead | Dead | Dead | Dead |
| Bash | Dead | Dead | Dead | Dead |
| Prolog | Dead | Dead | Dead | Dead |
| Erlang | Dead | Dead | Dead | Dead |
| Common Lisp | Dead | Dead | Dead | Dead |
| Clojure | 5.518s | 5.34% | 34.905s | 2.79% |
| F# | 0.519s | 2.76% | 5.937s | 6.86% |
| Haskell | Dead | Dead | Dead | Dead |
| Scheme | Dead | Dead | Dead | Dead |
| Swift | 0.378s | 8.15% | 5.237s | 5.02% |

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
