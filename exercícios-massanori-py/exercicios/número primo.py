num= int(input("Digite o número que você acha que é primo"))
k=1
divisores=0
while k<=num:
    if num%k ==0:
        divisores= divisores+1
    k=k+1
print(divisores==2)