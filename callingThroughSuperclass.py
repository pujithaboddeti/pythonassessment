class A:
    def method(self):
        print('welcome')
class B(A):
    def method(self):
        print('come')
class c(B):
    def method(self):
        print('honor')
obj=A()
obj.method