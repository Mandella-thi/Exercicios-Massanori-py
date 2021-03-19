import ctypes

atributo_ocultar=0x02

retorno= ctypes.windll.kernel32.SetFileAttributesW('ocultar.txt', atributo_ocultar)

if retorno:
    print("arquivo ocultado")
else:
    print('arquivo não foi ocultado')