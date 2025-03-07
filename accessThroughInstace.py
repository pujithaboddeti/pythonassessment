class accessThroughInstance():
    num=int(input())
    def __init__(self):
        if self.num%2==0:
            print(f'even number')
        else:
            print('odd number')
obj=accessThroughInstance()