# C. luck_sum #
# Soma três inteiros a, b, c
# Se aparecer um 13 ele não conta e todos os da sua direita também
# lucky_sum(1, 2, 3) -> 6
# lucky_sum(1, 2, 13) -> 3
# lucky_sum(1, 13, 3) -> 1
def lucky_sum(a, b, c):
  if a==13:
    return 0
  elif b==13:
      return a
  elif c==13:
      return a+b
  else:
      return a+b+c
print(lucky_sum(1,2,13))