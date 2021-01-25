uso =float(input("digite os minutos da chamada"))

if uso <200:
    preco = uso *0.20
    print("o preço da ligação é: ", preco)
elif uso  <=400:
    preco =uso * 0.18
    print("o preço da ligação é: ", preco)
elif uso <= 800:
    preco = uso* 0.15
    print("o preço da ligação é: ", preco)
else:
    preco =0.08 *uso
    print("o valor da ligação foi de: ", preco)