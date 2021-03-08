# G. count_code #
# conta quantas vezes aparece 'code'
# a letra 'd' pode ser trocada por outra qualquer
# assim 'coxe' ou 'coze' também são contadas como 'code'
# count_code('aaacodebbb') -> 1
# count_code('codexxcode') -> 2
# count_code('cozexxcope') -> 2
def count_code(s):
  count=0
  for k in range(len(s )-3):
      if s[k:k+2]=='co' and s[k+3]== 'e':
          count+=1
  return count

print(count_code('cozecowecode'))