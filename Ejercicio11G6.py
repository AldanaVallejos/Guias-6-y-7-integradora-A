#***********************************************************
# Fecha: 14/10/2021
# Autor: Aldana Vallejos
# Guia N6
#***********************************************************
# EJERCICIO 11: Diseñar el algoritmo correspondiente a un programa, que:
# Crea una tabla bidimensional de longitud 5x5 y nombre ‘diagonal’.
# Carga la tabla de forma que los componentes pertenecientes a la diagonal de la matriz tomen el valor 1 y el resto el valor 0.
# Muestra el contenido de la tabla en pantalla.
#***********************************************************
#                    D I S E Ñ O
#***********************************************************
# Declaracion de variables
diagonal=[]
import math

for i in range(5):
    diagonal.append([5,10,15,20,25])
for primero in range(5):
    for segundo in range(5):
        if segundo==primero:
            diagonal[primero][segundo]=1
        else:
            diagonal[primero][segundo]=0

print(diagonal) #Salida por pantalla