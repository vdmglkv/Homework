"""
Task 7.1
Implement class-based context manager for opening and working with file, including handling exceptions. Do not use
'with open()'. Pass filename and mode via constructor.

"""


class FileManager:

    def __init__(self, file_name, file_mode):
        self._file_name = file_name
        self._file_mode = file_mode

    def __enter__(self):
        self._file = open(self._file_name, self._file_mode)
        return self._file

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self._file.close()


with FileManager('test.txt', 'w') as f:
    f.write('I love Python!')
