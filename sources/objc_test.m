#import <Foundation/Foundation.h>

@interface ObjCTest : NSObject

+ (void) testHanoi: (int) n : (int) sticks;

+ (void) testCycle: (unsigned long) n;

@end

@implementation ObjCTest

+ (void) hanoi: (int) n : (int) start : (int) end : (int) sticks{
    if (n == 0){
        return;
    }
    int temp = sticks - start - end;
    [self hanoi: n - 1 : start : temp : sticks];
    [self hanoi: n - 1 : temp : start : sticks];
}

+ (void) cycle: (unsigned long) n{
    unsigned long i = 0;
    while (i < n){
        i += 1;
    }
}

+ (void) testHanoi: (int) n : (int) sticks {
    NSDate *startTime = [NSDate date];
    [self hanoi: n : 1 : sticks - 1 : sticks];
    printf("Hanoi test passed in %.3lfs.\n", [startTime timeIntervalSinceNow] * -1);
}

+ (void) testCycle: (unsigned long) n {
    NSDate *startTime = [NSDate date];
    [self cycle: n];
    printf("Cycle test passed in %.3lfs.\n", [startTime timeIntervalSinceNow] * -1);
}

@end

int main(int argc, char *argv[])
{
    printf("Objective-C:\n");
    [ObjCTest testHanoi: atoi(argv[1]) : atoi(argv[2])];
    [ObjCTest testCycle: strtoul(argv[3], NULL, 10)];
    return 0;
}