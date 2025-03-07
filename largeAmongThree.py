num1=int(input())
num2=int(input())
num3=int(input())
if num1>num2 and num1>num3:
    print(f'{num1} is greater')
elif num2>num3:
    print(f'{num2} is greater')
else:
    print(f'{num3} is greater')