
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
| Pascal | 0.000s | 122.47% | 0.000s | 122.47% |
| Java | 0.000s | 122.47% | 0.001s | 81.65% |
| Ruby | 0.004s | 23.18% | 0.009s | 17.39% |
    
![alt text](https://github.com/Morzeux/LangBenchmarks/tree/master/results/bar_graph1.png "Bar graph results 1")

![alt text](https://github.com/Morzeux/LangBenchmarks/tree/master/results/box_graph1.png "Box graph results 1")

#### Test 2. - Discs 20, Iterations 10000000
    
| Lang | Avg. cycles | Std. cycles | Avg. hanoi | Std. hanoi |
| :-----: | :-----: | :-----: | :-----: | :-----: |
| C | 0.000s | 0.00% | 0.000s | 0.00% |
| Pascal | 0.034s | 17.39% | 0.014s | 12.11% |
| Java | 0.020s | 11.45% | 0.006s | 28.98% |
| Ruby | 0.374s | 8.30% | 0.256s | 4.22% |
    
![alt text](https://github.com/Morzeux/LangBenchmarks/tree/master/results/bar_graph2.png "Bar graph results 2")

![alt text](https://github.com/Morzeux/LangBenchmarks/tree/master/results/box_graph2.png "Box graph results 2")

#### Test 3. - Discs 25, Iterations 100000000
    
| Lang | Avg. cycles | Std. cycles | Avg. hanoi | Std. hanoi |
| :-----: | :-----: | :-----: | :-----: | :-----: |
| C | 0.000s | 0.00% | 0.000s | 0.00% |
| Pascal | 0.293s | 1.66% | 0.355s | 2.99% |
| Java | 0.178s | 5.74% | 0.208s | 17.60% |
| Ruby | Dead | Dead | Dead | Dead |
    
![alt text](https://github.com/Morzeux/LangBenchmarks/tree/master/results/bar_graph3.png "Bar graph results 3")

![alt text](https://github.com/Morzeux/LangBenchmarks/tree/master/results/box_graph3.png "Box graph results 3")

#### Test 4. - Discs 30, Iterations 1000000000
    
| Lang | Avg. cycles | Std. cycles | Avg. hanoi | Std. hanoi |
| :-----: | :-----: | :-----: | :-----: | :-----: |
| C | Dead | Dead | Dead | Dead |
| Pascal | Dead | Dead | Dead | Dead |
| Java | Dead | Dead | Dead | Dead |
| Ruby | Dead | Dead | Dead | Dead |
    
![alt text](https://github.com/Morzeux/LangBenchmarks/tree/master/results/bar_graph4.png "Bar graph results 4")

![alt text](https://github.com/Morzeux/LangBenchmarks/tree/master/results/box_graph4.png "Box graph results 4")

#### Test 5. - Discs 32, Iterations 4294967295
    
| Lang | Avg. cycles | Std. cycles | Avg. hanoi | Std. hanoi |
| :-----: | :-----: | :-----: | :-----: | :-----: |
| C | Dead | Dead | Dead | Dead |
| Pascal | Dead | Dead | Dead | Dead |
| Java | Dead | Dead | Dead | Dead |
| Ruby | Dead | Dead | Dead | Dead |
    
![alt text](https://github.com/Morzeux/LangBenchmarks/tree/master/results/bar_graph5.png "Bar graph results 5")

![alt text](https://github.com/Morzeux/LangBenchmarks/tree/master/results/box_graph5.png "Box graph results 5")

