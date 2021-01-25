palavra= input("digite a palavra a ser testada")
if palavra == palavra[::-1]:
    print(f"A palavra {palavra} é palindromo")
else:
    print("A palavra não é palindromo")