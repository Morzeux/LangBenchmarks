(define (hanoi n start end sticks)
    (cond ((= n 0) #t)
    (else (let ((temp (- sticks start end)))
        (hanoi (- n 1) start temp sticks)
        (hanoi (- n 1) temp start sticks)
    )))
)

(define (cycle n)
    (do ((i 0 (+ i 1))) ((<= n i)))
)

(define (format-time time)
    (cond ((< time 1.0) (format "0~0,3F" time))
    (else (format "~0,3F" time)))
)

(define (timeMeasure func args)
    (let ((startTime (real-time-clock)))
        (cond ((apply func args) 
            (format-time (/ (- (real-time-clock) startTime) 1000.0)))
        )
    )
)

(define (testHanoi n sticks)
    (format "Hanoi test passed in ~as.~%"
        (timeMeasure hanoi (list n 1 (- sticks 1) 6))
    )
)

(define (testCycle n)
    (format "Cycle test passed in ~as.~%"
        (timeMeasure cycle (list n))
    )
)

(display (format "Scheme:~%"))
(display (testHanoi (string->number (car (command-line))) (string->number (cadr (command-line)))))
(display (testCycle (string->number (caddr (command-line)))))
