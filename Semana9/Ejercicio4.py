import pandas as pd
import random
SEPARADOR = ("*"*20)+"\n"

diccionario_notas_aleatorias = {\
    "Crescencio":[random.randrange(60,101) for x in range(3)],\
    "Domitila":[80,100,57], "Rutilio":[80,70,57], "Panfilo":[20,100,100],\
    "Ludoviko":[100,100,100]}
notas=pd.DataFrame(diccionario_notas_aleatorias)
notas.index = ["Programacion", "Base de Datos", "Contabilidad"]

print("Todas las asignaturas, todos los estudiantes")
subConjunto = notas.loc["Programacion":"Contabilidad"]
print(subConjunto)
x = input("Presiona una tecla")

print(SEPARADOR)

print("Ultimas dos asignaturas, todos los estudiantes")
subConjunto = notas.loc["Base de Datos":"Contabilidad"]
print(subConjunto)
print(SEPARADOR)

print("Subconjunto, solamente las notas de Rutilio y Ludoviko para las primeras dos asignaturas")
subConjunto = notas.loc["Programacion":"Base de Datos",["Rutilio","Ludoviko"]]
print(subConjunto)
print(SEPARADOR)

print("Solamente calificaciones aprobatorias")
aprobados = [(notas >= 70) & (notas%2==0)]
print(aprobados)
print(SEPARADOR)

print("La califiacion de 'Panfilo' en 'Programacion'")
nota_PanfiloProgramacion = notas.at["Programacion","Panfilo"]
print(nota_PanfiloProgramacion)
print(SEPARADOR)

print("Modificaremos la nota de Panfilo en programacion")
notas.at["Programacion", "Panfilo"] = 80
nota_PanfiloProgramacion = notas.at["Programacion","Panfilo"]
print(notas)

print(SEPARADOR)