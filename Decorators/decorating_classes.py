def print_something(func):
    def wrapper_func(*args, **kwargs):
        print(f"We're running {func}")
        return func(*args, **kwargs)
    return wrapper_func

@print_something
class Example:
    def __init__(self, name):
        self.name = name

# example = Example("Robert")
# print(example)

from dataclasses import dataclass
from datetime import date

@dataclass
class Record:
    name: str
    artist: str
    release_date: date

record1 = Record("Metallica", "Metallica", date(1991, 10, 1))
record2 = Record("Metallica", "Metallica", date(1991, 10, 1))

print(record1.name)
print(record1.artist)
print(record1.release_date)
print(record1 == record2)
 