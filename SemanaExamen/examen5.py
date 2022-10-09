import collections

alumnos_pila = collections.deque()
for i in range(3):
    alumnos_pila.append(input("dime el nombre del alumno: "))
    
print("---------------")
print("tamaño de la pila: ")
print(len(alumnos_pila))
print("---------------")
print("elementos de la pila: ")


while alumnos_pila:
    print(alumnos_pila.pop())

print("----------------")
print("hasta aqui, los elementos han sido desapilados")
pass