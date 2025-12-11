Day 04 – If / Else Statements

Today we learned decision making in Python using:

if
else
elif

These statements allow the program to take decisions based on conditions.

What is an if statement?
The if statement checks a condition.
If the condition is True, the code inside if will run.

Syntax:

if condition:
    statement
    
Example:

if age >= 18:
    print("Adult")

What is an else statement?
The else block runs only if the if condition becomes False.

Syntax:

if condition:
    statement1
else:
    statement2


Example:

if num > 0:
    print("Positive")
else:
    print("Negative")

What is an elif statement?
elif means "else if".
It is used when we need multiple conditions.

Syntax:

if condition1:
    statement1
elif condition2:
    statement2
else:
    statement3


Example:

if marks >= 90:
    print("A")
elif marks >= 75:
    print("B")
else:
    print("C")

Programs Covered Today

✔ Program 1: Check Positive or Negative
Uses simple if–else.

✔ Program 2: Check Even or Odd
Uses modulus (%) to check divisibility.

✔ Program 3: Largest of Two Numbers
Compares two values using > operator.

✔ Program 4: Grading System
Uses multiple conditions with elif.
