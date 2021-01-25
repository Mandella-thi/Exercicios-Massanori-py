a= 1
b=1
num= int(input("Digite o número de Fibonacci que deseja"))
n=0
if num ==1:
    print(a)
elif num==2:
    print(b)
while n< (num-2):
    a,b =b, a+b
    print(a,b)
    n= n+1