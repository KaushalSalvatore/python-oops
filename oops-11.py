'''
Abstraction : hiding the internal implementation and showing only the essential features to the user.
abstraction is typically implemented using abstract classes and methods via the abc module.

key Point :
1.To hide complex logic from the user
2.To enforce a blueprint for subclasses
3.To improve maintainability and security 
4.Abstract classes cannot be instantiated directly.
5.Any subclass must implement all abstract methods.
6.Useful when you want to define a contract or interface for subclasses.

'''

from abc import ABC,abstractmethod

class Payment(ABC):
    @abstractmethod
    def Pay(self,amount):
        pass


