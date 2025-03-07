class Parent:

    def __init__(self):
        print("Parent class default constructor called.")

    def __init__(self, arg1=None):
        if arg1 is None:
            print("Parent class default constructor called.")
        else:
            print(f"Parent class constructor with argument called: {arg1}")


class Child(Parent):
   
    def __init__(self, arg1=None):
        super().__init__(arg1) 
        print("Child class constructor called.")
def main():
    print("Instantiating Child class with no arguments:")
    child1 = Child()

    print("\nInstantiating Child class with an argument:")
    child2 = Child("Hello from Child!")

if __name__ == "__main__":
    main()
