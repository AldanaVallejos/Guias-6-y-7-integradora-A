#***********************************************************
# Fecha: 14/10/2021
# Autor: Aldana Vallejos
# Guia N6
#***********************************************************
# EJERCICIO 16: Vamos a crear un programa que tenga el siguiente menú:
# 1.	Añadir número a la lista: Me pide un número de la lista y lo añade al final de la lista.
# 2.	Añadir número de la lista en una posición: Me pide un número y una posición, y si la posición existe en la lista lo añade a ella (la posición se pide a partir de 1).
# 3.	Longitud de la lista: te muestra el número de elementos de la lista.
# 4.	Eliminar el último número: Muestra el último número de la lista y lo borra.
# 5.	Eliminar un número: Pide una posición, y si la posición existe en la lista lo borra de ella (la posición se pide a partir de 1).
# 6.	Contar números: Te pide un número y te dice cuantas apariciones hay en la lista.
# 7.	Posiciones de un número: Te pide un número y te dice en que posiciones está (contando desde 1).
# 8.	Mostrar números: Muestra los números de la lista
# 9.	Salir
#***********************************************************
#                    D I S E Ñ O
#***********************************************************
# Declaración de variables
continuar=True
opcion=0
lista=[]
posicion=0
apariciones=0

#Menú

while continuar==True:
    print("\n")
    print(""" MENÚ
    1 Añadir número a la lista
    2 Añadir número de la lista en una posición
    3 Longitud de la lista
    4 Eliminar el último número
    5 Eliminar un número
    6 Contar números
    7 Posiciones de un número
    8 Mostrar números
    9 Salir""")
    print("\n")
    try:
        opcion=int(input("Ingrese la opción elegida: ")) #Ingreso de dato
    except ValueError: #Validaciones
        print("Error. Tiene que ingresar un número entre 0 y 4")
    if opcion!=0 and opcion!=1 and opcion!=2 and opcion!=3 and opcion!=4 and opcion!=5 and opcion!=6 and opcion!=7 and opcion!=8 and opcion!=9:
          print("Error. El número ingresado es incorrecto.")
    else:
        if opcion==9: #Caso de opcion=salir
            print("Saliendo.")
            continuar=False
            break
        
        if opcion==1: #Caso añadir numero a la lista
            nro_ingresar=int(input("Ingrese el número a añadir al final de la lista: "))
            lista.append(nro_ingresar)
        
        if opcion==2: #Caso añadir numero de la lista en una posicion
            try:
                nro_ingresar=int(input("Ingrese el número a añadir a la lista: "))
                posicion=int(input("Ingrese una posicion (a partir del 1): "))
            except ValueError:
                print("Error. Ingrese numeros")
            if posicion<len(lista):
                lista.insert(posicion-1, (nro_ingresar))
            else:
                print("Posicion Incorrecta")
        
        if opcion==3: #Caso longitud de la lista
            print("La lista tiene {0} elementos".format(len(lista)))
        
        if opcion==4: #Caso eliminar el ultimo numero
            if len(lista)>0:
                print("El último número que se borrará de la lista es {0}".format(lista.pop()))
            else:
                print("La lista está vacia")
        
        if opcion==5: #Caso eliminar un numero
            try:
                posicion=int(input("Ingrese una posicion (a partir del 1):"))
            except ValueError:
                print("Error. Ingrese numeros")
            if posicion>len(lista):
                print("Posición incorrecta")
            else:
                print("El último número que se borrará de la lista es {0}".format(lista.pop(posicion - 1)))
        
        if opcion==6: #Caso contar numeros
            try:
                nro_ingresar=int(input("Ingrese un número a contar: "))
            except ValueError:
                print("Error. Ingrese numeros")
            print("El número {0} aparece {1} veces en la lista.".format(nro_ingresar,lista.count(lista)))

        if opcion==7: #Caso posiciones de un numero
            try:
                nro_ingresar=int(input("Ingrese un número: "))
            except ValueError:
                print("Error. Ingreso numeros")
            apariciones=0
            print(f"El numero {nro_ingresar} aparece: ",end=" veces en la lista")
            for aparicion in range(0,lista.count(nro_ingresar)):
                apariciones=lista.index(nro_ingresar,apariciones)
                apariciones+=1
                print(apariciones," ",end="")
      
        if opcion==8: #Caso mostrar lista
            for nro_ingresar in lista:
                print(nro_ingresar," ",end="")