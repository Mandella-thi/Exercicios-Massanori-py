conta= int(input('Conta: '))
pgto= int(input('pagamento'))
troco=pgto -conta
notas=[50,20,10,5,2,1]
for nota in notas:
    while troco >=nota:
        print(f'uma nota de {nota}')
        troco -=nota