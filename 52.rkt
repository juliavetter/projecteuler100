#lang racket

(require "mylib/useful.rkt")

; return a list of length 10 where each element is the number of occurences of that digit in x
(define (digit-occurences x)
  (foldl (λ (digit lst) (list-update lst digit add1))
         (range 10)
         (number->list x)))

(define (same-digits x y)
  (let [(x-digits (digit-occurences x))
        (y-digits (digit-occurences y))]
    (equal? x-digits y-digits)))

(define (findnum start)
  (cond [(andmap (λ (x) (same-digits start x))
                 (build-list 2 (λ (i) (* start i))))
         start]
        ; if the first two digits of start are > 17 (i.e. x6 it will add another digit), go to the next digit up
        [(equal? (take (number->list start) 2) '(1 7)) (findnum (expt 10 (add1 (inexact->exact (floor (log start 10))))))]
        [else (findnum (add1 start))]))

(findnum 10)