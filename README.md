
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
| Operating System | Linux-4.3.3-2-ARCH-x86_64-with-arch |
| Processor | Intel(R) Core(TM) i5-4200M CPU @ 2.50GHz |
| Total memory | 3.864GB |

### Compilers & Interpreters

| Language | Available Version |
| :-----: | :-----: |
| C | cc (GCC) 5.3.0 |
| C++ | Copyright (C) 2015 Free Software Foundation, Inc. |
| Objective-C | Copyright (C) 2015 Free Software Foundation, Inc. |
| C# | Mono C# compiler version 4.2.2.0 |
| D | DMD64 D Compiler v2.069 |
| Pascal | Free Pascal Compiler version 3.0.0 [2015/11/26] for x86_64 |
| Java | javac 1.8.0_66 |
| Scala | Scala code runner version 2.11.7 -- Copyright 2002-2013, LAMP/EPFL |
| Lua | Lua 5.3.2  Copyright (C) 1994-2015 Lua.org, PUC-Rio |
| JavaScript (node.js) | v5.3.0 |
| ActionScript3 | shell 2.1 release build cyclone |
| Go | go version go1.5.2 linux/amd64 |
| PHP | PHP 7.0.1 (cli) (built |  Jan  3 2016 09 | 05 | 41) ( NTS ) |
| Ruby | ruby 2.3.0p0 (2015-12-25 revision 53290) [x86_64-linux] |
| Python | Python 3.5.1 |
| Perl | This is perl 5, version 22, subversion 1 (v5.22.1) built for x86_64-linux-thread-multi |
| Bash | GNU bash, version 4.3.42(1)-release (x86_64-unknown-linux-gnu) |
| Prolog | SWI-Prolog version 7.2.3 for x86_64-linux |
| Erlang | Erlang (SMP,ASYNC_THREADS,HIPE) (BEAM) emulator version 7.2.1 |
| Common Lisp | GNU CLISP 2.49 (2010-07-07) (built on foutrelis) |
| Clojure | Clojure 1.7.0 |
| F# | F# Compiler for F# 4.0 (Open Source Edition) |
| Haskell | The Glorious Glasgow Haskell Compilation System, version 7.10.3 |
| Scheme | MIT/GNU Scheme microcode 15.3 |
| Swift | Swift version 2.2-dev (LLVM 3ebdbb2c7e, Clang f66c5bb67b, Swift 1f2908b4f7) |

### Performance Tests

In performance tests, scripts were executed 5 times with 120 seconds timeout.
After this timeout script was killed. After executions, their times average
value were computed together with standard deviation. This values was used
to construct tables and graphs.
#### Test 1. - Discs 20, Iterations 10000000
    
| Lang | Avg. cycles | Std. cycles | Avg. hanoi | Std. hanoi |
| :-----: | :-----: | :-----: | :-----: | :-----: |
| C | 0.024s | 4.93% | 0.008s | 9.68% |
| C++ | 0.026s | 2.43% | 0.008s | 7.91% |
| Objective-C | 0.045s | 16.81% | 0.013s | 12.40% |
| C# | 0.003s | 33.33% | 0.006s | 29.81% |
| D | 0.030s | 20.17% | 0.009s | 23.83% |
| Pascal | 0.029s | 22.35% | 0.010s | 37.95% |
| Java | 0.007s | 18.07% | 0.004s | 19.36% |
| Scala | 0.010s | 38.21% | 0.007s | 55.33% |
| Lua | 0.454s | 3.65% | 0.085s | 8.39% |
| JavaScript | 0.006s | 0.00% | 0.011s | 12.86% |
| ActionScript3 | 0.038s | 8.40% | 0.271s | 6.97% |
| Go | 0.004s | 25.00% | 0.005s | 12.65% |
| PHP | 0.132s | 4.72% | 0.134s | 11.71% |
| Ruby | 0.229s | 5.53% | 0.141s | 4.99% |
| Python | 0.647s | 1.25% | 0.376s | 4.41% |
| Perl | 0.489s | 4.12% | 0.761s | 3.25% |
| Bash | 72.836s | 2.29% | 37.862s | 3.57% |
| Prolog | 0.322s | 2.76% | 0.265s | 5.43% |
| Erlang | 12.037s | 3.98% | 11.865s | 4.17% |
| Common Lisp | 5.611s | 7.35% | 1.406s | 5.51% |
| Clojure | 0.087s | 16.55% | 0.131s | 55.10% |
| F# | 0.018s | 10.83% | 0.004s | 11.18% |
| Haskell | 6.383s | 4.55% | 1.635s | 4.03% |
| Scheme | 3.690s | 2.92% | 1.193s | 3.97% |
| Swift | 0.023s | 2.75% | 0.011s | 43.79% |

![Bar graph results 1](results/bar_graph1.png)

![Box graph results 1](results/log_bar_graph1.png)

#### Test 2. - Discs 25, Iterations 100000000
    
| Lang | Avg. cycles | Std. cycles | Avg. hanoi | Std. hanoi |
| :-----: | :-----: | :-----: | :-----: | :-----: |
| C | 0.239s | 4.79% | 0.257s | 1.98% |
| C++ | 0.241s | 1.95% | 0.266s | 6.20% |
| Objective-C | 0.411s | 2.30% | 0.454s | 10.45% |
| C# | 0.036s | 22.64% | 0.174s | 3.94% |
| D | 0.240s | 1.82% | 0.270s | 4.27% |
| Pascal | 0.238s | 4.04% | 0.252s | 2.45% |
| Java | 0.040s | 9.29% | 0.120s | 13.99% |
| Scala | 0.044s | 15.94% | 0.110s | 20.85% |
| Lua | 4.649s | 8.00% | 2.624s | 3.86% |
| JavaScript | 0.051s | 3.40% | 0.382s | 5.70% |
| ActionScript3 | 0.366s | 0.91% | 7.720s | 2.45% |
| Go | 0.053s | 23.79% | 0.183s | 12.65% |
| PHP | 1.251s | 3.63% | 3.808s | 1.72% |
| Ruby | 2.138s | 1.24% | 4.202s | 1.24% |
| Python | 6.323s | 1.61% | 11.387s | 1.03% |
| Perl | 4.753s | 4.07% | 22.862s | 3.12% |
| Bash | Dead | Dead | Dead | Dead |
| Prolog | 3.044s | 0.59% | 8.935s | 3.38% |
| Erlang | Dead | Dead | Dead | Dead |
| Common Lisp | 53.490s | 1.71% | 44.645s | 1.69% |
| Clojure | 0.431s | 8.12% | 0.866s | 3.68% |
| F# | 0.186s | 9.56% | 0.134s | 2.93% |
| Haskell | 64.793s | 1.74% | 52.502s | 1.95% |
| Scheme | 38.933s | 3.48% | 38.758s | 3.54% |
| Swift | 0.249s | 3.08% | 0.335s | 5.92% |

![Bar graph results 2](results/bar_graph2.png)

![Box graph results 2](results/log_bar_graph2.png)

#### Test 3. - Discs 30, Iterations 1000000000
    
| Lang | Avg. cycles | Std. cycles | Avg. hanoi | Std. hanoi |
| :-----: | :-----: | :-----: | :-----: | :-----: |
| C | 2.430s | 1.67% | 8.885s | 8.54% |
| C++ | 2.437s | 1.38% | 8.160s | 1.94% |
| Objective-C | 4.044s | 0.93% | 12.784s | 0.30% |
| C# | 0.336s | 1.23% | 5.381s | 0.21% |
| D | 2.378s | 0.33% | 8.238s | 0.29% |
| Pascal | 2.330s | 0.36% | 7.827s | 0.48% |
| Java | 0.380s | 2.78% | 2.834s | 0.55% |
| Scala | 0.361s | 3.31% | 2.834s | 0.25% |
| Lua | Dead | Dead | Dead | Dead |
| JavaScript | 0.515s | 4.41% | 11.559s | 2.20% |
| ActionScript3 | Dead | Dead | Dead | Dead |
| Go | 0.340s | 1.01% | 5.377s | 0.51% |
| PHP | Dead | Dead | Dead | Dead |
| Ruby | Dead | Dead | Dead | Dead |
| Python | Dead | Dead | Dead | Dead |
| Perl | Dead | Dead | Dead | Dead |
| Bash | Dead | Dead | Dead | Dead |
| Prolog | Dead | Dead | Dead | Dead |
| Erlang | Dead | Dead | Dead | Dead |
| Common Lisp | Dead | Dead | Dead | Dead |
| Clojure | 3.262s | 2.89% | 23.814s | 0.17% |
| F# | 1.673s | 1.18% | 4.095s | 0.80% |
| Haskell | Dead | Dead | Dead | Dead |
| Scheme | Dead | Dead | Dead | Dead |
| Swift | 2.304s | 1.00% | 9.007s | 2.71% |

![Bar graph results 3](results/bar_graph3.png)

![Box graph results 3](results/log_bar_graph3.png)

#### Test 4. - Discs 32, Iterations 2147483647
    
| Lang | Avg. cycles | Std. cycles | Avg. hanoi | Std. hanoi |
| :-----: | :-----: | :-----: | :-----: | :-----: |
| C | 5.078s | 1.22% | 32.479s | 1.09% |
| C++ | 5.195s | 0.52% | 32.315s | 1.29% |
| Objective-C | 8.688s | 0.82% | 51.293s | 1.10% |
| C# | 0.721s | 0.27% | 21.465s | 0.28% |
| D | 5.151s | 0.69% | 33.628s | 1.62% |
| Pascal | 5.156s | 2.82% | 37.427s | 11.52% |
| Java | 0.784s | 2.07% | 12.051s | 7.59% |
| Scala | 0.773s | 5.35% | 11.656s | 2.33% |
| Lua | Dead | Dead | Dead | Dead |
| JavaScript | 1.071s | 0.44% | 44.779s | 1.84% |
| ActionScript3 | Dead | Dead | Dead | Dead |
| Go | 0.725s | 0.54% | 21.406s | 0.11% |
| PHP | Dead | Dead | Dead | Dead |
| Ruby | Dead | Dead | Dead | Dead |
| Python | Dead | Dead | Dead | Dead |
| Perl | Dead | Dead | Dead | Dead |
| Bash | Dead | Dead | Dead | Dead |
| Prolog | Dead | Dead | Dead | Dead |
| Erlang | Dead | Dead | Dead | Dead |
| Common Lisp | Dead | Dead | Dead | Dead |
| Clojure | 7.294s | 8.47% | 95.625s | 0.71% |
| F# | 3.628s | 2.06% | 17.016s | 1.84% |
| Haskell | Dead | Dead | Dead | Dead |
| Scheme | Dead | Dead | Dead | Dead |
| Swift | 4.997s | 2.00% | 36.955s | 3.49% |

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
