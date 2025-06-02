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
