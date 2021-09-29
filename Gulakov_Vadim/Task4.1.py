"""Task 4.1 Implement a Counter class which optionally accepts the start value and the counter stop value. If the start value is not specified the counter should begin with 0. If the stop value is not specified it should be counting up infinitely. If the counter reaches the stop value, print "Maximal value is reached."

Implement to methods: "increment" and "get"

    If you are familiar with Exception rising use it to display the "Maximal value is reached." message.

"""


class Counter:

    def __init__(self, start: int = 0, end: int = None):
        if end is not None and start > end:
            raise ValueError('Start value should be smaller than end value!')

        self.start = start
        self.end = end

    def increment(self):
        self.start += 1

        if self.start == self.end:
            raise StopIteration('Maximal value is reached.')

    def get(self):
        return self.start


a = Counter()
