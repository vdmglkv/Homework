"""Task 4.5
Implement a decorator `remember_result` which remembers last result of function it decorates and prints it before next call.

```python
@remember_result
def sum_list(*args):
	result = ""
	for item in args:
		result += item
	print(f"Current result = '{result}'")
	return result

sum_list("a", "b")
"Last result = 'None'"
"Current result = 'ab'"
sum_list("abc", "cde")
"Last result = 'ab'"
"Current result = 'abccde'"
sum_list(3, 4, 5)
"Last result = 'abccde'"
"Current result = '12'"
```
"""
from functools import wraps


def remember_result(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        if not hasattr(wrapper, "last_result"):
            wrapper.last_result = None
        print(f"Last result = '{wrapper.last_result}'")
        wrapper.last_result = function(*args, **kwargs)
        return wrapper.last_result
    return wrapper


@remember_result
def sum_list(*args):
    result = sum(args)
    print(f"Current result = '{result}'")
    return result


sum_list(1, 2, 3)
sum_list(1, 2, 4)
sum_list(*[i for i in range(5)])
