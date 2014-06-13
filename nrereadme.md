LangBenchmarks

==============

Performance benchmarks for several programming languages. To modify languages config you need to edit "config.ini" file. Feel free to modify this code and run tests on your computer :)

At now benchmark support is for:

C, C#, Java, JavaScript, PHP, Ruby, Python, Prolog, Common Lisp.

More languages are comming soon...

Results

=======

Available compilers:

************************************************************

C compiler: gcc.exe (GCC) 4.8.1

C# compiler: Microsoft (R) Visual C# Compiler version 4.0.30319.18408

Java compiler: javac 1.8.0_05

JavaScript (node.js) compiler: v0.10.28

PHP compiler: PHP 5.5.13 (cli) (built: May 28 2014 09:50:06)

Ruby compiler: ruby 2.0.0p451 (2014-02-24) [i386-mingw32]

Python compiler: Python 3.4.0

Prolog compiler: SWI-Prolog version 6.6.5 for i386-win32

Common Lisp compiler: GNU CLISP 2.49 (2010-07-07) (built on STSst063.jenty.by [1

50.0.0.63])

System:

************************************************************

Operating System: Windows-7-6.1.7601-SP1

Processor: Intel64 Family 6 Model 37 Stepping 5, GenuineIntel

Total memory: 3.866GB

Compiling results:

************************************************************

Compiling C... OK

Compiling C#... OK

Compiling Java... OK

Test results (5 evaluations):

************************************************************

1. Hanoi(disks=10, sticks=6); Cycles(iters=1000)

  C:

    Hanoi: 0.000s (SD 0.00%)

    Cycles: 0.000s (SD 0.00%)

  C#:

    Hanoi: 0.000s (SD 0.00%)

    Cycles: 0.000s (SD 0.00%)

  Java:

    Hanoi: 0.000s (SD 0.00%)

    Cycles: 0.000s (SD 0.00%)

  JavaScript:

    Hanoi: 0.006s (SD 122.47%)

    Cycles: 0.000s (SD 0.00%)

  PHP:

    Hanoi: 0.003s (SD 200.00%)

    Cycles: 0.000s (SD 0.00%)

  Ruby:

    Hanoi: 0.000s (SD 0.00%)

    Cycles: 0.000s (SD 0.00%)

  Python:

    Hanoi: 0.003s (SD 200.00%)

    Cycles: 0.000s (SD 0.00%)

  Prolog:

    Hanoi: 0.006s (SD 122.47%)

    Cycles: 0.000s (SD 0.00%)

  Common Lisp:

    Hanoi: 0.000s (SD 0.00%)

    Cycles: 0.000s (SD 0.00%)

2. Hanoi(disks=15, sticks=6); Cycles(iters=100000)

  C:

    Hanoi: 0.000s (SD 0.00%)

    Cycles: 0.000s (SD 0.00%)

  C#:

    Hanoi: 0.000s (SD 0.00%)

    Cycles: 0.000s (SD 0.00%)

  Java:

    Hanoi: 0.000s (SD 0.00%)

    Cycles: 0.000s (SD 0.00%)

  JavaScript:

    Hanoi: 0.000s (SD 0.00%)

    Cycles: 0.003s (SD 200.00%)

  PHP:

    Hanoi: 0.034s (SD 18.71%)

    Cycles: 0.006s (SD 122.47%)

  Ruby:

    Hanoi: 0.003s (SD 200.00%)

    Cycles: 0.000s (SD 0.00%)

  Python:

    Hanoi: 0.028s (SD 21.43%)

    Cycles: 0.013s (SD 50.00%)

  Prolog:

    Hanoi: 0.009s (SD 72.96%)

    Cycles: 0.003s (SD 200.00%)

  Common Lisp:

    Hanoi: 0.065s (SD 9.82%)

    Cycles: 0.078s (SD 0.00%)

3. Hanoi(disks=20, sticks=6); Cycles(iters=10000000)

  C:

    Hanoi: 0.012s (SD 50.00%)

    Cycles: 0.022s (SD 33.40%)

  C#:

    Hanoi: 0.010s (SD 0.00%)

    Cycles: 0.010s (SD 0.00%)

  Java:

    Hanoi: 0.006s (SD 122.58%)

    Cycles: 0.016s (SD 2.53%)

  JavaScript:

    Hanoi: 0.022s (SD 34.99%)

    Cycles: 0.010s (SD 81.65%)

  PHP:

    Hanoi: 1.145s (SD 0.64%)

    Cycles: 0.400s (SD 1.96%)

  Ruby:

    Hanoi: 0.224s (SD 3.49%)

    Cycles: 0.322s (SD 2.44%)

  Python:

    Hanoi: 0.945s (SD 1.32%)

    Cycles: 1.379s (SD 3.16%)

  Prolog:

    Hanoi: 0.437s (SD 9.96%)

    Cycles: 0.562s (SD 0.07%)

  Common Lisp:

    Hanoi: 2.018s (SD 0.39%)

    Cycles: 7.373s (SD 0.31%)

4. Hanoi(disks=25, sticks=6); Cycles(iters=100000000)

  C:

    Hanoi: 0.337s (SD 2.33%)

    Cycles: 0.281s (SD 0.00%)

  C#:

    Hanoi: 0.320s (SD 3.42%)

    Cycles: 0.120s (SD 0.00%)

  Java:

    Hanoi: 0.159s (SD 4.02%)

    Cycles: 0.162s (SD 4.54%)

  JavaScript:

    Hanoi: 0.543s (SD 1.10%)

    Cycles: 0.125s (SD 0.00%)

  PHP:

    Hanoi: 36.632s (SD 1.09%)

    Cycles: 4.003s (SD 0.40%)

  Ruby:

    Hanoi: 7.432s (SD 0.10%)

    Cycles: 3.204s (SD 0.24%)

  Python:

    Hanoi: 29.809s (SD 0.81%)

    Cycles: 13.734s (SD 0.56%)

  Prolog:

    Hanoi: 14.209s (SD 1.04%)

    Cycles: 11.741s (SD 1.39%)

  Common Lisp:

    Hanoi: 64.194s (SD 0.05%)

    Cycles: 99.054s (SD 1.11%)

5. Hanoi(disks=30, sticks=6); Cycles(iters=1000000000)

  C:

    Hanoi: 10.773s (SD 0.12%)

    Cycles: 2.777s (SD 0.35%)

  C#:

    Hanoi: 10.126s (SD 0.71%)

    Cycles: 1.200s (SD 1.05%)

  Java:

    Hanoi: 4.630s (SD 0.13%)

    Cycles: 1.601s (SD 0.79%)

  JavaScript:

    Hanoi: 18.109s (SD 5.13%)

    Cycles: 1.454s (SD 34.77%)

  PHP:

    Hanoi: Killed

    Cycles: Killed

  Ruby:

    Hanoi: Killed

    Cycles: Killed

  Python:

    Hanoi: Killed

    Cycles: Killed

  Prolog:

    Hanoi: Killed

    Cycles: Killed

  Common Lisp:

    Hanoi: Killed

    Cycles: Killed

************************************************************

Cleaning up... OK

