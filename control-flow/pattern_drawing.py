# control-flow/pattern_drawing.py
# Drawing Patterns with Nested Loops
# Demonstrates the use of while loops and nested for loops.

# Prompt User for Pattern Size
size = int(input("Enter the size of the pattern: "))

# Draw the Pattern
row = 0
while row < size:
    for col in range(size):
        print("*", end="")  # Print stars side by side without newline
    print()  # Move to the next line after finishing one row
    row += 1
    