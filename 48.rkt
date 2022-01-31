#lang racket

(require math)

(define digits (expt 10 10))

(foldl (λ (x result) (modulo (+ result (modular-expt x x digits)) digits))
       0
       (range 1 1001))

; o7 to modular-expt for this one