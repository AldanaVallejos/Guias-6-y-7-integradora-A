#***********************************************************
# Fecha: 09/10/2021
# Autor: Aldana Vallejos
# Guia N6
#***********************************************************
# EJERCICIO 7: Programa que declare tres listas ‘lista1’, ‘lista2’ y ‘lista3’ de cinco
#              enteros cada uno, pida valores para ‘lista1’ y ‘lista2’ y calcule lista3=lista1+lista2.
#***********************************************************
#                    D I S E Ñ O
#***********************************************************
# Declaración de variables
lista1=[]
lista2=[]
lista3=[]
valorlista1=0.00
valorlista2=0.00

for i in range(5):
    try: #Validacion
        valorlista1=float(input("Ingrese un valor para la lista 1 (hasta 5 valores): ")) #ingreso de dato
        lista1.append(valorlista1)
    except ValueError:
        print("Error. Ingrese números, no cadenas de texto")

for x in range(5):
    try: #Validacion
        valorlista2=float(input("Ingrese un valor para la lista 2 (hasta 5 valores): ")) #ingreso de dato
        lista2.append(valorlista2)
    except ValueError:
        print("Error. Ingrese números, no cadenas de texto")

lista3=lista1+lista2
print(f"La lista 3 es {lista3}") #salida por pantalla