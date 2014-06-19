program pascal_test;
uses SysUtils, DateUtils;

procedure hanoi(n, start, _end, sticks: integer);
var
    temp: integer;
begin
    if n = 0 then
        exit;
    temp := sticks - start - _end;
    hanoi(n - 1, start, temp, sticks);
    hanoi(n - 1, temp, start, sticks);
end;

procedure cycle(n: cardinal);
var
    i: cardinal;
begin
    i := 0;
    while i < n do
        i := i + 1;
end;

procedure testHanoi(n, sticks: integer);
var
    startTime: TDateTime;
begin
    startTime := now;
    hanoi(n, 1, sticks - 1, sticks);
    writeln('Hanoi test passed in ', FormatFloat('0.000', MilliSecondsBetween(now, startTime)/1000), 's.');
end;

procedure testCycle(n: cardinal);
var
  startTime: TDateTime;
begin
    startTime := now;
    cycle(n);
    writeln('Cycle test passed in ', FormatFloat('0.000', MilliSecondsBetween(now, startTime)/1000), 's.')
end;

var
	disks, sticks: integer;
	iters: cardinal;
begin
    Val(ParamStr(1), disks);
    Val(ParamStr(2), sticks);
    Val(ParamStr(3), iters);
    writeln('Pascal:');
    testHanoi(disks, sticks);
    testCycle(iters);
end.
