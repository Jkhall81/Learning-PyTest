def round6(num: float) -> int:
    """This function has a bug in it."""
    return int(num + 0.6)


def main():
    result = round6(3.5)
    return result


if __name__ == '__main__':
    main()


print(round6(4.5))
