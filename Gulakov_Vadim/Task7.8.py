"""
Task 7.8

Implement your custom iterator class called MySquareIterator which gives squares of elements of collection it
iterates through. Example:
"""


class MySquareIterator:

    def __init__(self, elements):
        self.index = -1
        self.elements = elements

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < (len(self.elements) - 1):
            self.index += 1
            return (self.elements[self.index]) ** 2
        raise StopIteration
