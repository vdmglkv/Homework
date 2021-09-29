"""Task 4.2
Implement custom dictionary that will memorize 10 latest changed keys. Using method "get_history" return this keys.
"""


class Dictionary:

    def __init__(self, dict_: dict):
        self.dict_ = dict_
        self.memory_keys = []

    def get(self):
        return self.dict_

    def set_value(self, key, value):

        self.dict_[key] = self.dict_.pop(*self.dict_.keys())
        self.dict_[key] = value

        self.memory_keys.append(key)

    def get_history(self):
        return self.memory_keys


b = Dictionary({'foo': 2})
b.set_value('bar', 4)
b.set_value('asd', 3)
print(b.get())
print(b.get_history())
