#***********************************************************
# Fecha: 09/10/2021
# Autor: Aldana Vallejos
# Guia N6
#***********************************************************
# EJERCICIO 6: Crea un programa que pida un número al usuario un número de mes (por ejemplo, el 4) y diga
#              cuántos días tiene (por ejemplo, 30) y el nombre del mes. Debes usar listas.
#              Para simplificarlo vamos a suponer que febrero tiene 28 días.
#***********************************************************
#                    D I S E Ñ O
#***********************************************************
# Declaración de variables
numero=0
mesdelaño=[0, "Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
dias=["Tiene 31 días","Tiene 30 días","Tiene 28 días"]

while numero<=0 or numero>12: #Validaciones
    try:
        numero=int(input("Ingrese un número: ")) #Ingreso de dato
    except ValueError:
        print("Error. Ingrese números")
    if numero<=0 or numero>12:
        print("Error. tiene que ingresar un número mayor que 1 y menor que 12")
    else:
        print(mesdelaño[numero]) #Salida por pantalla

if numero==1 or numero==3 or numero==5 or numero==7 or numero==8 or numero==10 or numero==12: #Caso enero, marzo, mayo, julio, agosto, octubre y diciembre
    print(dias[0]) #Salida por pantalla
else:
    if numero!=1 and numero!=3 and numero!=5 and numero!=7 and numero!=8 and numero!=10 and numero!=12:
        if numero==4 or numero==6 or numero==9 or numero==11: #caso abril, junio, septiembre y noviembre
            print(dias[1]) #Salida por pantalla
        else:
            print(dias[2]) #Salida por pantalla
