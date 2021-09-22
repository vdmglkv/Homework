"""Task 4.6 Implement a function get_shortest_word(s: str) -> str which returns the longest word in the given string.
The word can contain any symbols except whitespaces ( , \n, \t and so on). If there are multiple longest words in
the string with a same length return the word that occures first. Example:

get_shortest_word('Python is simple and effective!')
'effective!'

get_shortest_word('Any pythonista like namespaces a lot.')
'pythonista'
"""
from functools import wraps


def call_once(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        if not hasattr(wrapper, "first_result"):
            wrapper.first_result = function(*args, **kwargs)
        return wrapper.first_result
    return wrapper


@call_once
def sum_of_numbers(a, b):
    return a + b


print(sum_of_numbers(1, 1))
print(sum_of_numbers(12123, 123123))
print(sum_of_numbers(100, 100))
