a=int(input("digite o maior número"))
b= int(input("Digite o menor número"))
while a%b != 0:
    a,b =b, a%b
    print(a, b)
print (f"O maior divisor comum é {b}")