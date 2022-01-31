#lang racket

(require (except-in math/number-theory
                    permutations))

(define (number->list-a x)
  (cond [(= x 0) '()]
        [else (cons
               (remainder x 10)
               (number->list-a (quotient x 10)))]))

(define (number->list x)
  (reverse (number->list-a x)))

(define (list->number lst)
  (/
   (foldl (λ (x result) (* 10 (+ result x)))
          0
          lst)
   10))

(define (num-permutations x)
  (remove-duplicates (map list->number (permutations (number->list x)))))

(define (prime-sequence?-a x y)
  (cond [(= y 0) #f]
        [(and (prime? (+ x y))
              (prime? (+ x y y))
              (member (+ x y) (num-permutations x))
              (member (+ x y y ) (num-permutations x)))
         #t]
        [else (prime-sequence?-a x (sub1 y))]))

; can x form a prime sequence, bounded by 10000
(define (prime-sequence? x)
  (prime-sequence?-a x (quotient (- 10000 x) 2)))

(filter prime-sequence? (filter prime? (range 3333))) ; we only need to check up to 10000/3
; we get 2969
(sort (filter prime? (num-permutations 2969)) <)