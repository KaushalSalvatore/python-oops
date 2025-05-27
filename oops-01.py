class Person:
    def __init__(self , name, age):
        self.name = name
        self.age = age
    
    def display_info(self):
        print(f'name :- {self.name} , age :- {self.age}')

person = Person('kaushal','28')

person.display_info()