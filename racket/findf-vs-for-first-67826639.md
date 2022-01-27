# What's the difference between Racket's findf and for/first functions?

The difference is that `for/first` iterates like `for`, so you have the full power of the Racket's [`for`](https://docs.racket-lang.org/reference/for.html?q=for%2Ffind#%28form._%28%28lib._racket%2Fprivate%2Fbase..rkt%29._for%29%29) syntax available:

```racket
> (for/first ([i '(1 2 3)]
              [j "abc"]
              #:when (odd? i)
              [k #(#t #f)])
    (list i j k))
'(1 #\a #t)
```

To achieve the same with `findf`, you'd have to generate the entire list up front:

```racket
> (findf (λ (x) (odd? (first x)))
         (for/list ([i '(1 2 3)]
                    [j "abc"]
                    [k #(#t #f)])
           (list i j k)))
'(1 #\a #t)
```

For searching a single list, you're correct that using `findf` is probably the correct function. It's simple and does what you need. But if you want to search across a more complex list or a list you need to create inline, `for/first` is better.

---

Here are some more simple examples to show you the power of `for/first` (and thus `for`).

Let's say you have two variables, a list of numbers and a string of the alphabet, and you want to pair them one-to-one and return the first pair where the number is even.

```racket
(define numbers (range 1 27)) ; numbers 1 to 26
(define alphabet "abcdefghijklmnopqrstuvwxyz")
```

Using `findf`, you need to first convert the string into a list of characters, then zip the two lists into pairs, and then create a lambda (an anonymous function in Racket terms) to check if a given pair has an even number.

 ```racket
(findf (lambda (pair) (even? (first pair)))
       (map list numbers (string->list alphabet)))
```

Using `for/first`, you need to assign each sequence to an identifier, and then reference the number identifier in the `#:when` clause to check if the number is even. (`for` iterates over each sequence in parallel, calls `string->list` for you on the string, and only evaluates the body if the `#:when` returns true.)

```racket
(for/first ([num numbers]
            [str alphabet]
            #:when (even? num))
  (list num str))
```

In terms of character count, they're roughly even (101 to 109), but in terms of clarity, I think the `for/first` is more obvious in what it's doing: take two collections, iterate over both at the same time, only evaluate the body when the number is even, and return a list.

What if we wanted to return the first pair where the number is even and greater than 10? Here we start to see things become unwieldy.

```racket
(findf (lambda (pair)
         (let ([num (first pair)])
           (and (even? num)
                (> num 10))))
       (map list numbers (string->list alphabet)))
```

versus

```racket
(for/first ([num numbers]
            [str alphabet]
            #:when (even? num)
            #:when (> num 10))
  (list num str))
;; or
(for/first ([num numbers]
            [str alphabet]
            #:when (and (even? num)
                        (> num 10)))
  (list num str))
```

Each of the `for` variants (`for/first`, `for/list`, etc) does something slightly different with the body but the iteration logic is the same, allowing for the author to be exact in their intention without re-implementing that logic.
