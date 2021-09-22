""""### Task 4.4
Look through file `modules/legb.py`.

1) Find a way to call `inner_function` without moving it from inside of `enclosed_function`.

2.1) Modify ONE LINE in `inner_function` to make it print variable 'a' from global scope.

2.2) Modify ONE LINE in `inner_function` to make it print variable 'a' form enclosing function.
"""

a = "I am global variable!"


# 1) Find a way to call `inner_function` without moving it from inside of `enclosed_function`.
def enclosing_function_1():
    a = "I am variable from enclosed function!"

    def inner_function():
        a = "I am local variable!"
        print(a)
    return inner_function


# 2) Modify ONE LINE in inner_function to make it print variable 'a' from global scope.
def enclosing_function_2():
    a = "I am variable from enclosed function!"

    def inner_function():
        global a
        print(a)
    return inner_function


# 3) Modify ONE LINE in inner_function to make it print variable 'a' form enclosing function.
def enclosing_function_3():
    a = "I am variable from enclosed function!"

    def inner_function():
        nonlocal a
        print(a)
    return inner_function
