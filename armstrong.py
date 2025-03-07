n=int(input())
t=n
s=0
while n!=0:
    r=n%10
    s+=r*r*r
    n=n//10
if s==t:
    print('armstrong')
else:
    print('not an armstrong')