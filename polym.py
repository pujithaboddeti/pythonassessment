class A():
    def __init__(self):
        super().__init__()
        self.c=9
class B(A):
    def __init__(self):
        super().__init__()
        self.c=40
class C(B):
    def __init__(self):
        super().__init__()
        self.c=10
obj1=A()
print(obj1.c)
obj2=B()
print(obj2.c)
obj3=C()
print(obj3.c)
