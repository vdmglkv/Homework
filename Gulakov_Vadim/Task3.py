# Task 1.3 Write a Python program that accepts a comma separated sequence of words as input and prints the unique
# words in sorted form. Examples: ``` Input: ['red', 'white', 'black', 'red', 'green', 'black'] Output: ['black',
# 'green', 'red', 'white', 'red']

seq = ['red', 'white', 'black', 'red', 'green', 'black']
# seq = input().split()
print(sorted(set(seq)))
