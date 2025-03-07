l=list(map(int,input().split()))
val=int(input('enter ele to remove'))
if val in l:
    l.remove(val)
print(l)