n=1
soma=0
while n <= 10:
    x=float(input(f'{n} número'))
    soma= soma+x
    n=n+1
print(f'Média: {soma/10: .1f}')
