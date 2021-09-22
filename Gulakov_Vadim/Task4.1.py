"""Task 4.1 Open file `data/unsorted_names.txt` in data folder. Sort the names and write them to a new file called
`sorted_names.txt`. Each name should start with a new line as in the following example:

```
Adele
Adrienne
...
Willodean
Xavier
```
"""

with open("data/unsorted_names.txt", 'r') as file:
    data = sorted(file.readlines())

with open("sorted_names.txt", 'w') as file:
    for inf in data:
        file.write(inf)

