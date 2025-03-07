l=list(map(int,input().split()))
val=int(input('enter a element'))
pos=int(input('enter a position'))
new=[0]*(len(l)+1)
# l.insert(pos,val)
# print(l)
for i in range(pos+1):
    new[i]=l[i]
new[pos]=val
for i in range(pos,len(l)):
    new[i+1]=l[i]
print(new)