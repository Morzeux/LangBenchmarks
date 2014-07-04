open System

let rec hanoi n start en sticks = 
    if n = 0 then
        ()
    else
        let temp = sticks - start - en
        hanoi (n - 1) start temp sticks
        hanoi (n - 1) temp start sticks

let cycle n = 
    let mutable i : uint32 = Convert.ToUInt32 0
    while i < n do
        i <- (i + (Convert.ToUInt32 1))

let testHanoi n sticks = 
    let sw = Diagnostics.Stopwatch()
    sw.Start()
    hanoi n 1 (sticks - 1) sticks
    sw.Stop()
    printfn "Hanoi test passed in %0.3fs." (sw.Elapsed.TotalMilliseconds / 1000.0)    

let testCycle n =
    let sw = Diagnostics.Stopwatch()
    sw.Start()
    cycle n
    sw.Stop()
    printfn "Cycle test passed in %0.3fs." (sw.Elapsed.TotalMilliseconds / 1000.0)

let args = Environment.GetCommandLineArgs()   
printfn "F#:"
testHanoi (Convert.ToInt32 args.[1]) (Convert.ToInt32 args.[2])
testCycle (Convert.ToUInt32 args.[3])
