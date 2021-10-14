"""
Task 7.5

Implement function for check that number is even and is greater than 2. Throw different exceptions for this errors.
Custom exceptions must be derived from custom base exception(not Base Exception class).
"""


class NotEvenError(BaseException):
    def __init__(self, message=None):
        self.msg = message

    def __str__(self):
        return repr(self.msg)


def is_even(number):
    if number > 2 and number % 2 == 0:
        return True
    return NotEvenError('Num isn\'t even')


