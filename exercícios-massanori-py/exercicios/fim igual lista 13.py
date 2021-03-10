# A. fim_igual
# Dada uma lista de strings, retorna o número de strings
# com tamanho >= 2 onde o primeiro e o último caracteres são iguais
# Exemplo: ['aba', 'xyz', 'aa', 'x', 'bbb'] retorna 3
def fim_igual(words):
  n=0
  for k in words:
      if k[0]==k[-1] and len(k)>=2:
          n=n +1
  return n

print(fim_igual(['aba','xyz','aa','x', 'bbb']))

