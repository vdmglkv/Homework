"""Task 4.4 Implement a function split_by_index(s: str, indexes: List[int]) -> List[str] which splits the s string by
indexes specified in indexes. Wrong indexes must be ignored. Examples:

split_by_index("python is cool, isn't it?", [6, 8, 12, 13, 18])
["python", "is", "cool", ",", "isn't", "it?"]

split_by_index("no luck", [42])
["no luck"]
"""

string = "python is cool, isn't it?"
indexes = [6, 8, 12, 13, 18]


def split_by_index(s, ind):
    s = s.replace(' ', '')
    result = []
    start = 0
    for ind in indexes:
        result.append(s[start:ind])
        start = ind
    if s[ind:]:
        result.append(s[ind:])
    return result


print(split_by_index(string, indexes))
