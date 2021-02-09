import random
lista1= random.sample(range(100),10)
lista2= random.sample(range(100), 10)
print(f'A primeira lista é{lista1}')
print(f'A segunda lista é {lista2}')
lista3=[]
n=0
while n<=9:
    lista3.append(lista1[n])
    lista3.append(lista2[n])
    n=n+1
print(f'A lista formada é {lista3}')