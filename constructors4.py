class MyClass:
    def __init__(self, arg1=None, arg2=None):
        if arg1 is None and arg2 is None:
            print("Default Constructor Called: No arguments")
        elif arg2 is None:
            print(f"One-Argument Constructor Called: Argument = {arg1}")
        else:
            print(f"Two-Argument Constructor Called: Argument1 = {arg1}, Argument2 = {arg2}")

def main():
    print("Instantiating MyClass with no arguments:")
    obj1 = MyClass()


    print("\nInstantiating MyClass with one argument:")
    obj2 = MyClass("Hello")
    print("\nInstantiating MyClass with two arguments:")
    obj3 = MyClass("Hello", "World")

if __name__ == "__main__":
    main()
