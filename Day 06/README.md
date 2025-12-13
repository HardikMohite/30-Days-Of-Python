📘 Day 06 – Pattern Programs (Basics)

In this day, we practiced pattern printing programs.
Pattern programs help us understand:

loops (for)

nested loops

how rows and columns work

logic building (very important for C, Java, Python)

These patterns are common in C, Java, and Python.

🔹 What is a Pattern Program?

A pattern program prints symbols (like *, numbers, or characters) in a specific shape using loops.

Example:

*
**
***
****

🔹 Why We Use Nested Loops in Patterns

Outer loop → controls rows

Inner loop → controls columns

print() → prints the symbol

print() without arguments → moves to next line

🔹 General Logic of Pattern Programs
for each row:
    for each column:
        print symbol
    go to next line


This logic is the same in C, Java, and Python.

🔹 Pattern 1: Solid Square Pattern

Output:

*****
*****
*****
*****
*****

Logic:

Fixed number of rows

Fixed number of columns

Print * in every position

🔹 Pattern 2: Right Angle Triangle (Stars)

Output:

*
**
***
****
*****

Logic:

Row number decides how many stars to print

Inner loop runs equal to row number

🔹 Pattern 3: Inverted Right Angle Triangle

Output:

*****
****
***
**
*

Logic:

Start with maximum stars

Reduce stars in every next row

Loop runs in reverse order

🔹 Pattern 4: Hollow Rectangle

Output:

*****
*   *
*   *
*****

Logic:

Print * for:

First row

Last row

First column

Last column

Print space " " inside

This pattern improves conditional thinking inside loops.

🔹 Pattern 5: Floyd’s Triangle

Output:

1
2 3
4 5 6
7 8 9 10

Logic:

Use a number variable

Increase number after every print

Rows decide how many numbers to print
