a = "I am global variable!"


def enclosing_funcion():
    a = "I am variable from enclosed function!"

    def inner_function():
        global a
        a = "I am local variable!"
        print(a)

    return inner_function()
