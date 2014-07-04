import std.stdio;
import std.datetime;
import std.conv;

void hanoi(int n, int start, int end, int sticks){
    if (n == 0){
        return;
    }
    int temp = sticks - start - end;
    hanoi(n - 1, start, temp, sticks);
    hanoi(n - 1, temp, start, sticks);
}

void cycle(uint n){
    uint i = 0;
    while (i < n){
        i += 1;
    }
}

void testHanoi(int n, int sticks){
    StopWatch sw;
    sw.start();
    hanoi(n, 1, sticks - 1, sticks);
    sw.stop();
    writefln("Hanoi test passed in %.3fs.", sw.peek().msecs / 1000.0f);
}

void testCycle(uint n){
    StopWatch sw;
    sw.start();
    cycle(n);
    sw.stop();
    writefln("Cycle test passed in %.3fs.", sw.peek().msecs / 1000.0f);
}

void main(string[] args) {
    writeln("D:");
    testHanoi(to!int(args[1]), to!int(args[2]));
    testCycle(to!uint(args[3]));
}
