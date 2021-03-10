# B. x_antes
# Dada uma lista de strings retorna uma lista onde
# todos os elementos que começam com x ficam sorteados antes
# Ex.: ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] retorna
# ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
# Dica: monte duas listas separadas e junte-as no final
def x_antes(words):
  n=[]
  outros=[]
  for k in words:
        if k[0]=='x':
          n.append(k)
        else:
            outros.append(k)

  return sorted(n)+sorted(outros)

print(x_antes(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']))