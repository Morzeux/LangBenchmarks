object scala_test {

    def hanoi(n:Int, start:Int, end:Int, sticks:Int) : Unit = {
        if (n == 0){
            return
        }

        var temp:Int = sticks - start - end
        hanoi(n - 1, start, temp, sticks)
        hanoi(n - 1, temp, start, sticks)
    }

    def cycle(n:Long) : Unit = {
        var i:Long = 0
        while (i < n) {
            i += 1
        }
    }

    def testHanoi(n:Int, sticks:Int) : Unit = {
        val startTime = System.currentTimeMillis()
        hanoi(n, 1, sticks - 1, sticks)
        println("Hanoi test passed in %.3fs.".format((System.currentTimeMillis() - startTime) / 1000.0f))
    }

    def testCycle(n:Long) : Unit = {
        val startTime = System.currentTimeMillis()
        cycle(n)
        println("Cycle test passed in %.3fs.".format((System.currentTimeMillis() - startTime) / 1000.0f))
    }

    def main(args: Array[String]) {
        println("Scala:")
        testHanoi(args(0).toInt, args(1).toInt)
        testCycle(args(2).toLong)
    }

}
