# D. double_char #
# retorna os caracteres da string original duplicados
# double_char('The') -> 'TThhee'
# double_char('AAbb') -> 'AAAAbbbb'
# double_char('Hi-There') -> 'HHii--TThheerree'
def double_char(s):
    t=''
    for k in range(len(s)):
        t+=s[k]*2
    return t

print(double_char('Thiago'))