from abc import ABC,abstractmethod
class name(ABC):
    @abstractmethod
    def pujitha(self):
        print('bca')
class rollNO(name):
    def pujitha(self):
        print('rollno 25')
obj=rollNO()
obj.pujitha()
