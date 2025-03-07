def second_largest(l):
    maxx=l[0]
    sec=l[0]
    for i in l:
        if maxx<i:
            sec=maxx
            maxx=i
        elif sec<i and i!=maxx:
            sec=i
    print(maxx)
    print(sec)
l=list(map(int,input().split()))
second_largest(l)
