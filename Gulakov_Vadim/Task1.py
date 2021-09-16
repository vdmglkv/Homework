# Task 1.1
# Write a Python program to calculate the length of a string without using the `len` function.


s = '12345678907878'


def length(string):
    count = 0
    for _ in string:
        count += 1
    return count


# print(length(s) == len(s))
print(length(s))
