
nota= int(input("Digite a nota"))
while nota<0 or nota>10:
    nota= int(input("digite a nota"))
    if nota <0 or nota>10:
        print("Valor incorreto para nota")
    else:
        print(nota)