public class java_test {
	
	static void hanoi(int n, int start, int end, int sticks){
		if (n == 0){
			return;
		}
		int temp = sticks - start - end;
		hanoi(n - 1, start, temp, sticks);
		hanoi(n - 1, temp, start, sticks);
	}

	static void cycle(long n){
		long i = 0;
		while (i < n) {
			i += 1;
		}
	}
	
	static void testHanoi(int n, int sticks){
		long startTime = System.currentTimeMillis();
		hanoi(n, 1, sticks - 1, sticks);
		System.out.printf("Hanoi test passed in %.3fs.\n", (System.currentTimeMillis() - startTime) / 1000.0f);
	}

	static void testCycle(long n){
		long startTime = System.currentTimeMillis();
		cycle(n);
		System.out.printf("Cycle test passed in %.3fs.\n", (System.currentTimeMillis() - startTime) / 1000.0f);
	}

	public static void main(String[] args) {
		System.out.println("Java:");
		testHanoi(Integer.parseInt(args[0]), Integer.parseInt(args[1]));
		testCycle(Long.parseLong(args[2]));
	}

}