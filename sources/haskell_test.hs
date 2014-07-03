{-# LANGUAGE BangPatterns #-}
import Data.Time
import Text.Printf
import System.Environment

hanoi n start end sticks
	| n == 0 = True
	| otherwise = hanoi (n-1) start temp sticks && hanoi (n-1) temp start sticks
	where temp = sticks - start - end

cycle' n
	| n == 0 = True
	| otherwise = cycle' (n-1)

getTime time = read (init . show $ time) :: Float

testHanoi n sticks = do
	startTime <- getCurrentTime
	let !_ = hanoi n 1 (sticks-1) sticks
	endTime <- getCurrentTime
	printf "Hanoi test passed in %.3fs.\n" (getTime (diffUTCTime endTime startTime))

testCycle n = do
	startTime <- getCurrentTime
	let !_ = cycle' n
	endTime <- getCurrentTime
	printf "Cycle test passed in %.3fs.\n" (getTime (diffUTCTime endTime startTime))

main = do 
	args <- getArgs
	printf "Haskell:\n"
	testHanoi (read (args !! 0) :: Int) (read (args !! 1) :: Int)
	testCycle (read (args !! 2) :: Int)
