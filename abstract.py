from abc import ABC, abstractmethod

#abstract class
class AbstractDemo(ABC):
    #abstract method
    @abstractmethod
    def absFunc(self):
        None
class ConcreteClass(AbstractDemo):
    def absFunc(self):
        print("This is abstract function!!")
obj = ConcreteClass()
obj.absFunc()
