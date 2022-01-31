#lang racket

(require math/number-theory)

(define (divisor-sum x)
  (- (apply + (divisors x)) x))

; a list of pairs: (x . (divisor-sum x))
(define divsums
  (map
   (λ (x) (cons x (divisor-sum x)))
   (range 1 10000)))

; a list of pairs: ((divisor-sum x) . x)
(define rev-divsums
  (map
   (λ (x) (cons (cdr x) (car x)))
   divsums))

; sum the amicable numbers
(foldl (λ (x result)
         (cond [(= (car x) (cdr x)) ; don't include numbers that are the sum of their own divisors
                result]
               [(member x rev-divsums) ; we have an amicable number
                (+ (car x) result)] ; add it to the sum
               [else
                result]))
       0
       divsums)