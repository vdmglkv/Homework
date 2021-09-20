"""Task 4.1
Implement a function which receives a string and replaces all " symbols with ' and vise versa.
"""

string = "Tes't' st'r'ing"


def string_replace(s):
    result = ""
    for char in s:
        if char == "'":
            result += '"'
        elif char == '"':
            result += "'"
        else:
            result += char
    return result


print(string_replace(string))
