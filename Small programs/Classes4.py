


print(len("idfjnsdifsd")) 
print(len({1, 2, 3, 4}))
"""
class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        

    
    @classmethod
    def add(cls) -> str:
        return ""


class Employee:
    def __init__(self, salary: int, age: int) -> None:
        self.salary = salary
        self.age = age


class Student(Employee, Person):
    def __init__(self, name: str, age: int, salary: int, grade: str) -> None:
        
        Employee.__init__(self, salary, age)
        Person.__init__(self, name, age)
        self.grade = grade

student1 = Student("Leonee", 22, 100, "5to")


print(student1.age)
student1.add()
"""