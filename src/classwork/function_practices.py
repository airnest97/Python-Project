def get_digit(number: int, position: int) -> int:
    """
    return digit at position in number, counting from right
    >>> get_digit(234, 0)
    4
    >>> get_digit(234, 2)
    2
    >>> "hello"
    'hello'
    """
    return number // (10 ** position) % 10


print(get_digit(35262193756583, 9))


