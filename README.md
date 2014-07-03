
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
| Clojure | Clojure 1.6.0 |
| Haskell | The Glorious Glasgow Haskell Compilation System, version 7.6.3 |

### Performance Tests

In performance tests, scripts were executed 5 times with 120 seconds timeout.
After this timeout script was killed. After executions, their times average
value were computed together with standard deviation. This values was used
to construct tables and graphs.
#### Test 1. - Discs 15, Iterations 1000000
    
| Lang | Avg. cycles | Std. cycles | Avg. hanoi | Std. hanoi |
| :-----: | :-----: | :-----: | :-----: | :-----: |
| C | 0.003s | 0.00% | 0.000s | 0.00% |
| Objective-C | 0.003s | 0.00% | 0.001s | 0.00% |
| C# | 0.004s | 0.00% | 0.000s | 0.00% |
| Pascal | 0.003s | 94.28% | 0.000s | 0.00% |
| Java | 0.003s | 0.00% | 0.001s | 0.00% |
| JavaScript | 0.001s | 141.42% | 0.002s | 70.71% |
| PHP | 0.152s | 1.81% | 0.127s | 6.08% |
| Ruby | 0.030s | 22.46% | 0.009s | 36.18% |
| Python | 0.126s | 2.04% | 0.027s | 45.93% |
| Perl | 0.109s | 1.64% | 0.051s | 3.04% |
| Bash | 25.744s | 1.73% | 4.130s | 0.72% |
| Prolog | 0.053s | 11.93% | 0.006s | 67.49% |
| Common Lisp | 1.314s | 0.72% | 0.121s | 13.56% |
| Clojure | 0.058s | 30.04% | 0.023s | 15.56% |
| Haskell | 1.218s | 1.70% | 0.118s | 8.15% |

![Bar graph results 1](results/bar_graph1.png)

![Box graph results 1](results/log_bar_graph1.png)

#### Test 2. - Discs 20, Iterations 10000000
    
| Lang | Avg. cycles | Std. cycles | Avg. hanoi | Std. hanoi |
| :-----: | :-----: | :-----: | :-----: | :-----: |
| C | 0.028s | 1.60% | 0.010s | 0.00% |
| Objective-C | 0.027s | 3.70% | 0.016s | 6.25% |
| C# | 0.043s | 2.08% | 0.009s | 8.61% |
| Pascal | 0.028s | 3.19% | 0.011s | 8.13% |
| Java | 0.011s | 21.51% | 0.006s | 14.91% |
| JavaScript | 0.012s | 3.73% | 0.019s | 0.00% |
| PHP | 1.507s | 0.74% | 3.856s | 1.24% |
| Ruby | 0.278s | 3.87% | 0.255s | 3.11% |
| Python | 1.252s | 1.22% | 0.696s | 1.32% |
| Perl | 1.090s | 1.07% | 1.635s | 0.94% |
| Bash | Dead | Dead | Dead | Dead |
| Prolog | 0.511s | 2.81% | 0.586s | 0.77% |
| Common Lisp | 13.268s | 0.54% | 3.618s | 0.64% |
| Clojure | 0.132s | 4.09% | 0.177s | 13.82% |
| Haskell | 12.473s | 1.22% | 3.739s | 4.46% |

![Bar graph results 2](results/bar_graph2.png)

![Box graph results 2](results/log_bar_graph2.png)

#### Test 3. - Discs 25, Iterations 100000000
    
| Lang | Avg. cycles | Std. cycles | Avg. hanoi | Std. hanoi |
| :-----: | :-----: | :-----: | :-----: | :-----: |
| C | 0.278s | 0.82% | 0.320s | 2.77% |
| Objective-C | 0.281s | 3.36% | 0.528s | 2.63% |
| C# | 0.445s | 1.98% | 0.315s | 1.09% |
| Pascal | 0.280s | 1.11% | 0.355s | 0.98% |
| Java | 0.083s | 2.85% | 0.156s | 3.65% |
| JavaScript | 0.123s | 1.67% | 0.559s | 3.83% |
| PHP | Dead | Dead | Dead | Dead |
| Ruby | 2.758s | 0.62% | 7.668s | 0.62% |
| Python | 13.490s | 13.13% | 22.100s | 0.59% |
| Perl | 11.525s | 10.66% | 54.729s | 5.49% |
| Bash | Dead | Dead | Dead | Dead |
| Prolog | 5.033s | 0.15% | 19.026s | 1.09% |
| Common Lisp | Dead | Dead | Dead | Dead |
| Clojure | 1.294s | 72.81% | 1.577s | 1.00% |
| Haskell | Dead | Dead | Dead | Dead |

![Bar graph results 3](results/bar_graph3.png)

![Box graph results 3](results/log_bar_graph3.png)

#### Test 4. - Discs 30, Iterations 1000000000
    
| Lang | Avg. cycles | Std. cycles | Avg. hanoi | Std. hanoi |
| :-----: | :-----: | :-----: | :-----: | :-----: |
| C | 2.796s | 0.28% | 10.034s | 0.25% |
| Objective-C | 2.787s | 0.50% | 17.253s | 3.67% |
| C# | 4.470s | 1.38% | 10.059s | 0.15% |
| Pascal | 2.965s | 10.35% | 11.407s | 1.93% |
| Java | 0.807s | 0.38% | 4.407s | 0.41% |
| JavaScript | 1.496s | 33.64% | 18.131s | 1.24% |
| PHP | Dead | Dead | Dead | Dead |
| Ruby | Dead | Dead | Dead | Dead |
| Python | Dead | Dead | Dead | Dead |
| Perl | Dead | Dead | Dead | Dead |
| Bash | Dead | Dead | Dead | Dead |
| Prolog | Dead | Dead | Dead | Dead |
| Common Lisp | Dead | Dead | Dead | Dead |
| Clojure | 7.420s | 10.71% | 47.817s | 0.84% |
| Haskell | Dead | Dead | Dead | Dead |

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
