#***********************************************************
# Fecha: 11/10/2021
# Autor: Aldana Vallejos
# Guia N6
#***********************************************************
# EJERCICIO 9: Queremos guardar la temperatura mínima y máxima de 5 días. Realiza un programa que de la siguiente información:
#              La temperatura media de cada día
#              Los días con menos temperatura
#              Se lee una temperatura por teclado y se muestran los días cuya temperatura máxima coincide con ella.
#              si no existe ningún día se muestra un mensaje de información.
#***********************************************************
#                    D I S E Ñ O
#***********************************************************
# Declaración de variables
temperaturaminima=[]
temperaturamaxima=[]
tempmin=0.00
tempmax=0.00
temperaturamedia=0
diaconmenostemperatura=0
minimo=10000

for x in range(1,5+1):
    try:
        tempmin=float(input(f"Ingrese la temperatura minima del día {x}: ")) #Ingreso dato
    except ValueError:
        print("Error. Ingrese valores de temperatura")
        tempmin=float(input(f"Ingrese la temperatura minima del día {x}: ")) #Ingreso dato
    temperaturaminima.append(tempmin)
    try:
        tempmmax=float(input(f"Ingrese la temperatura máxima del día {x}: "))
        temperaturamaxima.append(tempmax)
    except ValueError:
        print("Error. Ingrese valores de temperatura")
        tempmmax=float(input(f"Ingrese la temperatura máxima del día {x}: "))
        temperaturamaxima.append(tempmax)
    
    for i in temperaturaminima:
      if i<minimo:
          diaconmenostemperatura=x
        
    temperaturamedia=(tempmin+tempmax)/2
    #Salidas por pantalla
    print(f"La temperatura media del dia {x} es {temperaturamedia}")
    print(f"El dia con menos temperatura es el dia: {diaconmenostemperatura}")


