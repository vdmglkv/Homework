"""Task 4.5
A singleton is a class that allows only a single instance of itself to be created and gives access to
that created instance. Implement singleton logic inside your custom class using a method to initialize class
instance.
"""


def singleton(class_):
    instances = {}

    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]

    return getinstance


@singleton
class Person:
    def __init__(self, name):
        self.name = name

    def get(self):
        return self.insa


a = Person('Vadim')
b = Person('Vova')

print(a is b)
