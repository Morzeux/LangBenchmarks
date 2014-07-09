var sys:Class = getClassByName("avmplus.System");

function cycle(n:uint):void {
    var i:uint = 0;
    while (i < n){
        i += 1;
    }
}

function hanoi(n:int, start_:int, end:int, sticks:int):void {
    if (n == 0){
        return;
    }
    var temp = sticks - start_ - end;
    hanoi(n - 1, start_, temp, sticks)
    hanoi(n - 1, temp, start_, sticks)
}

function formatTime(start_:int, end:int, precision:int):String {
    var time_diff = (end - start_) / 1000;
    precision = Math.pow(10, precision);
    return String(Math.round(time_diff * precision) / precision);
}

function testHanoi(n:int, sticks:int):void {
    var startTime = new Date().getTime();
    hanoi(n, 1, sticks - 1, sticks);
    trace("Hanoi test passed in " + formatTime(startTime, new Date().getTime(), 3) + "s.");
}

function testCycle(n:uint):void {
    var startTime = new Date().getTime();
    cycle(n);
    trace("Cycle test passed in " + formatTime(startTime, new Date().getTime(), 3) + "s.");
}

trace("ActionScript3:");
testHanoi(int(sys.argv[0]), int(sys.argv[1]));
testCycle(uint(sys.argv[2]));
