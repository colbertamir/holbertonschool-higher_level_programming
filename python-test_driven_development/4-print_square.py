#!/usr/bin/python3
def print_square(size):
    

    """Prints a square of '#' characters.

    Args:
        size (int): The height and width of the square.

    Raises:
        TypeError: If `size` is not an integer.
        ValueError: If `size` is less than zero.

    """

if not isinstance(size, int):
    raise TypeError("size must be an integer")

if size < 0:
    raise ValueError("size must be >= 0")

if size > 0:
    for _ in range(size):
        print("#" * size)

if __name__ == "__main__":
    print_square(1)
    print_square(4)
    print_square(10)
    print_square(0)
