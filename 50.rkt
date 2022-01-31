#lang racket

(require math/number-theory)

(define (remove-last lst)
  (take lst (sub1 (length lst))))

; return the longer of l1, l2
; if they are equal, return l2
(define (longer l1 l2)
  (cond [(> (length l1) (length l2)) l1]
        [else l2]))

; add prime numbers to lst, a list of decreasing consecutive prime numbers, while the sum is < max
(define (add-primes lst max)
  (cond [(> (apply + lst) max) (rest lst)]
        [(add-primes (cons (next-prime (first lst)) lst) max)]))

; remove elements from the beginning of lst until it sums to a prime number
(define (remove-primes lst)
  (cond [(prime? (apply + lst)) lst]
        [(remove-primes (rest lst))]))

; given a starting list (of maximum feasible length) of consecutive prime numbers lst, come up with a list of consecutive prime numbers that sums to a prime number less than max
(define (f lst max)
  (cond [(prime? (apply + lst)) lst] ; base case
        [else
         (let [(try-this (remove-primes lst))
               (now-this (f (add-primes (remove-last lst) max) max))] ; remove smallest el't, add as many primes possible s.t. sum is < max
           (longer try-this now-this))]))


(define n 1000000)
(define start (add-primes '(2) n))
(define answer (f start n))
(println answer)
(println (length answer))
(println (apply + answer))







           