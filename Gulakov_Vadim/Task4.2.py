"""Task 4.2 Write a function that check whether a string is a palindrome or not. Usage of any reversing functions is
prohibited. To check your implementation you can use strings from here.
"""

string = 'Pip'


def is_palindrome(s):
    s = s.lower()
    if s == s[::-1]:
        return True
    return False


print(is_palindrome(string))
