(DEFUN hanoi (n start end sticks)
    (cond ((eq n 0) T)
    (T (let ((temp (- sticks start end))) 
        (hanoi (- n 1) start temp sticks)
        (hanoi (- n 1) temp start sticks)
    )))
)

(DEFUN cycle (n)
    (let ((i 0))
    (loop while (< i n) do 
        (setq i (+ i 1))
    ) T)
)

(DEFUN timeMeasure (func args)
    (let ((startTime (get-internal-real-time)))
        (cond ((apply func args) 
            (/ (- (get-internal-real-time) startTime) 1000000))
        )
    )
)

(DEFUN testHanoi (n sticks)
    (format t "Hanoi test passed in ~,3Fs.~%" 
        (timeMeasure 'hanoi (list n 1 (- sticks 1) sticks))
    )
)

(DEFUN testCycle (n)
    (format t "Cycle test passed in ~,3Fs.~%"
        (timeMeasure 'cycle (list n))
    )
)

(format t "Common Lisp:~%")
(testHanoi (parse-integer (car *args*)) (parse-integer (cadr *args*)))
(testCycle (parse-integer (caddr *args*)))
