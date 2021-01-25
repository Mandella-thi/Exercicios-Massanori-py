salario =float(input("digite quanto você por hora"))
horas= float(input("digite quantas horas trabalha por mês"))
bruto = salario*horas
irenda =bruto *(11/100)
inss= bruto* (8/100)
sindi =bruto *(5/100)
liquido =bruto -sindi -inss -irenda
print(f'Seu sálario bruto é de {bruto} reais')
print(f"você pagou de imposto de renda {irenda} reais")
print(f'Você pagou de INSS {inss} reais')
print(f'Você pagou de Sindicato {sindi} reais')
print(f'Se salário liquido é de {liquido} reais')