-module(erlang_test).

cycle(0) -> true;
cycle(N) -> cycle(N-1).

hanoi(0, _, _, _) -> true;
hanoi(N, S, E, ST) ->
    T = ST - S - E,
    hanoi(N - 1, S, T, ST),
    hanoi(N - 1, T, E, ST).

testHanoi(N, Sticks) ->
    statistics(wall_clock),
    hanoi(N, 1, Sticks - 1, Sticks),
    {_, EndTime} = statistics(wall_clock),
    io:format("Hanoi test passed in ~.3fs.\n", [EndTime / 1000]).

testCycle(N) ->
    statistics(wall_clock),
    cycle(N),
    {_, EndTime} = statistics(wall_clock),
    io:format("Cycle test passed in ~.3fs.\n", [EndTime / 1000]).

main([A1, A2, A3]) ->
    {N, _} = string:to_integer(A1),
    {Sticks, _} = string:to_integer(A2),
    {Iters, _} = string:to_integer(A3),
    io:format("Erlang:\n"),
    testHanoi(N, Sticks),
    testCycle(Iters).
