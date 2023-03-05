#***********************************************************
# Fecha: 13/10/2021
# Autor: Aldana Vallejos
# Guia N6
#***********************************************************
# EJERCICIO 15: Crear un programa de ordenador para gestionar los resultados de la quiniela de fútbol. Para ello vamos a utilizar dos tablas:
# •	Equipos: Que es una tabla de cadenas donde guardamos en cada columna el nombre de los equipos de cada partido. En la quiniela se indican 15 partidos.
# •	Resultados: Es una tabla de enteros donde se indica el resultado. También tiene dos columnas, en la primera se guarda el número
#  de goles del equipo que está guardado en la primera columna de la tabla anterior, y en la segunda los goles del otro equipo.
# El programa ira pidiendo los nombres de los equipos de cada partido y el resultado del partido, a continuación se imprimirá la quiniela de esa jornada.
# ¿Qué modificación habría que hacer en las tablas para guardar todos los resultados de todas las jornadas de la temporada?
#
#***********************************************************
#                    D I S E Ñ O
#***********************************************************
# Declaración de variables
equipos=[]
resultados=[]

#Constante
num_equipos=15

for indice in range(0,num_equipos): #Bucle para ingresar los nombres de los 15 equipos y los goles anotados
	#Nombre de los equipos
	partido=[] #inicializo lista
	partido.append(input("Ingrese el nombre del equipo 1 del partido %d: " % (indice+1))) #Ingreso de datos
	partido.append(input("Ingrese el nombre del equipo 2 del partido %d: " % (indice+1)))
	equipos.append(partido) #Guardo en otra lista
	#Resultados de los equipos
	goles=[]
	goles.append(int(input("Ingrese los goles anotados por el equipo %s: " % (partido[0]))))
	goles.append(int(input("Ingrese los goles anotados por el equipo %s: " % (partido[1]))))
	resultados.append(goles)

#Armo la quiniela
print("\n")
print("QUINIELA")
for partido,goles in zip(equipos,resultados): #Bucle para mostrar la quiniela
	print(partido[0],"-",partido[1],":",end="")  #nombre del 1er equipo - nombre del 2do equipo : resultado
	if goles[0]>goles[1]: #Caso primer equipo ganó
		print("-> 1")
	else:
		if goles[0]<goles[1]: #Caso segundo equipo ganó
			print("-> 2")
		else: #Caso de un empate entre los equipos
			print("-> X")