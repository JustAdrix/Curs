from dataclasses import dataclass
from typing import List

@dataclass
class Person:
    name: str
    age: int

@dataclass
class Student(Person):
    university: str
    grades: List[float] # from typing import List


p = Person("Adrian", 37)
print(p)
s = Student("Valentin", 45, "Babes", [7.0, 8.3, 9.5])
print(s)

# O clasa de tip data class defineste automat functiile __init__, __repr__, __eq__