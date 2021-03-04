# I. pego_correndo
# você foi pego correndo
# o resultado será:
# sem multa = 0
# multa média = 1
# multa grave = 2
# velocide <= 60 sem multa
# velocidade entre 61 e 80 multa média
# velocidade maior que 81 multa grave (cidade do interior)
# caso seja seu aniversário a velocidade pode ser 5 km/h maior em todos os casos
# pego_correndo(60, False) -> 0
# pego_correndo(65, False) -> 1
# pego_correndo(65, True) -> 0
def pego_correndo(speed, is_birthday):
  if speed<=60 and is_birthday==False:
      return 0
  elif 80>=speed>=61 and is_birthday==False:
      return 1
  elif speed>=81 and is_birthday==False:
      return 2
  elif speed<=65 and is_birthday==True:
      return 0
  elif 85>=speed>=65 and is_birthday==True:
      return 1
  elif speed>85 and is_birthday==True:
      return 2

print(pego_correndo(90,False))