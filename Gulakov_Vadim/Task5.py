# Task 1.5
# Write a Python program to sort a dictionary by key.

dictionary = {1: 1, 3: 3, 2: 2, 7: 7, 4: 4}
print(sorted(dictionary.items(), key=lambda x: x[0]))
