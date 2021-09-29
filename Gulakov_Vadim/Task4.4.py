"""" Task 4.4
    Create hierarchy out of birds. Implement 4 classes:

    class Bird with an attribute name and methods fly and walk. class FlyingBird with attributes name, ration,
    and with the same methods. ration must have default value. Implement the method eat which will describe its
    typical ration. class NonFlyingBird with same characteristics but which obviously without attribute fly. Add same
    "eat" method but with other implementation regarding the swimming bird tastes. class SuperBird which can do all
    of it: walk, fly, swim and eat. But be careful which "eat" method you inherit.

Implement str() function call for each class.
"""


class Bird:

    def __init__(self, name: str) -> None:
        self.name = name

    def fly(self):
        print(f'{self.name} can fly!')

    def walk(self):
        print(f'{self.name} can walk!')

    def __str__(self):
        return f'{self.name} can walk and fly.'


class FlyingBird(Bird):
    def __init__(self, name: str, ration: str = 'grass seeds') -> None:
        super().__init__(name)
        self.ration = ration

    def eat(self):
        print(f'{self.name} can eat {self.ration}')

    def __str__(self):
        return f'{self.name} can walk and fly.'


class NonFlyingBird(Bird):
    def __init__(self, name: str, ration: str = 'fish') -> None:
        super().__init__(name)
        self.ration = ration

    def fly(self):
        raise AttributeError('NonFlyingBird object has no attribute \'fly\'')

    def swim(self):
        print(f'{self.name} can swim!')

    def eat(self):
        print(f'{self.name} can eat {self.ration}')

    def __str__(self):
        return f'{self.name} can swim and walk.'


class SuperBird(FlyingBird, NonFlyingBird):

    def __init__(self, name: str, ration: str = 'fish') -> None:
        super().__init__(name, ration)

    def __str__(self):
        return f'{self.name} can walk, fly and swim.'

    def fly(self):
        return super(NonFlyingBird, self).fly()
