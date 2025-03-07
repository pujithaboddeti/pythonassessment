from abc import ABC, abstractmethod 

class Animal(ABC):
    @abstractmethod
    def make_sound(self):  
        pass
    def sleep(self): 
        print("Sleeping...")
class Dog(Animal):
    def make_sound(self):
        print("Bark! Bark!")
dog = Dog()
dog.sleep()
dog.make_sound()  