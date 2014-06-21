using System;
using System.Diagnostics;

namespace CSharpTest
{
    class Program
    {
        static void hanoi(int n, int start, int end, int sticks){
	        if (n == 0){
		        return;
	        }
	        int temp = sticks - start - end;
	        hanoi(n - 1, start, temp, sticks);
	        hanoi(n - 1, temp, start, sticks);
        }

        static void cycle(ulong n){
	        ulong i = 0;
	        while (i < n){
		        i += 1;
	        }
        }

        static void testHanoi(int n, int sticks)
        {
            Stopwatch sw = new Stopwatch();
            sw.Start();
            hanoi(n, 1, sticks - 1, sticks);
            sw.Stop();
            Console.WriteLine("Hanoi test passed in {0}s.", String.Format("{0:0.000}", sw.ElapsedMilliseconds / 1000.0f));
        }

        static void testCycle(ulong n)
        {
            Stopwatch sw = new Stopwatch();
            sw.Start();
            cycle(n);
            sw.Stop();
            Console.WriteLine("Cycle test passed in {0}s.", String.Format("{0:0.000}", sw.ElapsedMilliseconds / 1000.0f));
        }

        static int Main(string[] args)
        {
            Console.WriteLine("C#:");
            testHanoi(Int32.Parse(args[0]), Int32.Parse(args[1]));
            testCycle(UInt64.Parse(args[2]));

            return 0;
        }
    }
}
