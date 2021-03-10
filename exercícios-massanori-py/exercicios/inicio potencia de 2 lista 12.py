# L. inicio em potencia de 2
# Dado um número inteiro positivo n retorne a primeira potência de 2
# que tenha o início igual a n
# Exemplo: para n = 65 retornará 16 pois 2**16 = 65536
def inip2(n):
    k=0
    while True:
        pot= str(2**k)
        if pot.startswith((str(n))):
            return k
        k=k+1

print(inip2(7))