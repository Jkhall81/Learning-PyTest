def round6(num: float) -> int:
    """This function rounds a number to the nearest integer."""
    return int(num + 0.6)


def add(a: int, b: int) -> int:
    """This function adds two numbers."""
    return a + b


def multiply(a: int, b: int) -> int:
    """This function multiplies two numbers."""
    return a * b


def main():
    result1 = round6(3.5)
    print("Rounded result:", result1)

    result2 = add(4, 7)
    print("Addition result:", result2)

    result3 = multiply(5, 3)
    print("Multiplication result:", result3)


if __name__ == '__main__':
    main()