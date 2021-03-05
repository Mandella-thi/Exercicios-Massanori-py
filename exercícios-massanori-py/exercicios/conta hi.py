# E. count_hi #
# conta o número de vezes que aparece a string 'hi'
# count_hi('abc hi ho') -> 1
# count_hi('ABChi hi') -> 2
# count_hi('hihi') -> 2
def count_hi(s):
    return s.count('hi')
print(count_hi('hihimhi'))