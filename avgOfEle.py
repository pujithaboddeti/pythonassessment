n=int(input())
l=list(map(int,input().split()))
s=0
for i in l:
    s+=i
avg=s//n
print(avg)