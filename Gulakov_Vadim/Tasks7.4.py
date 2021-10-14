"""
Task 7.4

Implement decorator for suppressing exceptions. If exception not occure write log to console.
"""
import functools


def catch_exceptions(f):
    @functools.wraps(f)
    def exceptions_handler(*args, **kwargs):
        flag = False
        try:
            return f(*args, **kwargs)
        except Exception:
            flag = True
        finally:
            if flag:
                print('Suppressing')
    return exceptions_handler()


@catch_exceptions
def exept():
    raise Exception('Exception executed!')


exept()