
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
| C | 0.003s | 0.00% | 0.000s | 0.00% |
| Objective-C | 0.003s | 0.00% | 0.001s | 0.00% |
| C# | 0.004s | 0.00% | 0.000s | 0.00% |
| Pascal | 0.003s | 57.14% | 0.001s | 0.00% |
| Java | 0.003s | 14.41% | 0.001s | 0.00% |
| JavaScript | 0.001s | 34.99% | 0.002s | 0.00% |
| PHP | 0.157s | 3.05% | 0.123s | 0.83% |
| Ruby | 0.028s | 3.91% | 0.008s | 0.00% |
| Python | 0.133s | 8.63% | 0.022s | 3.37% |
| Perl | 0.109s | 0.90% | 0.052s | 2.63% |
| Bash | 26.132s | 3.06% | 4.274s | 2.33% |
| Prolog | 0.055s | 10.53% | 0.006s | 40.03% |
| Common Lisp | 1.334s | 0.58% | 0.115s | 0.95% |

![Bar graph results 1](results/bar_graph1.png)

![Box graph results 1](results/box_graph1.png)

#### Test 2. - Discs 20, Iterations 10000000
    
| Lang | Avg. cycles | Std. cycles | Avg. hanoi | Std. hanoi |
| :-----: | :-----: | :-----: | :-----: | :-----: |
| C | 0.029s | 4.88% | 0.010s | 0.00% |
| Objective-C | 0.028s | 1.72% | 0.017s | 2.82% |
| C# | 0.044s | 0.00% | 0.010s | 7.34% |
| Pascal | 0.029s | 4.08% | 0.011s | 10.53% |
| Java | 0.010s | 4.71% | 0.007s | 11.00% |
| JavaScript | 0.013s | 4.87% | 0.019s | 3.90% |
| PHP | 1.556s | 4.22% | 4.056s | 1.74% |
| Ruby | 0.303s | 11.13% | 0.250s | 1.06% |
| Python | 1.290s | 1.80% | 0.710s | 2.13% |
| Perl | 1.106s | 1.09% | 1.659s | 1.83% |
| Bash | Dead | Dead | Dead | Dead |
| Prolog | 0.515s | 2.07% | 0.596s | 2.26% |
| Common Lisp | 13.800s | 4.40% | 3.768s | 2.20% |

![Bar graph results 2](results/bar_graph2.png)

![Box graph results 2](results/box_graph2.png)

#### Test 3. - Discs 25, Iterations 100000000
    
| Lang | Avg. cycles | Std. cycles | Avg. hanoi | Std. hanoi |
| :-----: | :-----: | :-----: | :-----: | :-----: |
| C | 0.286s | 3.26% | 0.318s | 1.17% |
| Objective-C | 0.289s | 2.73% | 0.575s | 4.65% |
| C# | 0.449s | 0.88% | 0.324s | 2.43% |
| Pascal | 0.285s | 1.43% | 0.361s | 2.60% |
| Java | 0.088s | 8.53% | 0.158s | 3.67% |
| JavaScript | 0.124s | 1.86% | 0.562s | 1.75% |
| PHP | Dead | Dead | Dead | Dead |
| Ruby | 2.867s | 1.24% | 8.076s | 2.41% |
| Python | 12.871s | 0.47% | 22.799s | 1.41% |
| Perl | 11.173s | 1.06% | 54.272s | 2.00% |
| Bash | Dead | Dead | Dead | Dead |
| Prolog | 5.132s | 0.45% | 19.532s | 2.41% |
| Common Lisp | Dead | Dead | Dead | Dead |

![Bar graph results 3](results/bar_graph3.png)

![Box graph results 3](results/box_graph3.png)

#### Test 4. - Discs 30, Iterations 1000000000
    
| Lang | Avg. cycles | Std. cycles | Avg. hanoi | Std. hanoi |
| :-----: | :-----: | :-----: | :-----: | :-----: |
| C | 2.853s | 0.64% | 10.540s | 5.60% |
| Objective-C | 2.868s | 0.55% | 17.418s | 0.90% |
| C# | 4.558s | 1.38% | 10.255s | 0.12% |
| Pascal | 2.894s | 1.89% | 11.476s | 0.75% |
| Java | 0.852s | 2.01% | 4.618s | 0.82% |
| JavaScript | 1.249s | 1.52% | 18.742s | 4.10% |
| PHP | Dead | Dead | Dead | Dead |
| Ruby | Dead | Dead | Dead | Dead |
| Python | Dead | Dead | Dead | Dead |
| Perl | Dead | Dead | Dead | Dead |
| Bash | Dead | Dead | Dead | Dead |
| Prolog | Dead | Dead | Dead | Dead |
| Common Lisp | Dead | Dead | Dead | Dead |

![Bar graph results 4](results/bar_graph4.png)

![Box graph results 4](results/box_graph4.png)

