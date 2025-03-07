def remove_duplicates(l):
    new=[]
    for i in l:
        if i in new:
            pass
        else:
            new.append(i)
    return new
l=list(map(int,input().split()))
print(remove_duplicates(l))