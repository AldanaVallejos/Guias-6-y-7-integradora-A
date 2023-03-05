#***********************************************************
# Fecha: 09/10/2021
# Autor: Aldana Vallejos
#***********************************************************
# EJERCICIO 3: Se quiere realizar un programa que lea por teclado las 5 notas obtenidas por un alumno
#              (comprendidas entre 0 y 10). A continuación debe mostrar todas las notas, la nota
#              media, la nota más alta que ha sacado y la menor.
#***********************************************************
#                    D I S E Ñ O
#***********************************************************
# Declaración de variables
listanotas=[]
nota1=-1
nota2=-1
nota3=-1
nota4=-1
nota5=-1
notamedia=[]
notaalta=[]
notamenor=[]
notamedia1=[]

while nota1<0 or nota1>10:
    try:#Validacion
        #Ingreso de datos
        nota1=int(input("Ingrese la nota: "))
        nota2=int(input("Ingrese la nota: "))
        nota3=int(input("Ingrese la nota: "))
        nota4=int(input("Ingrese la nota: "))
        nota5=int(input("Ingrese la nota: "))
    except ValueError:
        print("Error. Ingrese números")
    if nota1>10 or nota1<0:#Validacion
        print("Error. Ingrese una nota entre 0 y 10")
        
    listanotas.append(nota1)
    listanotas.append(nota2)
    listanotas.append(nota3)
    listanotas.append(nota4)
    listanotas.append(nota5)
    notamedia=sum(listanotas)/5
  
#salidas por pantalla
print("Las notas son: {0}".format(listanotas))
print("La nota media es: {0}".format(notamedia))
print("La nota más alta es {0}".format(max(listanotas)))
print("La nota menor es {0}".format(min(listanotas)))