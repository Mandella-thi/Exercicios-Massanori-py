area = int(input("Digite quantos metros quadrados pretende pintar"))
alata= 3*18
lata= int(area /alata)
if (area % alata) !=0:
    lata =lata +1
grana = lata *80
print(f'A quantidade de latas necessárias é {lata} e o preço sera de {grana} reais')