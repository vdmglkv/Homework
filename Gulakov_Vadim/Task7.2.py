"""
Task 7.2

Implement context manager for opening and working with file, including handling exceptions with @contextmanager
decorator.
"""

from contextlib import contextmanager


@contextmanager
def filemanager(file_name, file_mode):

    try:
        file = open(file_name, file_mode)
        yield file

    except Exception as e:
        print('caught:', e)

    finally:
        file.close()


with filemanager('test.txt', 'w') as source:
    print(f'Source: {source}')
