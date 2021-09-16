# Task 1.7
# Write a Python program to convert a given tuple of positive integers into an integer.
# Examples:
# Input: (1, 2, 3, 4)
# Output: 1234

nums = (1, 2, 3, 4)
print(int(''.join(tuple(map(str, nums)))))
