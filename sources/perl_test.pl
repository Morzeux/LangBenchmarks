#!/usr/bin/perl
use Time::HiRes qw( time );

sub hanoi {
    my ($n, $start, $end, $sticks) = (@_);
    if ($n == 0){
        return;
    }

    $temp = $sticks - $start - $end;
    hanoi($n - 1, $start, $temp, $sticks);
    hanoi($n - 1, $temp, $start, $sticks);
}

sub cycle {
    my ($n) = @_;
    my $i = 0;
    while ($i < $n){
        $i = $i + 1;
    }
}

sub testHanoi {
    my ($n, $sticks) = (@_);
    my $start = time();
    hanoi($n, 1, $sticks - 1, $sticks);
    printf("Hanoi test passed in %.3fs.\n", time() - $start);
}

sub testCycle {
    my ($n) = @_;
    my $start = time();
    cycle($n);
    printf("Cycle test passed in %.3fs.\n", time() - $start);
}

print "Perl:\n";
testHanoi($ARGV[0], $ARGV[1]);
testCycle($ARGV[2]);
