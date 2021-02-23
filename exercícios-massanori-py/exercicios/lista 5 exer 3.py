cont =0
for x in range(1066,3628):
    if x% 2==0 and x% 7==0:
        cont= cont +1
print(f'os que são divisiveis por 2 e por 7 são:{cont}')