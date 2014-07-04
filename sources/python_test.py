import sys
from time import time

def hanoi(n, start, dest, sticks):
    if n == 0:
        return

    temp = sticks - start - dest
    hanoi(n - 1, start, temp, sticks)
    hanoi(n - 1, temp, dest, sticks)

def cycle(n):
    i = 0
    while i < n:
        i += 1

def testHanoi(n, sticks):
    startTime = time()
    hanoi(n, 1, sticks - 1, sticks)
    print('Hanoi test passed in %.3fs.' % (time() - startTime))

def testCycle(n):
    startTime = time()
    cycle(n)
    print('Cycle test passed in %.3fs.' % (time() - startTime))

print('Python:')
testHanoi(int(sys.argv[1]), int(sys.argv[2]))
testCycle(int(sys.argv[3]))
