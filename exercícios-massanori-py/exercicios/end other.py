# H. end_other #
# as duas strings devem ser convertidas para minúsculo via lower()
# depois disso verifique que no final da string b ocorre a string a
# ou se no final da string a ocorre a string b
# end_other('Hiabc', 'abc') -> True
# end_other('AbC', 'HiaBc') -> True
# end_other('abc', 'abXabc') -> True
def end_other(a, b):
    a.lower()
    b.lower()
    return a.endswith(b) or b.endswith(a)
print(end_other('abc', 'tuabc'))