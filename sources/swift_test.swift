import Foundation

func hanoi(n: Int, start: Int, end: Int,  sticks: Int) -> Void {
    if (n == 0){
        return
    }
    let temp = sticks - start - end
    hanoi(n - 1, start, temp, sticks)
    hanoi(n - 1, temp, start, sticks)
}

func cycle(n: UInt) -> Void {
    var i:UInt = 0
    while (i < n) {
        i += 1;
    }
}

func testHanoi(n: Int, sticks: Int) -> Void {
    let startTime = NSDate()
    hanoi(n, 1, n - 1, sticks)
    println(NSString(format: "Hanoi test passed in %.3fs.", NSDate().timeIntervalSinceDate(startTime)))
}

func testCycle(n: UInt) -> Void {
    let startTime = NSDate()
    cycle(n)
    println(NSString(format: "Cycle test passed in %.3fs.", NSDate().timeIntervalSinceDate(startTime)))
}

let args = Process.arguments
println("Swift:")
testHanoi(args[1].toInt()!, args[2].toInt()!)
testCycle(UInt(args[3].toInt()!))
