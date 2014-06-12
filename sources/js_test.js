var hanoi = function(n, start, dest, sticks){
	if(n == 0){
		return;
	}

	var temp = sticks - start - dest;
	hanoi(n - 1, start, temp, sticks);
	hanoi(n - 1, temp, dest, sticks);
};

var cycle = function(n){
	var i = 0;
	while(i < n){
		i += 1;
	}
}

var testHanoi = function(n, sticks){
	var startTime = new Date().getTime();
	hanoi(n, 1, sticks - 1, sticks);
	console.log("Hanoi test passed in " + parseFloat((new Date().getTime() - startTime) / 1000).toFixed(3) + "s.");
};

var testCycle = function(n){
	var startTime = new Date().getTime();
	cycle(n);
	console.log("Cycle test passed in " + parseFloat((new Date().getTime() - startTime) / 1000).toFixed(3) + "s.");
};

console.log("JavaScript:");
testHanoi(parseInt(process.argv[2]), parseInt(process.argv[3]));
testCycle(parseInt(process.argv[4]));
