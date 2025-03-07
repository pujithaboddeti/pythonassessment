class Parent:
    def __init__(self):  # Public constructor
        print("Parent class public constructor called.")

    def _protected_constructor(self):  # Protected constructor
        print("Parent class protected constructor called.")

    def __private_constructor(self):  # Private constructor
        print("Parent class private constructor called.")

class Child(Parent):
    def __init__(self):
        super().__init__()
        self._protected_constructor()
        try:
            self.__private_constructor()
        except AttributeError:
            print("Cannot access private constructor.")

def main():
    print("Instantiating Child class:")
    child = Child()

if __name__ == "__main__":
    main()
