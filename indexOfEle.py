l=list(map(int,input().split()))
ele=int(input("enter element"))
for i in range(len(l)):
    if l[i]==ele:
        print(f'index of element is:{i}')