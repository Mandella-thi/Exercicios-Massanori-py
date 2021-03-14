# E. Cripto desafio!!
# Dada uma frase, você deve retirar todas as letras repetidas das palavras
# e ordenar as letras que sobraram
# Exemplo: 'ana e mariana gostam de banana' vira 'an e aimnr agmost de abn'
# Dicas: tente transformar cada palavra em um conjunto,
# depois tente ordenar as letras e montar uma string com o resultado.
# Utilize listas auxiliares se facilitar
def cripto(frase):
  return''.join([''.join(sorted(set(p))) for p in frase.split()])

print(cripto('amanha vou la'))