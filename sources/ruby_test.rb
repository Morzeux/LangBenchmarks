def hanoi(n, start, dest, sticks)
    if n == 0
        return
    end
    
    temp = sticks - start - dest
    hanoi(n - 1, start, temp, sticks)
    hanoi(n - 1, temp, dest, sticks)
end
    
def cycle(n)
    i = 0
    while i < n
        i += 1
    end
end
        
def testHanoi(n, sticks)
    startTime = Time.now()
    hanoi(n, 1, sticks - 1, sticks)
    puts 'Hanoi test passed in %.3fs.' % (Time.now() - startTime)
end
    
def testCycle(n)
    startTime = Time.now()
    cycle(n)
    puts 'Cycle test passed in %.3fs.' % (Time.now() - startTime)
end

puts 'Ruby:'
testHanoi(ARGV[0].to_i, ARGV[1].to_i)
testCycle(ARGV[2].to_i)
