d={1:'pavani',2:'gayathri',3:'pujitha',4:'saziya',5:'prasanna'}
update=input()
key=int(input('enter the key value to update'))
for i in d:
    if i==key:
        d[i]=update
print(d)