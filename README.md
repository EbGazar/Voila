# The Voila Programming Language

Welcome to the Voila repository! This repository contains all the necessary documents, design specifications, implementation details and related tools for Voila. Voila is an easy-to-learn programming language that has a simple syntax which makes it perfect for beginners.

Voila is an open source programming language that makes it easy to build simple.

## Voila - Language Features:

* Visualize Compiler `Lexer`.

* Visualize Compiler `Symbol Table`.

* Visualize Compiler `Parser`.

* Visualize Compiler `Parse Tree`.

* Visualize Compiler `Parse Table`.



## Voila - Language Definition: 

* `Language Delimiter` will be defined as “;” as end of line.

* `Boolean:` True and False.

* `Blocks` will be contained in ‘{’ and ‘}’.

* `Keywords (Reserved Words):` ‘#’, ‘;’, ‘for’, ‘while’, ‘if’, ‘elif’, ‘else’, ‘and’, ‘or’, ‘def’ and ‘print’.
Identifiers (Variables Name): starts with a letter (A to Z or a to z), lowercase and uppercase letters are distinct, and does not allow punctuation characters such as @, $, and %.

* `Operators:` + , - , * , / , **, == , != , < , > , <= , >=.

* `Literals:` Integers, Floating Points and Strings.

* `Data Structure:` List defined by double brackets ‘[]’.

* `Types` may `not change after assignment`, but `values may change`.

## Voila - Language Grammer:

```python
program
   : statement+
   ;

statement
   : 'if' paren_expr statement
   | 'if' paren_expr statement 'else' statement
   | 'while' paren_expr statement
   | '{' statement* '}'
   | expr ';'
   | ';'
   ;

expr
   : test
   | id '=' expr
   ;

test
   : sum
   | sum '<' sum
   ;

sum
   : term
   | sum '+' term
   | sum '-' term
   ;

term
   : id
   | integer
   | paren_expr
   ;

id
   : STRING
   ;

integer
   : INT
   ;


STRING
   : [A-Za-z][A-Za-z0-9_]*
   ;


INT
   : [0-99999]+
   ;
```

## Contributing

To contribute, please reach me in [LinkedIn](https://www.linkedin.com/in/ebgazar/) or [Gmail](https://mail.google.com/mail/u/0/#inbox?compose=CllgCHrjDTSNgGDVkrdVtJFtGCVxjRjqnBRfKNtLxWWCVhhfNBvmxvpjVRKJRljkgzcRWgmJsWg).

