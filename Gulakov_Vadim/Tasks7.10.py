"""
Task 7.10

Implement a generator which will generate odd numbers endlessly.
"""


def odd_gen():
    count = 1
    while True:
        yield count
        count += 2


gen = odd_gen()
while True:
    print(next(gen))
