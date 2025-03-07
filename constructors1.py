class Person:
    def __init__(self, name, age, city): 
        self.name = name
        self.age = age
        self.city = city

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, City: {self.city}")

def main():
    person1 = Person("Alice", 25, "New York")  
    person2 = Person("Bob", 30, "Los Angeles")  

    person1.display_info()  
    person2.display_info()  

if __name__ == "__main__":
    main()
