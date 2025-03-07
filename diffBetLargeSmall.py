def difference_between_large_and_small(l):
    maxx=l[0]
    minn=l[0]
    for i in l:
        if i>maxx:
            maxx=i
        else:
            minn=i
    print(f'max element is:{maxx}')
    print(f'min element is:{minn}')
    print(f'difference is:{maxx-minn}')
l=list(map(int,input().split()))
difference_between_large_and_small(l)
