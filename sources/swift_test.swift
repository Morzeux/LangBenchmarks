import Foundation

func getTime(value: Double, round: Int) -> String {
    let fmt = NSNumberFormatter()
    fmt.maximumFractionDigits = round
    fmt.minimumFractionDigits = round
    fmt.minimumIntegerDigits = 1

    return fmt.stringFromNumber(NSNumber(value: NSDate().timeIntervalSince1970 - value))!
}

func hanoi(n: Int, start: Int, end: Int,  sticks: Int) -> Void {
    if (n == 0){
        return
    }
    let temp = sticks - start - end
    hanoi(n: n - 1, start: start, end: temp, sticks: sticks)
    hanoi(n: n - 1, start: temp, end: start, sticks: sticks)
}

func cycle(n: UInt) -> Void {
    var i:UInt = 0
    while (i < n) {
        i += 1;
    }
}

func testHanoi(n: Int, sticks: Int) -> Void {
    let startTime = NSDate().timeIntervalSince1970
    hanoi(n: n, start: 1, end: n - 1, sticks: sticks)
    print("Hanoi test passed in " + getTime(value: startTime, round: 3) + "s.")
}

func testCycle(n: UInt) -> Void {
    let startTime = NSDate().timeIntervalSince1970
    cycle(n: n)
    print("Cycle test passed in " + getTime(value: startTime, round: 3) + "s.")
}

let args = Process.arguments
print("Swift:")
testHanoi(n: Int(args[1])!, sticks: Int(args[2])!)
testCycle(n: UInt(args[3])!)
