# J. zeros finais
# Verifique quantos zeros há no final de um número inteiro positivo
# Exemplo: 10010 tem 1 zero no fim e 908007000 possui três
def zf(n):
    n=str(n)[::-1]
    k=0
    while n[k]=='0':
        k=k+1
    return k

print(zf(9000))