# B. lone_sum
# Soma maluca: some os números inteiros a, b, e c
# Se algum número aparecer repetido ele não conta na soma
# lone_sum(1, 2, 3) -> 6
# lone_sum(3, 2, 3) -> 2
# lone_sum(3, 3, 3) -> 0
def lone_sum(a, b, c):
  if a!=b and b!=c and a!=c:
      return a+b+c
  elif a==b and b==c and a==c:
      return 0
  elif a==b:
      return c
  elif a==c:
      return b
  elif b==c:
      return a

print(lone_sum(4,3,4))