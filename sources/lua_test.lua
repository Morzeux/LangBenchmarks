function cycle(n)
    i = 0
    while (i < n) do
        i = i + 1
    end
end

function hanoi(n, start, en, sticks)
    if (n == 0) then
        return
    end
    temp = sticks - start - en
    hanoi(n - 1, start, temp, sticks)
    hanoi(n - 1, temp, start, sticks)
end

function testCycle(n)
    startTime = os.clock()
    cycle(n)
    print(string.format("Cycle test passed in %.3fs.", os.clock() - startTime))
end

function testHanoi(n, sticks)
    startTime = os.clock()
    hanoi(n - 1, 1, sticks - 1, sticks)
    print(string.format("Hanoi test passed in %.3fs.", os.clock() - startTime))
end

print("Lua:")
testHanoi(tonumber(arg[1]), tonumber(arg[2]))
testCycle(tonumber(arg[3]))
