def fatorial(x):
    num=1
    num2=1
    while num <=x:
        num2= num2*num
        num= num +1
    return num2


print(fatorial(4))