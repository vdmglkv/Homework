"""Task 4.3 File `data/students.csv` stores information about students in [CSV](
https://en.wikipedia.org/wiki/Comma-separated_values) format. This file contains the student’s names,
age and average mark. 1) Implement a function which receives file path and returns names of top performer students
```python def get_top_performers(file_path, number_of_top_students=5): pass

print(get_top_performers("students.csv"))
['Teresa Jones', 'Richard Snider', 'Jessica Dubose', 'Heather Garcia', 'Joseph Head']
```

2) Implement a function which receives the file path with srudents info and writes CSV student information to the
new file in descending order of age. Result: ``` student name,age,average mark Verdell Crawford,30,8.86 Brenda
Silva,30,7.53 ... Lindsey Cummings,18,6.88 Raymond Soileau,18,7.27 ```
"""

import csv
path = 'data/students.csv'
path_out = 'data/students_sort_by_age.csv'


def get_top_performers(filepath, number_of_top_students=5):

    with open(filepath) as file:
        reader = csv.reader(file, delimiter=",")
        next(reader)
        return [student[0] for student in sorted(reader, key=lambda x: float(x[2]), reverse=True)[:number_of_top_students]]


def sort_age(unsorted_filepath, sorted_filepath):

    with open(unsorted_filepath, newline="") as unsorted_file, open(sorted_filepath, "w", newline="") as sorted_file:
        reader = csv.reader(unsorted_file, delimiter=",")
        writer = csv.writer(sorted_file, delimiter=",")

        writer.writerow(next(reader))
        for row in sorted(reader, key=lambda student: int(student[1]), reverse=True):
            writer.writerow(row)


print(get_top_performers(path))
print(sort_age(path, path_out))
