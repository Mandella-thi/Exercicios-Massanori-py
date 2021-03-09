# F. busca (COMP 89 IME-USP)
# Verifique quantas ocorrências de uma palavra há numa frase
# frase = 'ana e mariana gostam de banana'
# palavra = 'ana'
# busca ('ana e mariana gostam de banana', 'ana') == 4
# Hall of Fame Victor H. Panisa, 1a turma Python para Zumbis
def busca(frase, palavra):
  return len([k for k in range(len(frase))
      if frase[k:k+len(palavra)] == palavra])

print(busca('ana e mariana gostam de banana','ana'))