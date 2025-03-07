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
    def create_instance_and_call(self):
        obj = Dog() 
        obj.make_sound()  
        obj.sleep() 
dog = Dog()
dog.create_instance_and_call()
