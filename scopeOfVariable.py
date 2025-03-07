#local variable
def scope():
    s='pujitha'
    print(s)
scope()

#global variable
def scope(n):
    print(n)
    print(s)
s='pujitha'
scope(s)