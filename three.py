class MyClass:
    def display(self, arg1, arg2=None):
        if arg2 is None:
            print(f"Method with 1 argument: {arg1}")
        else:
            print(f"Method with 2 arguments: {arg1}, {arg2}")

def main():
    obj = MyClass()

    obj.display("Hello")
    obj.display("Hello", "World")

if __name__ == "__main__":
    main()
