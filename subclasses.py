class A:
    def printing(self):
        print('name')
class B(A):
    def printing(self):
        print('pujitha')
class C(B):
    def printing(self):
        print('gayathri')
o=C()
o.printing()