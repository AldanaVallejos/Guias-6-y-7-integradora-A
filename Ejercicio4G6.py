#***********************************************************
# Fecha: 10/10/2021
# Autor: Aldana Vallejos
#***********************************************************
# EJERCICIO 4: Programa que declare una lista y la vaya llenando de números
#              hasta que introduzcamos un número negativo. Entonces se debe imprimir el vector (sólo los elementos introducidos).
#***********************************************************
#                    D I S E Ñ O
#***********************************************************
# Declaración de variables
milista=[]
continuar="S"
numero=0.00

while continuar=="S":
    try: #Validacion
        numero=int(input("Ingrese un número (finaliza con un número negativo): ")) #Ingreso de dato
    except ValueError:
        print("Error. Tiene que ingresar un numero")
        numero=int(input("Ingrese un número (finaliza con un número negativo): ")) #Ingreso de dato
    
    if numero<0:
        continuar="N"
    else:
        milista.append(numero)

for i in milista: 
    print(i, end=" ") #Salida por pantalla