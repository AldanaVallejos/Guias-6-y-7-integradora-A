#***********************************************************
# Fecha: 14/10/2021
# Autor: Aldana Vallejos
# Guia N6
#***********************************************************
# EJERCICIO 18: Escriba un programa que permita crear una lista de palabras y que, a continuación de tres opciones:
# •	Contar: Me pide una cadena, y me dice cuantas veces aparece en la lista
# •	Modificar: Me pide una cadena, y otra cadena a modificar, y modifica todas alas apariciones de la primera por la segunda en la lista.
# •	Eliminar: Me pide una cadena, y la elimina de la lista.
# •	Mostrar: Muestra la lista de cadenas
# •	Terminar
#***********************************************************
#                    D I S E Ñ O
#***********************************************************
# Declaración de variables
lista=[]
continuar=True
cadena=input("Introduce elementos para la lista (finaliza con *): ") #Ingreso de dato
while cadena!="*":
    lista.append(cadena)
    cadena = input("Introduce elementos para la lista (finaliza con*): ")
while continuar==True:
    print("****Menú de opciones****")
    print("[1] Contar")
    print("[2] Modificar")
    print("[3] Eliminar")
    print("[4] Mostrar")
    print("[5] Terminar")
    opcion=int(input("Seleccione una opción:")) #Ingreso de dato
    if opcion==1: #Caso de que opción sea igual a contar
        cadena=input("Introduce una cadena a buscar:") #Ingreso de dato
        print("La cadena aparece %d veces" % lista.count(cadena))
    elif opcion==2: #Caso de que opción sea igual a modificar
        cadena=input("Introduce una cadena a buscar:") #Ingreso de dato
        cadena2=input("Introduce una cadena a modificar:") #Ingreso de dato
        indice=0
        for elemento in lista:
            if elemento==cadena:
                lista[indice]=cadena2
            indice+=1
    elif opcion==3: #Caso de que opción sea igual a eliminar
        cadena=input("Introduce una cadena a eliminar:") #Ingreso de dato
        if cadena in lista:
            while cadena in lista:
                lista.remove(cadena)
        else:
            print("No existe ese elemento en la lista.") #Salida por pantalla
    elif opcion==4: #Caso de que opción sea igual a mostrar
        for elemento in lista:
            print(elemento," ",end="") #Salida por pantalla
    elif opcion==5: #Caso de que opción sea igual a salir
        break
    else: #Validacion
        print("Error. Ingrese una opción correcta") #Salida por pantalla