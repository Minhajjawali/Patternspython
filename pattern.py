# patterns.py

def star_pattern(n):
    """
    Prints a right-angled triangle star pattern.

    Args:
        n (int): The number of rows in the pattern.
    """
    print("\n--- 1. Star Pattern ---")
    for i in range(1, n + 1):
        print("*" * i)
 def half_pyramid_number_pattern(n):
    """
    Prints a right-angled triangle number pattern.

    Args:
        n (int): The number of rows in the pattern.
    """
    print("\n--- 3. Half Pyramid Number Pattern ---")
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end="")
        print()

def inverted_pyramid_number_pattern(n):
    """
    Prints an inverted right-angled triangle number pattern.

    Args:
        n (int): The number of rows in the pattern.
    """
    print("\n--- 4. Inverted Pyramid Number Pattern ---")
    for i in range(n, 0, -1):
        for j in range(1, i + 1):
            print(j, end="")
        print()
