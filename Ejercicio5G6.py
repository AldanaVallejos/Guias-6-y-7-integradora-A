#***********************************************************
# Fecha: 09/10/2021
# Autor: Aldana Vallejos
# Guia N6
#***********************************************************
# EJERCICIO 5: Hacer un programa que inicialice una lista de números con valores
#              aleatorios (10 valores), y posterior ordene los elementos de menor a mayor.
#***********************************************************
#                    D I S E Ñ O
#***********************************************************
# Declaración de variables
listacadenas=[]
import random

listacadenas=[random.randint(0, 100),random.randint(0, 100),random.randint(0, 100),random.randint(0, 100),random.randint(0, 100),random.randint(0, 100),random.randint(0, 100),random.randint(0, 100),random.randint(0, 100),random.randint(0, 100),]

print("La lista con 10 valores aleatorios es {0}".format(listacadenas)) #Salida por pantalla
print("La lista anterior ordenada de menor a mayor es {0}".format(sorted(listacadenas))) #Salida por pantalla