# importing cs50 module
from cs50 import get_int

# taking user input
while True:
    height = get_int("Height: ")
    if height > 0 and height < 9:
        break

# printing answer
for i in range(0, height):
    print(" " * (height - (i + 1)), end="")
    print("#" * (i + 1), end="")
    print("  ", end="")
    print("#" * (i + 1))
