#lang racket

(findf even? '(1 2 3 4))

(for/first ([n '(1 2 3 4)]
            #:when (even? n))
           n)

(for/first ([i '(1 2 3)]
            [j "abc"]
            #:when (odd? i)
            [k #(#t #f)])
  (list i j k))

(findf (λ (x) (odd? (first x)))
       (for/list ([i '(1 2 3)]
                  [j "abc"]
                  [k #(#t #f)])
         (list i j k)))
