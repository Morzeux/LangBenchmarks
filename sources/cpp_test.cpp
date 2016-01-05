#include <cstdlib>
#include <string>
#include <iostream>
#include <iomanip>
#include <ctime>

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
    std::cout << "Hanoi test passed in " << std::fixed << std::setprecision(3) << (clock() - startTime) / CLOCKS_PER_SEC << "s." << std::endl;
}

void testCycle(unsigned long n){
    double startTime = (double)clock();
    cycle(n);
    std::cout << "Cycle test passed in " << std::fixed << std::setprecision(3) << (clock() - startTime) / CLOCKS_PER_SEC << "s." << std::endl;
}

int main(int argc, char *argv[]){
    std::cout << "C++:" << std::endl;
    testHanoi(std::atoi(argv[1]), std::atoi(argv[2]));
    testCycle(std::stoul(argv[3], NULL, 10));
    return 0;
}
