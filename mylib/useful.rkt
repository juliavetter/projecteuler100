#lang racket

(provide number->list
         list->number
         base-convert)

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

(define (base-convert-a x b)
  (cond
    [(< x b) (cons x '())]
    [else (cons (remainder x b)
                (base-convert-a (quotient x b) b))]))

; converts a number given in base 10 to base b
(define (base-convert x b)
  (list->number (reverse (base-convert-a x b))))