n=int(input('Número: '))
for k in range(2,n):
    while n%k ==0:
        print(f'o k é {k}')
        print(k)
        n=n/k
        print(f' o novo n é {n}')