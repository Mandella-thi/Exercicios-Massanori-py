n1= int(input("digite o primeiro número"))
n2= int(input("Digite o segundo número"))
n3= int(input("Digite o terceiro número"))
if n1>= n2 and n1>=n3:
    print(f"O maior número é: {n1}")
    if n2>=n3:
        print(f"O menor número é {n3}")
    else:
        print(f'o menor número é {n2}')
elif n2>= n1 and n2>= n3 and n3>=n1:
    print(f"O maior número é {n2}")
    if n1>=n3:
        print(f'O menor número é {n3}')
    else:
        print(f'o menor número é {n1}')
elif n3>=n2 and n3>=n1:
    print(f"O maior número é {n3}")
    if n2>=n1:
        print(f'O menor número é {n1}')
    else:
        print(f'o menor número é {n2}')

