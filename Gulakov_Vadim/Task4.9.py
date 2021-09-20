"""Task 4.9
Implement a bunch of functions which receive a changeable number of strings and return next parameters:

characters that appear in all strings

characters that appear in at least one string

characters that appear at least in two strings

characters of alphabet, that were not used in any string

Note: use string.ascii_lowercase for list of alphabet letters

test_strings = ["hello", "world", "python", ]
print(test_1_1(*strings))
{'o'}
print(test_1_2(*strings))
{'d', 'e', 'h', 'l', 'n', 'o', 'p', 'r', 't', 'w', 'y'}
print(test_1_3(*strings))
{'h', 'l', 'o'}
print(test_1_4(*strings))
{'a', 'b', 'c', 'f', 'g', 'i', 'j', 'k', 'm', 'q', 's', 'u', 'v', 'x', 'z'}"""""

import string


def test_1_1(*lst):

    num = len(lst)
    chars = {}
    for word in lst:
        for char in set(word.lower()):
            chars[char] = chars.get(char, 0) + 1
    return sorted({k for k, v in chars.items() if v == num})


def test_1_3(*lst):

    chars = {}
    for word in lst:
        for char in set(word.lower()):
            chars[char] = chars.get(char, 0) + 1
    return sorted({k for k, v in chars.items() if v > 1})


def test_1_2(*lst):
    return sorted({char for word in lst for char in word.lower()})


def test_1_4(*lst):
    return sorted(set(string.ascii_lowercase) - {char for word in lst for char in word.lower()})


test_strings = ["hello", "world", "python", ]
print(test_1_1(*test_strings))
print(test_1_2(*test_strings))
print(test_1_3(*test_strings))
print(test_1_4(*test_strings))
