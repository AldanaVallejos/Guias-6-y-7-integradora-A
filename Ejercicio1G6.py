#***********************************************************
# Fecha: 09/10/2021
# Autor: Aldana Vallejos
#***********************************************************
# EJERCICIO 1: Realizar un programa que inicialice una lista con 10 valores aleatorios (del 1 al 10)
#              y posteriormente muestre en pantalla cada elemento de la lista junto con su cuadrado y su cubo.
#***********************************************************
#                    D I S E Ñ O
#***********************************************************
# Declaración de variables
listavalores=[]
valores=0
cuadrado=0
cubo=0
import random
cantidad=0

for i in range(0,10):
    valores=random.randint(1,10)
    listavalores.append(valores)
    cantidad=len(listavalores)
    if cantidad==10:
        cuadradocubo(listavalores, cuadrado, cubo)
        
    def cuadradocubo(listavalores, cuadrado, cubo):
        for x in range(0,10):
            numero=listavalores[x]
            cuadrado=numero**2
            cubo=numero**3
            print("El número {0} su cuadrado es {1} y su cubo es {2}".format(numero,cuadrado,cubo)) #Salida por pantalla