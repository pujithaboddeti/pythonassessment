class MyClass:
    def display(self, *args): 
        if len(args) == 1:
            print(f"Method with 1 argument: {args[0]}")
        elif len(args) == 2:
            print(f"Method with 2 arguments: {args[0]}, {args[1]}")
        else:
            print("Invalid number of arguments")

def main():
    obj = MyClass()
    obj.display("Hello")
    obj.display("Hello", "World")

if __name__ == "__main__":
    main()
