# K. conta 2
# Verifique quantas vezes o dígito 2 aparece entre 0 e n-1
# Exemplo: para n = 20 o dígito 2 aparece duas vezes entre 0 e 19
def conta2(n):
  p=''
  for k in range(n):
    p=p+str(k)

  return p.count('2')

print(conta2(21))