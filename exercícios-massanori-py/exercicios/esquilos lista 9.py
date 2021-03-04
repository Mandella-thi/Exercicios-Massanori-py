#H. squirrel_play
# os esquilos na FATEC brincam quando a temperatura está entre 60 e 90
# graus Fahreneit (são estrangeiros e o termômetro é diferente rs)
# caso seja verão, então a temperatura superior é 100 no lugar de 90
# retorne True caso os esquilos brinquem
# squirrel_play(70, False) -> True
# squirrel_play(95, False) -> False
# squirrel_play(95, True) -> True
def squirrel_play(temp, is_summer):
    if 90>=temp>=60 and is_summer== False:
      return True
    if 100>=temp>=60 and is_summer==True:
        return True
    return False

print(squirrel_play(60,False))
