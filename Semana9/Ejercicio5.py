import pandas as pd
import random
SEPARADOR = ("*"*20)+"\n"

diccionario_notas_aleatorias = {\
    "Crescencio":[random.randrange(60,101) for x in range(3)], \
    "Domitila":[80,100,57], "Rutilio":[80,70,57], "Panfilo":[20,100,100],\
    "Ludoviko":[100,100,100]}
notas = pd.DataFrame(diccionario_notas_aleatorias)
notas.index = ["Programacion", "Base de Datos", "Contabilidad"]

notas.to_csv(r'notas.csv', index=True, header=True)
print("SI SE PUDO PA")