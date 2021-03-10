# H. not_bad
# Dada uma string, procura a primeira ocorrência de 'not' e 'bad'
# Se 'bad' aparece depois de 'not' troca 'not' ... 'bad' por 'good'
# Assim 'This dinner is not that bad!' retorna 'This dinner is good!'
def not_bad(s):
  n=s.find('not')
  b=s.find('bad')
  if b>n:
    s=s[:n]+ 'good'+ s[b+3:]
    return s
print(not_bad('this dinner is not that bad'))