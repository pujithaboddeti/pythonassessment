class name():
    def __init__(self):
        self.__nameofst1='pujitha'
        self.__nameofst2='gayathri'
    def main(self):
        print('this is private class')
    def acess_private(self):
        print(self.__nameofst1)
        print(self.__nameofst2)
class roll(name):
    def twentyfive(self):
        self.rollOfSt=25
        print(self.rollOfSt)
        self.rollofSt2=35
        print(self.rollofSt2)
    def access_parent_class(self):
        try:
            print(self.__nameofst1)
            print(self.__nameofst2)
        except AttributeError:
            print('parent class cannot be accessed')
obj=roll()
obj.twentyfive()
obj.acess_private()
obj.access_parent_class()
obj.main()