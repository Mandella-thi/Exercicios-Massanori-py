cont =0
soma=0
while True:
    x=int(input('n (zero sai) : '))
    if x== 0:
        break
    soma =soma +x
    cont= cont +1
print(f'Media: {soma/cont}')