l=list(map(int,input().split()))
d={}
for i in l:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
new=[]
for i in d:
    if d[i]==1:
        new.append(i)
print(new)