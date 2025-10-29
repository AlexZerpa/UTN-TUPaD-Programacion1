#TP5
# EJERCICIO 1
notas= [6, 5, 10, 8, 10,4,9,8,8,7]
print("Lista de notas:")
for i in notas:
    print(i, end=" ")
print("\n")

#PROMEDIO
promedio = sum(notas) / len(notas)
print("El promedio de las notas es:", promedio)
#notas ALTAS y notas BAJAS
notas_masaltas = notas[0]
for i in notas:
    if i>notas_masaltas:
        notas_masaltas=i
notas_masbajas = notas[0]
for i in notas:
    if i<notas_masbajas:
        notas_masbajas=i        
print("La nota mas alta es:", notas_masaltas)
print("La nota mas baja es:", notas_masbajas)

# EJERCICIO 2
productos =[]
for i in range(5):
    producto = input("Ingrese el nombre del producto: ")
    productos.append(producto)

#Mostrar la lista de productos
productos_ordenados = sorted(productos)
print("Lista de productos ordenados alfabéticamente:")
for producto in productos_ordenados:
    print(producto)
#ELIMINAR UN PRODUCTO
producto_eliminar = input("Ingrese el nombre del producto que desea eliminar: ")
if producto_eliminar in productos:
    productos.remove(producto_eliminar)
    print(f"El producto '{producto_eliminar}' ha sido eliminado.")
    for producto in productos:
        print(producto)
else:
    print(f"El producto '{producto_eliminar}' no se encuentra en la lista.")

# EJERCICIO 3
import random
numeros=[random.randint(1,100) for i in range(15)]
print("lista de numeros generadas:")
for i in numeros:
    print(i, end=" ")
print("\n")

pares=[]
impares=[]

for num in numeros:
    if num%2==0:
        pares.append(num)
    else:
        impares.append(num)

print("Cantidad de numeros pares: ", len(pares))
print("Cantidad de numeros impares: ", len(impares))

# EJERCICIO 4
datos = [1,3,5,3,7,1,9,5,3]
print("Lista original:", datos)
datos_sin_duplicados = list(set(datos))
print("Lista sin duplicados:", datos_sin_duplicados)

# EJERCICIO 5
estudiantes = ["Luis","Carlos","Ana","Maria","Jose","Lucia","Jorge","Sofia"]
print("Lista de estudiantes:",estudiantes)

accion = input("¿Desea AGREGAR un estudiante o ELIMINAR uno? (Escriba 'agregar' o 'eliminar'): ").lower()

if accion == "agregar":
    nuevo_estudiante = input("Ingrese el nombre del nuevo estudiante: ")
    estudiantes.append(nuevo_estudiante)
    print("Estudiante agregado. Lista actualizada:", estudiantes)
elif accion == "eliminar":
    estudiante_eliminar = input("Ingrese el nombre del estudiante a eliminar: ")
    if estudiante_eliminar in estudiantes:
        estudiantes.remove(estudiante_eliminar)
        print("Estudiante eliminado. Lista actualizada:", estudiantes)
    else:
        print("El estudiante no se encuentra en la lista.")

# EJERCICIO 6
numeros =[1,2,3,4,5,6,7]
print("Lista original: ", numeros)

ultimo_elemento = numeros[-1]
resto = numeros[:-1]

print("Ultimo elemento: ", ultimo_elemento)
print("Resto de la lista: ", resto)

nueva_lista = [ultimo_elemento] + resto
print("Lista con el ultimo elemento al principio: ", nueva_lista)

# EJERCICIO 7
temperaturas = [[10,25],[12,28],[8,20],[15,30],[11,26],[9,22],[13,29]]

suma_minimas=0
suma_maximas=0  
for dia in temperaturas:
    suma_minimas+=dia[0]
    suma_maximas+=dia[1]

promedio_minimas=suma_minimas/len(temperaturas)
promedio_maximas=suma_maximas/len(temperaturas)
print("El promedio de las temperaturas minimas es:", promedio_minimas)
print("El promedio de las temperaturas maximas es:", promedio_maximas)  

mayor_amplitud=0
dia_mayor_amplitud= -1

for i, dia in enumerate(temperaturas):
    amplitud= dia[1]-dia[0]
    if amplitud>mayor_amplitud:
        mayor_amplitud=amplitud
        dia_mayor_amplitud=i+1

print(f"La mayor amplitud térmica se registro el dia {dia_mayor_amplitud} con una amplitud de {mayor_amplitud} grados.")

# EJERCICIO 8
notas_estudiantes = [[8,7,9],[6,9,8],[10,8,7],[7,6,9],[9,10,10]]

for i, notas in enumerate(notas_estudiantes):
    promedio = sum(notas) / len(notas)
    print(f"El promedio del estudiante {i+1} es: {promedio}")  

for j in range(len(notas_estudiantes[0])):
    suma_materia = 0
    for i in range(len(notas_estudiantes)):
        suma_materia += notas_estudiantes[i][j]
    promedio_materia = suma_materia / len(notas_estudiantes)
    print(f"El promedio de la materia {j+1} es: {promedio_materia}")

# EJERCICIO 9
tablero = [['-' for _ in range(3)] for _ in range(3)]

def mostrar_tablero(tablero):
    for fila in tablero:
        print(" ".join(fila))

jugador='X'
while True:
    mostrar_tablero(tablero)
    print(f"Turno del jugador {jugador}.")

    try:
        fila = int(input("Ingrese el numero de fila (1-3): ")) - 1
        columna = int(input("Ingrese el numero de columna (1-3): ")) - 1

        if 0 <= fila <=2 and 0 <= columna <= 2 and tablero[fila][columna] == '-':
            tablero[fila][columna] = jugador

            if jugador == 'X':
                jugador = 'O'
            else:
                jugador = 'X'
        else:
            print("Movimiento invalido. Intente de nuevo.")
    except (ValueError, IndexError):
        print("Entrada invalida. Por favor ingrese numeros entre 1 y 3.")

# EJERCICIO 10
ventas=[[10,20,15,25,30,18,20],
        [5,12,8,10,15,9,11],
        [25,30,28,35,40,32,38],
        [8,15,11,19,21,14,16]]

print("Ventas totales por producto:")
for i in range(len(ventas)):
    total = 0
    for venta in ventas[i]:
        total += venta
    print(f"Producto {i+1}: {total}")

ventas_por_dia =[0]* len(ventas[0])
for i in range(len(ventas[0])):
    for j in range(len(ventas)):
        ventas_por_dia[i] += ventas[j][i]

dia_max_ventas = 0
max_ventas = 0
for i in range(len(ventas_por_dia)):
    if ventas_por_dia[i] > max_ventas:
        max_ventas = ventas_por_dia[i]
        dia_max_ventas = i + 1

print("\nVentas totales por dia:",ventas_por_dia)
print(f"El dia con mayores ventas es el dia {dia_max_ventas} con {max_ventas} ventas")

totales_productos =[sum(fila) for fila in ventas]
producto_mas_vendidos=0
max_vendido = 0
for i in range(len(totales_productos)):
    if totales_productos[i]>max_vendido:
        max_vendido=totales_productos[i]
        producto_mas_vendidos=i+1

print("\nTotales de ventas por producto:", totales_productos)
print(f"El producto mas vendido es el producto {producto_mas_vendidos} con {max_vendido} ventas")