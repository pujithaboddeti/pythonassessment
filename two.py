class MyClass:
    def display(self, arg):
        if isinstance(arg, str):
            print(f"Method with string argument: {arg}")
        elif isinstance(arg, int):
            print(f"Method with integer argument: {arg}")
        else:
            print("Unsupported argument type")

def main():
    obj = MyClass()
    obj.display("Hello")
    obj.display(100)

if __name__ == "__main__":
    main()
