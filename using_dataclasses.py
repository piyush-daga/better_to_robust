from dataclasses import dataclass, asdict, astuple

@dataclass(order=True)
class User:
    age: int
    first_name: str
    last_name: str
    hometown: str = ""


tom = User(25, 'Tom', 'Holland')
tom_clone = User(25, 'Tom', 'Holland')
andrew = User(38, 'Andrew', 'Garfield')

# True
print(tom == tom_clone)
# False
print(tom == andrew)
# True True False True
print(tom < andrew, andrew > tom, tom >= andrew, tom <= andrew)

# {'age': 25, 'first_name': 'Tom', 'last_name': 'Holland'}
print(asdict(tom))
# (25, 'Tom', 'Holland')
print(astuple(tom))
