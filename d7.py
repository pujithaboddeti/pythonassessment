d={}
ex={}
n=int(input())
subN=int(input())
for i in range(n):
    key=int(input('enter main key:'))
    ex.clear()
    for i in range(subN):
        key1=int(input('enter sub key:'))
        value=input('enter value:')
        ex[key1]=value
    d[key]=ex
for i in d:
    print(i,end=' ')