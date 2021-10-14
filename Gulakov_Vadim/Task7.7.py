"""
Task 7.7

Implement your custom collection called MyNumberCollection. It should be able to contain only numbers. It should NOT
inherit any other collections. If user tries to add a string or any non numerical object there, exception TypeError
should be raised. Method init sholud be able to take either start,end,step arguments, where start - first number of
collection, end - last number of collection or some ordered iterable collection (see the example). Implement
following functionality:

    appending new element to the end of collection
    concatenating collections together using +
    when element is addressed by index(using []), user should get square of the addressed element.
    when iterated using cycle for, elements should be given normally
    user should be able to print whole collection as if it was list. Example:

"""


class MyNumberCollection:

    def __init__(self, start, end=None, step=None):

        self.number_list = []
        self.start = start
        self.end = end
        self.step = step
        self.index = -1

        if isinstance(start, int):
            for i in range(self.start, self.end, self.step):
                self.number_list.append(i)
            if self.number_list[-1] != self.end:
                self.number_list.append(self.end)
        else:
            for i in self.start:
                if isinstance(i, int):
                    self.number_list.append(i)
                else:
                    raise TypeError(f'Excepted int, got {type(i)}')

    def __repr__(self):

        return str(self.number_list)

    def __getitem__(self, index):

        return self.number_list[index]**2

    def __add__(self, other):

        self.temp = self.number_list.copy()
        for i in other:
            if isinstance(i, int):
                self.temp.append(i)
            else:
                raise TypeError(f'Excepted int, got {type(i)}')
        return self.temp

    def append(self, other):

        if isinstance(other, int):
            self.number_list.append(other)
        else:
            raise TypeError(f'{other} - is not a number!')

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < (len(self.number_list) - 1):
            self.index += 1
            return self.number_list[self.index]
        raise StopIteration
