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
    def eat(self):  
        print("Eating food...")

    def create_instance_and_call_non_abstract(self):
        obj = Dog()
        obj.sleep()  
        obj.eat()   

dog = Dog()
dog.create_instance_and_call_non_abstract()
