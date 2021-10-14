"""
Task 7.9

Implement an iterator class EvenRange, which accepts start and end of the interval as an init arguments and gives
only even numbers during iteration. If user tries to iterate after it gave all possible numbers Out of numbers!
should be printed. Note: Do not use function range() at all
"""


class EvenRange:
    def __init__(self, start, end):
        self.current_num = start
        self.end = end
        self.flag = False

    def __iter__(self):
        return self

    def is_next(self):
        while True:
            self.current_num += 1
            if self.current_num % 2 != 0:
                continue
            else:
                break
        if self.current_num < self.end:
            return self.current_num
        raise StopIteration

    def __next__(self):
        while True:
            try:
                return self.is_next()
            except StopIteration:
                if not self.flag:
                    self.flag = True
                    return 'Out of numbers!'
                else:
                    raise StopIteration

