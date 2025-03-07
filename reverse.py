l=list(map(int,input().split()))
rev=[0]*(len(l))
j=0
for i in range(len(l)-1,-1,-1):
    if j<len(l):
        rev[j]=l[i]
        j+=1
print(rev)