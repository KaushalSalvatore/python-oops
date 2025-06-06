'''
@property is used to control access to an attribute of a class — often called getter/setter behavior.
It allows encapsulation: exposing data like a public attribute but giving control like a method.

To hide internal implementation
To add validation or logic on getting/setting a variable
To make code clean and readable
'''

class Dog():
    def speak(self):
        return 'woafff !!!'

dog = Dog()
print(dog.speak())

def cat(self):
    return 'Meow !!!'

Dog.speak = cat

print(dog.speak())