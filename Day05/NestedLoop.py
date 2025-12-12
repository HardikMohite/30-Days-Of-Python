# A nested loop means having one loop inside another loop.
# The outer loop runs first, and for every single execution of the outer loop,
# the inner loop runs completely.
# Nested loops are mainly used to print patterns, work with 2D lists, matrices, etc.

for i in range(1, 4):          # Outer loop → controls number of rows
    for j in range(1, 4):      # Inner loop → controls number of columns
        print(i, j)            # Prints pair of (i, j)
    print()                    # Adds an empty line after each row
