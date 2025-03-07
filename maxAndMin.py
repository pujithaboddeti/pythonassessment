l=list(map(int,input().split()))
maxx=l[0]
minn=l[0]
for i in range(len(l)):
    if maxx<l[i]:
        maxx=l[i]
print(f'maximum value is:{maxx}')
for i in range(len(l)):
    if minn>l[i]:
        minn=l[i]
print(f'minimum value is:{minn}')