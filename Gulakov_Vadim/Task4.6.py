"""Task 4.6 Implement a function get_shortest_word(s: str) -> str which returns the longest word in the given string.
The word can contain any symbols except whitespaces ( , \n, \t and so on). If there are multiple longest words in
the string with a same length return the word that occures first. Example:

get_shortest_word('Python is simple and effective!')
'effective!'

get_shortest_word('Any pythonista like namespaces a lot.')
'pythonista'
"""

string = 'Python is simple and effective!'


def get_longest_word(s):
    return max(s.split(), key=lambda x: len(x))


print(get_longest_word(string))
