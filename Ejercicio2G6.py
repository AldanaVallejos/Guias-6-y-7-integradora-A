#***********************************************************
# Fecha: 09/10/2021
# Autor: Aldana Vallejos
#***********************************************************
# EJERCICIO 2: Crea una lista e inicializala con 5 cadenas de caracteres leídas por teclado.
#              Copia los elementos de la lista en otra lista pero en orden inverso, y muestra sus elementos por la pantalla.
#***********************************************************
#                    D I S E Ñ O
#***********************************************************
# Declaración de variables
listacadenas=[]
listanueva=[]
cadena=""
validacion=True

for x in range(5):
    cadena=input("Ingrese una cadena de caracteres que desee incluir en la lista: ") #Ingreso de dato
    listacadenas.append(cadena)

listanueva=(listacadenas[::-1])

print("La lista creada en orden inverso es: {0}".format(listanueva)) #Salida por pantalla