# B. string_splosion
# string_splosion('Code') -> 'CCoCodCode'
# string_splosion('abc') -> 'aababc'
# string_splosion('ab') -> 'aab'
def string_splosion(s):
    return ''.join([s[:k] for k in range(len(s)+1)])


print(string_splosion('pamaka'))