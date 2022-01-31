#lang racket

(require math/number-theory)

; return true iff x - n^2 is prime
(define (goldbach?-a x n)
  (prime? (- x (* 2 (* n n)))))
  
; return true iff x follows the goldbach conjecture
(define (goldbach? x)
  (ormap
   (λ (y) (goldbach?-a x y))
   (range (+ 1 (floor (sqrt (/ x 2)))))))

(define (findnum x)
  (cond [(not (goldbach? x)) (print x)]
        [else (findnum (+ 2 x))]))

(findnum 3)