#***********************************************************
# Fecha: 11/10/2021
# Autor: Aldana Vallejos
# Guia N6
#***********************************************************
# EJERCICIO 13: De una empresa de transporte se quiere guardar el nombre de los conductores que tiene, y los kilómetros que conducen cada día de la semana.
#               Para guardar esta información se van a utilizar dos arreglos:
#               •	Nombre: Lista para guardar los nombres de los conductores.
#               •	kms: Tabla para guardar los kilómetros que realizan cada día de la semana.
#               •	Se quiere generar una nueva lista (“total_kms”) con los kilómetros totales que realza cada conductor.
#               Al finalizar se muestra la lista con los nombres de conductores y los kilómetros que ha realizado.
#***********************************************************
#                    D I S E Ñ O
#***********************************************************
# Declaración de variables
nombre=[]
kms=[]
total_kms=[]
kilometros=0
continuar=True

while continuar==True:
    nombres=input("Ingrese el nombre del conductor: ") #Ingreso dato
    nombre.append(nombres)
    for dia in ("lunes","martes","miércoles","jueves","viernes"):
        try: 
            kilometros=int(input(f"Ingrese los kilometros recorridos el {dia} ")) #Ingreso dato
        except ValueError:
            print("Error Ingrese números") #Validación
        kms.append(kilometros)
        total_kms=sum(kms)
    print("El/los conducto/res {0} hizo/hicieron un total de {1} kilómetros".format(nombre,total_kms)) #Salida por pantalla
    
    