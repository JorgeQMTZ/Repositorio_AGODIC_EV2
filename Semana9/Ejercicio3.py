import pandas as pd
import random
SEPARADOR = ("*"*20)+"\n"

diccionario_notas_aleatorias = {\
    "Crescencio":[random.randrange(60,101) for x in range(3)],\
    "Domitilia":[80,100,57], "Rutilio":[80,70,57], "Panfilo":[20,100,100],\
    "Ludoviko":[100,100,100]}
notas_diccionario = pd.DataFrame(diccionario_notas_aleatorias)
notas_diccionario.index = ["Programacion", "Base de Datos", "Contabilidad"]

print(notas_diccionario["Domitilia"])
print()
print(notas_diccionario.Domitilia)
print(SEPARADOR)

print(notas_diccionario.loc["Programacion"])
print()
print(notas_diccionario.loc["Base de Datos"])
print()
print(notas_diccionario.loc["Contabilidad"])
