valor = int(input("Digite o valor da compra"))
pagamento=int(input("Gigite o valor do pagamento"))
troco= pagamento - valor
if troco >=50:
    notas50= int(troco/50)
    resto50=troco%50
    print(f"notas de 50 são:{notas50}")
    if resto50 >=20:
        notas20=int(resto50/20)
        resto20= resto50%20
        print(f"notas de 20 são {notas20}")
        if resto20>=10:
            notas10=int(resto20/10)
            resto10=resto20%10
            print(f'notas de 10 são: {notas10}')
            if resto10>= 5:
                notas5 =int(resto10/5)
                resto5=resto10%5
                print(f'Notas de 5 são: {notas5}')
                if resto5 >=1:
                    notas1=int(resto5/1)
                    print(f'notas de 1 são {notas1}')
                else:
                    print("não tem notas de 1")
            elif 5>resto10>=1:
                print(f'notas de 1 são: {resto10}')
        elif 10>resto20>=5:
            notas5= int(resto20/5)
            resto5= resto20%5
            print(f'Notas de 5 são: {notas5}')
            if resto5>=1:
                notas1= resto5
                print(f'Notas de 1 são: {notas1}')
        elif 5>resto20>=1:
            notas1= resto20
            print(f'Notas de 1 são: {notas1}')
    elif 20>resto50>=10:
        notas10= int(resto50/10)
        resto10= resto50%10
        print(f'notas de 10 são: {notas10}')
        if resto10>= 5:
            notas5= int(resto10/5)
            resto5= resto10%5
            print(f'notas de 5 são:{notas5}')
            if resto5 >=1:
                notas1= int(resto5/1)
                print(f'notas 1 são: {notas1}')
    elif 10>resto50>=5:
        notas5= resto50/5
        resto5=resto50%5
        if resto5>=1:
            notas1=resto5
            print(f'notas de 1 são: {notas1}')
    elif 5>resto50>=1:
        print(f'notas de 1 são{resto50}')

    elif 10>resto50>=5:
        notas5= int(resto50/5)
        resto5= resto50%5
        print(f'Notas de 5 são: {notas5}')
        if resto5 >=1:
            notas1=resto5
            print(f'Notas de um são: {notas1}')
    elif 5>resto50>=1:
        notas1 =resto50
        print(f'Notas de 1 são: {notas1}')
elif 50>troco>=20:
    notas20 = int(troco / 20)
    resto20 = troco % 20
    print(f"notas de 20 são {notas20}")
    if resto20 >= 10:
        notas10 = int(resto20 / 10)
        resto10 = resto20 % 10
        print(f'notas de 10 são: {notas10}')
        if resto10 >= 5:
            notas5 = int(resto10 / 5)
            resto5 = resto10 % 5
            print(f'Notas de 5 são: {notas5}')
            if resto5 >= 1:
                notas1 = resto5 / 1
                print(f'notas de 1 são {notas1}')
        elif 5>resto10>=1:
            notas1 =int(resto10/1)
            print(f'Notas de 1 são{notas1}')
    elif 10>resto20>=5:
        notas5= int(resto20/5)
        resto5= resto20%5
        print(f'Notas de 5 são: {notas5}')
        if resto5>=1:
            notas1= resto5
            print(f'Notas de 1 são: {notas1}')
    elif 5>resto20>=1:
        notas1= resto20
        print(f'Notas de 1 são: {notas1}')
elif troco >= 10:
    notas10 = int(troco / 10)
    resto10 = troco % 10
    print(f"notas de 10 são {notas10}")
    if resto10 >= 5:
            notas5 = int(resto10 / 5)
            resto5 = resto10 % 5
            print(f'Notas de 5 são: {notas5}')
            if resto5 >= 1:
                notas1 = resto5 / 1
                print(f'notas de 1 são {notas1}')
            else:
                print("não tem notas de 1")
elif 10>troco >= 5:
    notas5 = int(troco / 5)
    resto5 = troco % 5
    print(f"notas de 5 são {notas5}")
    if resto5 >= 1:
            notas1 = int(resto5 / 1)
            print(f'Notas de 1 são: {notas1}')
elif 5>troco >= 1:
    notas1 = troco / 1
    print(f"notas de 1 são {notas1}")
