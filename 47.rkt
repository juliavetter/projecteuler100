#lang racket

(require math/number-theory)

(define (findnum x)
  (let [(divs (list
               (prime-divisors x)
               (prime-divisors (+ 1 x))
               (prime-divisors (+ 2 x))
               (prime-divisors (+ 3 x))
               ))]
    (cond [(andmap (λ (lst)
                     (and
                      (= (length lst) 4) ; all numbers have 4 prime factors
                      (not (check-duplicates lst)))) ; all numbers have distinct prime factors
                   divs)
           (print x)]
          [else (findnum (+ 1 x))])))

(findnum 0)