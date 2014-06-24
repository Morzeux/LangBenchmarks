
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
        i += 1;
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
| Operating System | Windows-7-6.1.7601-SP1 |
| Processor | Intel64 Family 6 Model 37 Stepping 5, GenuineIntel |
| Total memory | 3.866GB |

### Compilers & Interpreters

| Language | Available Version |
| :-----: | :-----: |
| C | gcc.exe (GCC) 4.8.1 |
| Objective-C | Not available |
| C# | Not available |
| Pascal | Free Pascal Compiler version 2.6.4 [2014/03/06] for i386 |
| Java | javac 1.8.0_05 |
| JavaScript (node.js) | Not available |
| PHP | Not available |
| Ruby | ruby 2.0.0p451 (2014-02-24) [i386-mingw32] |
| Python | Not available |
| Perl | Not available |
| Bash | Not available |
| Prolog | Not available |
| Common Lisp | Not available |

### Performance Tests

In performance tests, scripts were executed 5 times with 1 seconds timeout.
After this timeout script was killed. After executions, their times average
value were computed together with standard deviation. This values was used
to construct tables and graphs.
#### Test 1. - Discs 15, Iterations 100000
    
| Lang | Avg. cycles | Std. cycles | Avg. hanoi | Std. hanoi |
| :-----: | :-----: | :-----: | :-----: | :-----: |
| C | 0.000s | 0.00% | 0.000s | 0.00% |
| Pascal | 0.000s | 200.00% | 0.001s | 81.65% |
| Java | 0.001s | 50.00% | 0.001s | 50.00% |
| Ruby | 0.004s | 17.82% | 0.008s | 23.33% |

![Bar graph results 1](results/bar_graph1.png)

![Box graph results 1](results/box_graph1.png)

#### Test 2. - Discs 20, Iterations 10000000
    
| Lang | Avg. cycles | Std. cycles | Avg. hanoi | Std. hanoi |
| :-----: | :-----: | :-----: | :-----: | :-----: |
| C | 0.000s | 0.00% | 0.000s | 0.00% |
| Pascal | 0.028s | 3.47% | 0.011s | 11.32% |
| Java | 0.017s | 4.82% | 0.005s | 14.81% |
| Ruby | 0.343s | 4.32% | 0.237s | 1.74% |

![Bar graph results 2](results/bar_graph2.png)

![Box graph results 2](results/box_graph2.png)

#### Test 3. - Discs 25, Iterations 100000000
    
| Lang | Avg. cycles | Std. cycles | Avg. hanoi | Std. hanoi |
| :-----: | :-----: | :-----: | :-----: | :-----: |
| C | 0.000s | 0.00% | 0.000s | 0.00% |
| Pascal | 0.288s | 0.56% | 0.341s | 3.12% |
| Java | 0.171s | 7.46% | 0.168s | 1.16% |
| Ruby | Dead | Dead | Dead | Dead |

![Bar graph results 3](results/bar_graph3.png)

![Box graph results 3](results/box_graph3.png)

#### Test 4. - Discs 30, Iterations 1000000000
    
| Lang | Avg. cycles | Std. cycles | Avg. hanoi | Std. hanoi |
| :-----: | :-----: | :-----: | :-----: | :-----: |
| C | Dead | Dead | Dead | Dead |
| Pascal | Dead | Dead | Dead | Dead |
| Java | Dead | Dead | Dead | Dead |
| Ruby | Dead | Dead | Dead | Dead |

![Bar graph results 4](results/bar_graph4.png)

![Box graph results 4](results/box_graph4.png)

#### Test 5. - Discs 32, Iterations 4294967295
    
| Lang | Avg. cycles | Std. cycles | Avg. hanoi | Std. hanoi |
| :-----: | :-----: | :-----: | :-----: | :-----: |
| C | Dead | Dead | Dead | Dead |
| Pascal | Dead | Dead | Dead | Dead |
| Java | Dead | Dead | Dead | Dead |
| Ruby | Dead | Dead | Dead | Dead |

![Bar graph results 5](results/bar_graph5.png)

![Box graph results 5](results/box_graph5.png)

