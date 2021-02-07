num= int(input("Digite o número"))
x=1
while x*(x+1)* (x+2) < num:
    x=x+1
print(x*(x+1) *(x+2)==num)