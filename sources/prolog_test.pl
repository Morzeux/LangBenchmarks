hanoi(0, _, _, _) :- !.

hanoi(N, S, E, ST) :-
    T is ST - S - E,
    N1 is N - 1,
    hanoi(N1, S, T, ST),
    hanoi(N1, T, E, ST).

cycle(0) :- !.

cycle(N) :-
    N1 is N - 1,
    cycle(N1).

timeMeasure(FUNC, ARGS, TIME) :-
        S =.. [FUNC|ARGS],
    statistics(runtime, [_, T1]),
    call(S),
    statistics(runtime, [_, T2]),
    TIME is abs((T2 - T1) / 1000).

testHanoi(N, D) :-
    D1 is D - 1,
    timeMeasure(hanoi, [N, 1, D1, D], X),
    write('Hanoi test passed in '),
    format('~3f', [X]), write('s.'), nl.

testCycle(N) :-
    timeMeasure(cycle, [N], X),
    write('Cycle test passed in '),
    format('~3f', [X]), write('s.'), nl.

args([AC1, AC2, AC3]) :-
    current_prolog_flag(argv, [A1, A2, A3]),
    atom_number(A1, AC1),
    atom_number(A2, AC2),
    atom_number(A3, AC3).

:-
    (args([DISKS, STICKS, CYCLES]),
    write('Prolog:'), nl,
    testHanoi(DISKS, STICKS),
    testCycle(CYCLES), halt);
    (write('Must have three arguments.'), nl, halt).
