"""Task 4.2
Implement a function which search for most common words in the file.
Use `data/lorem_ipsum.txt` file as a example.

```python
def most_common_words(filepath, number_of_words=3):
    pass

print(most_common_words('lorem_ipsum.txt'))
['donec', 'etiam', 'aliquam']
```

> NOTE: Remember about dots, commas, capital letters etc.
"""
from collections import Counter
path = 'data/lorem_ipsum.txt'


def most_common_words(filepath, number_of_words=3):
    res = []
    with open(filepath, 'r') as file:
        common_word = dict(Counter(file.read().lower().replace('.', '').replace(',', '').split()))
        common_word = sorted(common_word.items(), key=lambda x: x[1], reverse=True)
        for pair in common_word[:number_of_words]:
            res.append(pair[0])
    return res


print(most_common_words(path))
