# patterns.py
# function of star function
def star_pattern(n):
    """
    Prints a right-angled triangle star pattern.

    Args:
        n (int): The number of rows in the pattern.
    """
    print("\n--- 1. Star Pattern ---")
    for i in range(1, n + 1):
        print("*" * i)

        def character_pattern(n):
    """
    Prints a right-angled triangle character pattern (A, AB, ABC, ...).

    Args:
        n (int): The number of rows in the pattern.
    """
    print("\n--- 5. Character Pattern ---")
    char_code = ord('A')
    for i in range(1, n + 1):
        for _ in range(i):
            print(chr(char_code), end="")
            char_code += 1
        print()
#function of inverted character pattern
def inverted_character_pattern(n):
    """
    Prints an inverted right-angled triangle character pattern.

    Args:
        n (int): The number of rows in the pattern.
    """
    print("\n--- 6. Inverted Character Pattern ---")
    start_char_code = ord('A')
    for i in range(n, 0, -1):
        current_char_code = start_char_code
        for _ in range(i):
            print(chr(current_char_code), end="")
            current_char_code += 1
        start_char_code = current_char_code
        print()

def hollow_rectangle(rows, cols):
    """
    Prints a hollow rectangle pattern of stars.

    Args:
        rows (int): The number of rows in the rectangle.
        cols (int): The number of columns in the rectangle.
    """
    print("\n--- 7. Hollow Rectangle Pattern ---")
    for i in range(rows):
        for j in range(cols):
            if i == 0 or i == rows - 1 or j == 0 or j == cols - 1:
                print("*", end="")
            else:
                print(" ", end="")
        print()

def inverted_rotated_half_pyramid(rows):
    """
    Prints an inverted and rotated right-angled triangle star pattern.

    Args:
        rows (int): The number of rows in the pattern.
    """
    print("\n--- 8. Inverted and Rotated Half Pyramid ---")
    for i in range(1, rows + 1):
        print(" " * (rows - i) + "*" * i)

def inverted_half_pyramid_number(n):
    """
    Prints an inverted right-angled triangle number pattern (numbers decrease in each row).

    Args:
        n (int): The number of rows in the pattern.
    """
    print("\n--- 9. Inverted Half Pyramid Number Pattern ---")
    for i in range(n, 0, -1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

def floyds_triangle(n):
    """
    Prints Floyd's triangle number pattern.

    Args:
        n (int): The number of rows in the pattern.
    """
    print("\n--- 10. Floyd's Triangle ---")
    counter = 1
    for i in range(1, n + 1):
        for _ in range(i):
            print(counter, end=" ")
            counter += 1
        print()

def zero_one_triangle(n):
    """
    Prints a 0-1 triangle pattern.

    Args:
        n (int): The number of rows in the pattern.
    """
    print("\n--- 11. 0-1 Triangle Pattern ---")
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            if (i + j) % 2 == 0:
                print("1", end="")
            else:
                print("0", end="")
        print()

def butterfly_pattern(n):
    """
    Prints a butterfly pattern of stars.

    Args:
        n (int): The number of rows in the upper half (total height is 2*n).
    """
    print("\n--- 12. Butterfly Pattern ---")
    # Upper half
    for i in range(1, n + 1):
        print("*" * i + " " * (2 * (n - i)) + "*" * i)
    # Lower half
    for i in range(n, 0, -1):
        print("*" * i + " " * (2 * (n - i)) + "*" * i)

def solid_rhombus(n):
    """
    Prints a solid rhombus pattern of stars.

    Args:
        n (int): The number of rows (and width) of the rhombus.
    """
    print("\n--- 13. Solid Rhombus Pattern ---")
    for i in range(1, n + 1):
        print(" " * (n - i) + "*" * n)

def hollow_rhombus(n):
    """
    Prints a hollow rhombus pattern of stars.

    Args:
        n (int): The number of rows (and width) of the rhombus.
    """
    print("\n--- 14. Hollow Rhombus Pattern ---")
    for i in range(1, n + 1):
        print(" " * (n - i), end="")
        for j in range(1, n + 1):
            if i == 1 or i == n or j == 1 or j == n:
                print("*", end="")
            else:
                print(" ", end="")
        print()

def diamond_pattern(n):
    """
    Prints a diamond pattern of stars.

    Args:
        n (int): The number of rows in the upper half (total height is 2*n - 1).
    """
    print("\n--- 15. Diamond Pattern ---")
    # Upper half
    for i in range(1, n + 1):
        print(" " * (n - i) + "*" * (2 * i - 1))
    # Lower half
    for i in range(n - 1, 0, -1):
        print(" " * (n - i) + "*" * (2 * i - 1))

def advanced_star_pattern(n):
    """
    Prints a more complex star pattern.

    Args:
        n (int): Determines the size and complexity of the pattern.
    """
    print("\n--- 16. Advanced Star Pattern ---")
    for i in range(1, 2 * n):
        if i <= n:
            print("*" * i + " " * (2 * (n - i)) + "*" * i)
        else:
            print("*" * (2 * n - i) + " " * (2 * (i - n)) + "*" * (2 * n - i))

def another_number_pattern(n):
    """
    Prints another interesting number pattern.

    Args:
        n (int): The number of rows.
    """
    print("\n--- 17. Another Number Pattern ---")
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(i, end=" ")
        print()

def triangular_star_pattern(n):
    """
    Prints a slightly different triangular star pattern.

    Args:
        n (int): The number of rows.
    """
    print("\n--- 18. Triangular Star Pattern ---")
    for i in range(n):
        print("* " * (i + 1))

def decreasing_number_triangle(n):
    """
    Prints a triangle with decreasing numbers in each row.

    Args:
        n (int): The number of rows.
    """
    print("\n--- 19. Decreasing Number Triangle ---")
    for i in range(n, 0, -1):
        for j in range(1, i + 1):
            print(i, end=" ")
        print()

def right_arrow_pattern(n):
    """
    Prints a right arrow pattern of stars.

    Args:
        n (int): Determines the size of the arrow.
    """
    print("\n--- 20. Right Arrow Pattern ---")
    for i in range(n):
        if i < (n + 1) // 2:
            print(" " * i + "*" * ((n + 1) // 2))
        else:
            print(" " * (n - 1 - i) + "*" * ((n + 1) // 2))

def left_arrow_pattern(n):
    """
    Prints a left arrow pattern of stars.

    Args:
        n (int): Determines the size of the arrow.
    """
    print("\n--- 21. Left Arrow Pattern ---")
    for i in range(n):
        if i < (n + 1) // 2:
            print("*" * ((n + 1) // 2) + " " * i)
        else:
            print("*" * ((n + 1) // 2) + " " * (n - 1 - i))

def increasing_decreasing_triangle(n):
    """
    Prints a triangle with increasing numbers up to the middle and then decreasing.

    Args:
        n (int): The number of rows.
    """
    print("\n--- 22. Increasing Decreasing Triangle ---")
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        for k in range(i - 1, 0, -1):
            print(k, end=" ")
        print()

def reverse_increasing_triangle(n):
    """
    Prints a triangle with increasing numbers in reverse order in each row.

    Args:
        n (int): The number of rows.
    """
    print("\n--- 23. Reverse Increasing Triangle ---")
    for i in range(1, n + 1):
        for j in range(i, 0, -1):
            print(j, end=" ")
        print()

def sandglass_pattern(n):
    """
    Prints a sandglass pattern of stars.

    Args:
        n (int): Determines the size of the sandglass.
    """
    print("\n--- 24. Sandglass Pattern ---")
    # Upper part
    for i in range(n, 0, -1):
        print(" " * (n - i) + "*" * (2 * i - 1))
    # Lower part
    for i in range(2, n + 1):
        print(" " * (n - i) + "*" * (2 * i - 1))

def increasing_alphabet_triangle(n):
    """
    Prints a triangle with increasing alphabets in each row.

    Args:
        n (int): The number of rows.
    """
    print("\n--- 25. Increasing Alphabet Triangle ---")
    for i in range(n):
        start_char = ord('A')
        for j in range(i + 1):
            print(chr(start_char + j), end="")
        print()

def reverse_alphabet_triangle(n):
    """
    Prints a triangle with decreasing alphabets in each row.

    Args:
        n (int): The number of rows.
    """
    print("\n--- 26. Reverse Alphabet Triangle ---")
    for i in range(n):
        start_char = ord('A') + i
        for j in range(i + 1):
            print(chr(start_char - j), end="")
        print()

def number_crown_pattern(n):
    """
    Prints a number crown pattern.

    Args:
        n (int): Determines the size of the crown.
    """
    print("\n--- 27. Number Crown Pattern ---")
    for i in range(1, n + 1):
        print(str(i) + " " * (2 * (n - i) - 1) + (str(n) if i < n else str(i)))

def hollow_diamond(n):
    """
    Prints a hollow diamond pattern.

    Args:
        n (int): Determines the size of the diamond.
    """
    print("\n--- 28. Hollow Diamond ---")
    for i in range(n):
        spaces = abs(n // 2 - i)
        stars = n - 2 * spaces
        if stars > 0:
            print(" " * spaces + "*" + " " * (stars - 2) + ("*" if stars > 1 else ""))
        else:
            print(" " * n + "*") # Handle single middle row for odd n

def main():
    num_rows = 5 # You can change this value to adjust the size of the patterns

    star_pattern(num_rows)
    inverted_star_pattern(num_rows)
    half_pyramid_number_pattern(num_rows)
    inverted_pyramid_number_pattern(num_rows)
    character_pattern(num_rows)
    inverted_character_pattern(num_rows)

    hollow_rectangle(num_rows, 8) # Adjust columns as needed
    inverted_rotated_half_pyramid(num_rows)
    inverted_half_pyramid_number(num_rows)
    floyds_triangle(num_rows)
    zero_one_triangle(num_rows)
    butterfly_pattern(num_rows)
    solid_rhombus(num_rows)
    hollow_rhombus(num_rows)
    diamond_pattern(num_rows)

    advanced_star_pattern(num_rows)
    another_number_pattern(num_rows)
    triangular_star_pattern(num_rows)
    decreasing_number_triangle(num_rows)
    right_arrow_pattern(num_rows * 2 - 1) # Adjust size for arrow
    left_arrow_pattern(num_rows * 2 - 1)  # Adjust size for arrow
    increasing_decreasing_triangle(num_rows)
    reverse_increasing_triangle(num_rows)
    sandglass_pattern(num_rows)
    increasing_alphabet_triangle(num_rows)
    reverse_alphabet_triangle(num_rows)
    number_crown_pattern(num_rows)
    hollow_diamond(num_rows * 2 - 1) # Adjust size for diamond

    # Adding more similar patterns to reach around 500 lines

    def right_half_diamond(n):
        print("\n--- Right Half Diamond ---")
        for i in range(n):
            print("*" * (i + 1))
        for i in range(n - 2, -1, -1):
            print("*" * (i + 1))

    def left_half_diamond(n):
        print("\n--- Left Half Diamond ---")
        for i in range(n):
            print(" " * (n - 1 - i) + "*" * (i + 1))
        for i in range(n - 2, -1, -1):
            print(" " * (n - 1 - i) + "*" * (i + 1))

    def pascal_triangle_pattern(n):
        print("\n--- Pascal's Triangle Pattern (Basic) ---")
        for i in range(n):
            for j in range(n - i - 1):
                print(" ", end="")
            for j in range(i + 1):
                print("* ", end="")
            print()

    def binary_triangle(n):
        print("\n--- Binary Triangle ---")
        for i in range(1, n + 1):
            for j in range(1, i + 1):
                print((i + j) % 2, end="")
            print()

    def continuous_alphabet_pyramid(n):
        print("\n--- Continuous Alphabet Pyramid ---")
        char_code = ord('A')
        for i in range(1, n +
