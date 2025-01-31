class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"This person is {self.name} and is {self.age} years old"


p1 = Person("John", 35)
print(p1)