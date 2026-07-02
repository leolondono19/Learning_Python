from abc import ABC, abstractmethod

class Animals(ABC):
    def __init__(self, name: str, breed: str) -> None:
        self.name = name
        self.breed = breed
    
    @abstractmethod
    def eat(self) -> None:
        print("I'm eating")

class Dog(Animals):
    def __init__(self, name: str, breed: str, color: str) -> None:
        super().__init__(name, breed)
        self.color = color
    
    def bark(self) -> None:
        print("waf")



dog1 = Animals()
dog1.eat()
dog1.bark()


