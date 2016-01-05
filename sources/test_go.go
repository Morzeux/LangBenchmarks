package main

import (
    "fmt"
    "time"
	"os"
	"strconv"
)

func hanoi(n int, start int, end int, sticks int) {
    if n == 0 {
        return
    }

    var temp = sticks - start - end
    hanoi(n - 1, start, temp, sticks)
    hanoi(n - 1, temp, start, sticks)
}


func cycle(n uint) {
	var i uint = 0

	for i < n {
		i += 1
	}
}

func testHanoi(n int, sticks int){
	var startTime = time.Now()
	hanoi(n, 1, n - 1, sticks)
	fmt.Println(fmt.Sprintf("Hanoi test passed in %.3fs.", time.Now().Sub(startTime).Seconds()))
}

func testCycle(n uint){
	var startTime = time.Now()
	cycle(n)
	fmt.Println(fmt.Sprintf("Cycle test passed in %.3fs.", time.Now().Sub(startTime).Seconds()))
}

func IntParse(value string) int {
	var intValue, _ = strconv.Atoi(value)
	return intValue
}

func main() {
	fmt.Println("Go:")
	testHanoi(IntParse(os.Args[1]), IntParse(os.Args[2]))
	testCycle(uint(IntParse(os.Args[3])))
}