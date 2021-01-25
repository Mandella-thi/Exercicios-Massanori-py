lado1 =int(input("digite o primeiro lado do triângulo"))
lado2= int(input("digite o sehundo lado do triângulo"))
lado3 = int(input("digite o terceiro lado do triângulo"))
if abs(lado1-lado2) <lado3 and lado3< (lado1 +lado2) and abs(lado2-lado3)<lado1 and lado1<(lado2 +lado3) and abs(lado1-lado3)< lado2 and lado2< (lado1+lado3):
    print("pode ser um tiângulo")
    if lado1== lado2 and lado1== lado3 and lado2==lado3:
        print("este triângulo é equilatero")
    elif lado1== lado2 and lado1 != lado3 and lado2 != lado3:
        print("este triângulo é isóceles")
    else:
        print("este triângulo é escaleno")