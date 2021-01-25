pesca =int(input("Digite a quantidade de peixes"))
if pesca> 50:
    excedente = pesca -50
    multa =excedente *4
    print(f"Voce levou uma multa de {multa} reais por ter um excedente de {excedente} kilos")
else:
    print("não tem multa, continue pescando")