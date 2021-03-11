# D. Dada uma lista de números retorna uma lista sem os elementos repetidos
def remove_iguais(nums):
    unico=[]
    [unico.append(n) for n in nums if n not in unico]
    return unico

print(remove_iguais([1,1,2,2,3,3,4,4,5,5,5]))