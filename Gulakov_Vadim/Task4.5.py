"""Task 4.5
Implement a function get_digits(num: int) -> Tuple[int] which returns a tuple of a given integer's digits. Example:

split_by_index(87178291199)
(8, 7, 1, 7, 8, 2, 9, 1, 1, 9, 9)
"""

num = 87178291199


def getdigits(number):
    res = []
    while number != 0:
        last_digit = number % 10
        res.append(last_digit)
        number //= 10
    return tuple(res[::-1])


print(getdigits(num))
