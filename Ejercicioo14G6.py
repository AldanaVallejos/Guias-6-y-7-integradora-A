#***********************************************************
# Fecha: 13/10/2021
# Autor: Aldana Vallejos
# Guia N6
#***********************************************************
# EJERCICIO 14: Crear un programa que lea los precios de 5 artículos y las cantidades vendidas por una empresa en sus 4 sucursales. Informar:
#               •	Las cantidades totales de cada artículo.
#               •	La cantidad de artículos en la sucursal 2.
#               •	La cantidad del artículo 3 en la sucursal 1.
#               •	La recaudación total de cada sucursal.
#               •	La recaudación total de la empresa.
#               •	La sucursal de mayor recaudación.
#***********************************************************
#                    D I S E Ñ O
#***********************************************************
# Declaración de variables
precios=[]
cantidades=[]
num_articulos=3
num_sucursales=2
for indice_art in range(0, num_articulos):
   precios.append(float(input('Ingrese el precio del articulo %d: ' % (indice_art+1)))) #Ingreso de dato

for indice_sucursal in range(0, num_sucursales):
    cant_art = []
    for indice_art in range(0, num_articulos):
        cant_art.append(int(input('Ingrese la cantidad del articulo %d, en sucursal %d: ' % (indice_art+1,indice_sucursal+1)))) #Ingreso de dato
    cantidades.append(cant_art)

print('Cantidades por artículos: ') #Salida por pantalla
for indice_art in range(0, num_articulos):
    suma = 0
    for cant_sucursal in cantidades:
        suma = suma + cant_sucursal[indice_art]
    print('Total articulo %d: %d ' % (indice_art + 1,suma))

#Salidas por pantalla
print('Total de sucursal 2: %d ' % sum(cantidades[1])) #total de artículos Sucursal 2
print('Sucursal 1 y articulo 3: %d ' % cantidades[0][2])

total_por_sucursal = [] #recaudaciones de cada sucursal
for cant_sucursal in cantidades:
    total=0
    for precio,cantidad in zip(precios,cant_sucursal):
        total=total+precio*cantidad
    total_por_sucursal.append(total)

mayorrec = max(total_por_sucursal)   
indice_sucursal = 1
for indice_sucursal in range(0, num_sucursales):
    print('Recaudaciones de la sucursal %d: %f ' % (indice_sucursal,total_por_sucursal[indice_sucursal])) #Salida por pantalla
    indice_sucursal += 1

indice_sucursal = 1 #sucursal con mayor recaudación
for cant_sucursal in total_por_sucursal:
    if cant_sucursal == mayorrec: break
    indice_sucursal += 1

#Salidas por pantalla
print('Recaudación total de la empresa: %f ' % sum(total_por_sucursal))
print('Sucursal de mayor Recaudación: %d ' % indice_sucursal)