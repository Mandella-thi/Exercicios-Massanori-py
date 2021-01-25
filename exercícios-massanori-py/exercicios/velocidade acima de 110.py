velocidade = int(input("digite a velocidade do carro"))
if velocidade > 110:
    valor = (velocidade -110)*5
    print("multado em R$", valor)
else:
    print("não multado")
