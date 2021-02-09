import random
lista= random.sample(range(100),10)
print(lista)
x=lista[0]
y=lista[0]
i=1
j=1

while i <=9:
    if x>=lista[i]:
        x=x
    else:
        x= lista[i]
    i=i+1
print(f'O maior número é {x}')
while j <=9:
    if y>=lista[j]:
        y=lista[j]
    else:
        y=y
    j=j+1
print(f'O menor número é {y}')

