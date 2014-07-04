#!/bin/bash

function hanoi {
    if [ $1 = 0 ]; then
        return
    fi

    local temp=$[$4-$2-$3]
    hanoi $[$1-1] $2 $temp $4
    hanoi $[$1-1] $temp $2 $4
}

function cycle {
    local i=0
    while [ $i -lt $1 ]; do
        let i=i+1
    done 
}

function testHanoi {
    start=`python -c 'import time; print time.time()'`
    hanoi $1 1 $[$2-1] $2
    end=`python -c 'import time; print time.time()'`
    diff=$(echo "$end - $start" | bc)
    printf "Hanoi test passed in %.3fs.\n" $diff
}

function testCycle {
    start=`python -c 'import time; print time.time()'`
    cycle $1
    end=`python -c 'import time; print time.time()'`
    diff=$(echo "$end - $start" | bc)
    printf "Cycle test passed in %.3fs.\n" $diff
}

echo "Bash:"
testHanoi $1 $2
testCycle $3
