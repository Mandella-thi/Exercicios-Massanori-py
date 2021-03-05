# A. near_ten #
# Seja um n não negativo, retorna True se o número está a distância de
# pelo menos dois de um múltiplo de dez. Use a função resto da divisão.
# near_ten(12) -> True
# near_ten(17) -> False
# near_ten(19) -> True
def near_ten(n):
  if 8<=n%10 or n%10<=2:
    return True
  else:
    return False
print(near_ten(1))