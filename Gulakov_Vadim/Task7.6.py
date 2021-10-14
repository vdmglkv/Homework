"""
Task 7.6

Create console program for proving Goldbach's conjecture. Program accepts number for input and print result. For
pressing 'q' program succesfully close. Use function from Task 5.5 for validating input, handle all exceptions and
print user friendly output.
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
