# Functional Program Generation using Genetic Programming
Developed for the AI in Software Engineering course for my MSc. course.

## Features so far:
- parse LISP expressions (operators, conditions, comparisons, null, functions)
- evaluate LISP expression
- defun token + recursive functions
- identify all tokens to use as elements for reproduction in genes
- check validity of S-expression (using "parse_sexp" or pre-existing compiler "SBCL")
- use an existing lisp compiler to ensure program correctness and output (difficult to implement everything)
- considered a different chromosome representation: s-expressions
- mutation techniques: shrink, subtree, swap
- inserted perfect candidate in initial pool and see what happens
- cache fitness computations for candidates without changes - use unique candidate ids
- improved mutation fairness
- add similarity coefficient computation in fitness function (ex: https://www.mdpi.com/2076-3417/11/10/4673)
  - caching won't work this way, cause the fitness of an individual is dependent on all other individuals now

## Notes:
- "Null" checks whether a list is empty or not.
- consider idea: take some existing LISP code, evaluate it, scan it, then generate it.
- SBCL command for factorial program 
sbcl --noinform --eval "(defun factorial (n) (cond ((zerop n) 1) (t (* n (factorial (- n 1))))))" --eval "(print (factorial 3))" --quit --disable-debugger
  