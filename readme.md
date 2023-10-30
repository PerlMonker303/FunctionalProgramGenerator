# Functional Program Generation using Genetic Programming
Developed for the AI in Software Engineering course for my MSc. course.

## Features so far:
- parse LISP expressions (operators, conditions, comparisons, null, functions)
- evaluate LISP expression
- defun token + recursive functions
- identify all tokens to use as elements for reproduction in genes
- check validity of S-expression (using "parse_sexp")

## TODOs:
- define GA elements (chromosomes, fitness, etc...)
- generate program in the GA paradigm
- more operators: cutting a list (cdr or car or something) - depends on what data is used

## Notes:
- Main code in procedural.py
- "Null" checks whether a list is empty or not.
- consider idea: take some existing LISP code, evaluate it, scan it, then generate it.