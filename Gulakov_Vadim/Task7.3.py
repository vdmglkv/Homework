"""
Task 7.3

Implement decorator with context manager support for writing execution time to log-file. See contextlib module.
"""

import logging
from time import time, sleep
from contextlib import ContextDecorator


class Loger(ContextDecorator):

    def __init__(self, file_name):
        logging.basicConfig(level=logging.INFO, filename=file_name, filemode='w')

    def __enter__(self):
        self.start_time = time()
        logging.info(f'Started: {self.start_time}')

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.end_time = time()
        logging.info(f'Stopped: {self.end_time}')
        logging.info(f'{self.end_time - self.start_time} seconds elapsed')


@Loger("test.txt")
def timed():
    sleep(3)


timed()
