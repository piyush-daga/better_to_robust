from functools import total_ordering


@total_ordering
class User:
    def __init__(self, first_name: str, last_name: str, age: int) -> None:
        self.__first_name: str = first_name
        self.__last_name: str = last_name
        self.__age: int = age

    @property
    def first_name(self):
        return self.__first_name

    @property
    def last_name(self):
        return self.__last_name

    @property
    def age(self):
        return self.__age

    # User(first_name=Peter, last_name=Parker, age=21)
    def __repr__(self) -> str:
        return f'{self.__class__.__name__}(first_name={self.first_name}, last_name={self.last_name}, age={self.age})'

    def __eq__(self, __o: object) -> bool:
        if __o.__class__ is self.__class__:
            return (self.first_name, self.last_name, self.age) == (__o.first_name, __o.last_name, __o.age)
        raise NotImplementedError

    def __lt__(self, __o: object):
        if __o.__class__ is self.__class__:
            return self.age < __o.age
        raise NotImplementedError


tom = User('Tom', 'Holland', 25)
tom_clone = User('Tom', 'Holland', 25)
andrew = User('Andrew', 'Garfield', 38)

# # True
print(tom == tom_clone)
# # False
print(tom == andrew)
# # True True False True
print(tom < andrew, andrew > tom, tom >= andrew, tom <= andrew)
