**Day 03 – Python Operators**
Today we explored different types of Python operators.
Operators are symbols/keywords that help Python perform actions like math, comparison, logic, updating values, and binary calculations.

**1. Arithmetic Operators**
Used to perform mathematical operations.

✔ Syntax:
result = a operator b

Example:
c = a + b

Operators:
+ → addition
- → subtraction
* → multiplication
/ → division
// → floor division (removes decimal part)
% → modulus (remainder)
** → exponent (power)

✔ Example Used in Program:
a = 15
b = 4
print(a + b)

**2. Comparison Operators**
Compare two values and return True or False.

✔ Syntax:
result = a operator b

Example:
a == b

✔ Operators:
== → equal
!= → not equal
> → greater
< → smaller
>= → greater or equal
<= → smaller or equal

✔ Example Used in Program:
x = 10
y = 20
print(x < y)   # True

**3. Logical Operators**

Combine or modify conditions.
Python does NOT use &&, ||, !.
Python uses English-like words.

✔ Syntax:
condition1 and condition2
condition1 or condition2
not condition

✔ Operators:
and → True only if both conditions true
or → True if at least one condition true
not → reverses True/False

**4. Assignment Operators**

Used to assign or update values.

Syntax:
x = 10     (assign)
x += 5     (x = x + 5)
x -= 3     (x = x - 3)
x *= 2     (x = x * 2)
x /= 4     (x = x / 4)
x //= 3    (x = x // 3)
x %= 2     (x = x % 2)
x **= 2    (x = x ** 2)

Meaning:

+= adds and assigns

-= subtracts and assigns

*= multiplies and assigns

/= divides and assigns

**= raises to power and assigns


**5. Bitwise Operators**
These work on the binary bits of numbers.

Syntax
a & b     # AND
a | b     # OR
a ^ b     # XOR
~a        # NOT (flip all bits)
a << n    # Left shift by n bits
a >> n    # Right shift by n bits

Explanation with Example

We used:

a = 5   → 0101  
b = 3   → 0011

Output:

a & b → 1
a | b → 7
a ^ b → 6
~a → -6
a << 1 → 10
a >> 1 → 2

Right shift (>>) adds 0 on the left for positive numbers.
