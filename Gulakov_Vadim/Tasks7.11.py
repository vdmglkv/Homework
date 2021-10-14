"""
Task 7.11

Implement a generator which will geterate Fibonacci numbers endlessly.
"""


def fib_generator():
    a = 0
    b = 1
    while True:
        yield b
        a, b = b, a + b


gen = fib_generator()

while True:
    print(next(gen))
