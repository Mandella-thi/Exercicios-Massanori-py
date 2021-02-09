import random
lista= random.sample(range(100),20)
print(lista)
par=[]
impar=[]
for n in lista:
    if n%2==0:
        par.append(n)
    elif n%2==1:
        impar.append(n)
print(f'a lista dos pares é: {par}')
print(f'a lista dos impares é: {impar}')