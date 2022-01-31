#lang racket

(require math/number-theory)

(length
 (filter (λ (x) (> x 1000000))
         (flatten
          (map (λ (x)
                 (map (λ (y) (binomial x y))
                      (range 1 (add1 x))))
               (range 1 101)))))