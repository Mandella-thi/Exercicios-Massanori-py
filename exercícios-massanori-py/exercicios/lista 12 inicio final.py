# I. inicio_final
# Divida cada string em dois pedaços.
# Se a string tiver um número ímpar de caracteres
# o primeiro pedaço terá um caracter a mais,
# Exemplo: 'abcde', divide-se em 'abc' e 'de'.
# Dadas 2 strings, a e b, retorna a string
#  a-inicio + b-inicio + a-final + b-final
def inicio_final(a, b):
  n=a[0: len(a)//2]
  m=a[(len(a)//2):]
  j=b[0:len(b)//2]
  p = b[(len(b) // 2):]
  return n +j+m+p
print(inicio_final('thiago','leopoldo'))