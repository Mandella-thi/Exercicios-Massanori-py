# G. verbing
# Dada uma string, caso seu comprimento seja pelo menos 3,
# adiciona 'ing' no final
# Caso a string já termine em 'ing', acrescentará 'ly'.
def verbing(s):
  verbo=''
  if len(s)>=3:
    if s[-3:] == 'ing':
        verbo= s +'ly'
    else: verbo=s+ 'ing'
    return verbo

print(verbing('Thiago'))