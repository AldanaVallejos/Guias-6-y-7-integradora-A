#***********************************************************
# Fecha: 11/10/2021
# Autor: Aldana Vallejos
# Guia N6
#***********************************************************
# EJERCICIO 8: Queremos guardar los nombres y las edades de los alumnos de un curso. Realiza un programa
#              que introduzca el nombre y la edad de cada alumno. El proceso de lectura de datos terminará
#              cuando se introduzca como nombre un asterisco (*) Al finalizar se mostrará los siguientes datos:
#              Todos los alumnos mayores de edad y los alumnos mayores (los que tienen más edad).
#***********************************************************
#                    D I S E Ñ O
#***********************************************************
# Declaración de variables
nombres=[]
edades=[]
continuar=True
nombre=""
edad=1
alumnos=0
alumnosmayores=[]
alumnosdemasedad=[]

while continuar==True:
    nombre=input("Ingrese el nombre del alumno: ") #Ingreso de dato
    if nombre=="*":
        break
    try: #Validacion
        edad=int(input("Ingrese la edad: ")) #Ingreso de dato
    except ValueError:
        print("Error. Tiene que ingresar un numero")
        numero=int(input("Ingrese la edad: ")) #Ingreso de dato

    if nombre!="*":
        nombres.append(nombre)
        edades.append(edad)

    if edad==18:
        alumnosmayores.append(nombre)
    
    if edad>18:
        alumnosdemasedad.append(nombre)

#Salidas por pantalla
print(f"Los alumnos mayores son {alumnosmayores}")
print(f"Los alumnos de más edad son {alumnosdemasedad}")