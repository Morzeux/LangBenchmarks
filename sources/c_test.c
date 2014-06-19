#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>

void hanoi(int n, int start, int end, int sticks){
	if (n == 0){
		return;
	}
	int temp = sticks - start - end;
	hanoi(n - 1, start, temp, sticks);
	hanoi(n - 1, temp, start, sticks);
}

void cycle(unsigned long n){
	unsigned long i = 0;
	while (i < n){
		i += 1;
	}
}

void testHanoi(int n, int sticks){
	double startTime = (double)clock();
	hanoi(n, 1, sticks - 1, sticks);
	printf("Hanoi test passed in %.3fs.\n", (clock() - startTime) / 1000.0f);
}

void testCycle(unsigned long n){
	double startTime = (double)clock();
	cycle(n);
	printf("Cycle test passed in %.3fs.\n", (clock() - startTime) / 1000.0f);
}

int main(int argc, char *argv[]){
	printf("C:\n");
	testHanoi(atoi(argv[1]), atoi(argv[2]));
	testCycle(strtoul(argv[3], NULL, 10));
	return 0;
}
