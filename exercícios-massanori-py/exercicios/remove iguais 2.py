# D. Dada uma lista de números retorna uma lista sem os elementos repetidos
def remove_iguais(nums):
  return list(set(nums))

print(remove_iguais([1,1,2,3,3]))
