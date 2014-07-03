(defn hanoi [n start end sticks]
	(cond 
		(= n 0) true
		true (let [temp (- sticks start end)]
			(hanoi (- n 1) start temp sticks)
			(hanoi (- n 1) temp start sticks)
		)
	)
)

(defn cycles [n]
	(loop [i 0]
		(when (< i n)
			(recur (+ i 1))
		)
	) true
)

(defn timeMeasure [func args]
	(let [startTime (System/currentTimeMillis)]
		(cond (apply func args) 
			(float (/ (- (System/currentTimeMillis) startTime) 1000))
		)
	)
)

(defn testHanoi [n sticks]
	(format "Hanoi test passed in %.3fs."
		(timeMeasure hanoi (list n 1 (- sticks 1) sticks))
	)
)

(defn testCycle [n]
	(format "Cycle test passed in %.3fs."
		(timeMeasure cycles (list n))
	)
)

(let [args *command-line-args*]
	(println "Clojure:")
	(println (testHanoi (read-string (nth args 0)) (read-string (nth args 1))))
	(println (testCycle (read-string (nth args 2))))
)
