# I. count_evens
# conta os números pares da lista
# count_evens([2, 1, 2, 3, 4]) -> 3
# count_evens([2, 2, 0]) -> 3
# count_evens([1, 3, 5]) -> 0
def count_evens(nums):
  cont=0
  for k in nums:
      if k %2==0:
          cont +=1
  return cont

print(count_evens([2,4,6,5,7,9]))