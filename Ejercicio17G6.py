#***********************************************************
# Fecha: 14/10/2021
# Autor: Aldana Vallejos
# Guia N6
#***********************************************************
# EJERCICIO 17: Crear un programa que añada números a una lista hasta que introducimos un número negativo.
#               A continuación debe crear una nueva lista igual que la anterior pero eliminando los números
#               duplicados. Muestra esta segunda lista para comprobar que hemos eliminados los duplicados.
#***********************************************************
#                    D I S E Ñ O
#***********************************************************
# Declaración de variables
milista=[]
continuar="S"
numero=0.00
listanueva=[]

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
    
#Salidas por pantalla
print(milista)
conjunto=set()
conjunto=set(milista)
listanueva=list(conjunto)
print(listanueva)