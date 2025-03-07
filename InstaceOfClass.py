class A:
    def name1(self):
        print('hello')
    def name2(self):
        print('namasthe')
    def name3(self):
        print('hanji')
class B(A):
    def classone(self):
        print('bca')
    def classtwo(self):
        print('bsc')
    def name3(self):
        print('electronics')
class C(B):
    def roll1(self):
        print('25')
    def roll2(self):
        print('35')
    def name3(self):
        print('90')
obj=C()
obj.name3()
