<?php 

function hanoi($n, $start, $dest, $sticks){
	if($n === 0){
		return;
	}

	$temp = $sticks - $start - $dest;
	hanoi($n - 1, $start, $temp, $sticks);
	hanoi($n - 1, $temp, $dest, $sticks);
}

function cycle($n){
	$i = 0;
	while($i < $n){
		$i += 1;
	}
}

function testHanoi($n, $sticks){
	$startTime = microtime(True);
	hanoi($n, 1, $sticks - 1, $sticks);
	echo "Hanoi test passed in " . number_format((microtime(True)-$startTime), 3) . "s.\n";
}

function testCycle($n){
	$startTime = microtime(True);
	cycle($n);
	echo "Cycle test passed in " . number_format((microtime(True)-$startTime), 3) . "s.\n";
}

echo "PHP:\n";
testHanoi((int)$argv[1], (int)$argv[2]);
testCycle((int)$argv[3]);

?>