# 1. Diccionario inicial
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
print(f"Diccionario original: {precios_frutas}")

# Añadir las nuevas frutas [cite: 16, 17, 18]
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

print(f"Diccionario actualizado: {precios_frutas}")

# 2. Actualizar los precios de las frutas
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

print(f"Diccionario con precios actualizados: {precios_frutas}")

# 3. Crear una nueva lista unicamente las frutas sin el precio:
lista_frutas = list(precios_frutas.keys())

print(f"Lista de frutas: {lista_frutas}")

# 4. Agenda de numero telefonicos:
contactos = {}

print("--- Carga de Contactos ---")
# Permitir al usuario cargar 5 contactos 
for i in range(5):
    # Usamos i+1 para que muestre "Contacto 1", "Contacto 2", etc.
    nombre = input(f"Ingrese el nombre del contacto {i+1}: ")
    numero = input(f"Ingrese el número de {nombre}: ")
    contactos[nombre] = numero # Guardamos en el diccionario

print(f"\nAgenda completa: {contactos}")

print("\n--- Consulta de Contactos ---")
# Pedir un nombre y mostrar el número [cite: 25]
nombre_consulta = input("Ingrese el nombre del contacto que desea consultar: ")

# Usamos el método .get() que es más seguro
numero_encontrado = contactos.get(nombre_consulta)

if numero_encontrado:
    print(f"El número de {nombre_consulta} es: {numero_encontrado}")
else:
    print(f"El contacto '{nombre_consulta}' no se encuentra en la agenda.")

# 5. fRASES

frase = input("Ingrese una frase: ")

# Preparamos la frase: minúsculas y la separamos en una lista de palabras
palabras = frase.lower().split()

# Palabras únicas (usando un set) 
# Un set, por definición, no puede tener elementos repetidos.
palabras_unicas = set(palabras)
print(f"Palabras únicas: {palabras_unicas}")

# Diccionario con recuento de palabras 
recuento = {}
for palabra in palabras:
    if palabra in recuento:
        # Si la palabra ya está en el diccionario, le sumamos 1
        recuento[palabra] += 1
    else:
        # Si es la primera vez que la vemos, la agregamos con valor 1
        recuento[palabra] = 1

print(f"Recuento de palabras: {recuento}")

# 6. Promedio de notas

alumnos = {}

# Cargar 3 alumnos y sus notas 
for i in range(3):
    nombre = input(f"Ingrese el nombre del alumno {i+1}: ")
    
    # Pedimos las 3 notas en una sola línea
    notas_str = input(f"Ingrese las 3 notas de {nombre} (separadas por coma, ej: 8, 9, 7): ")
    
    # Convertimos el string "8, 9, 7" en una lista ["8", " 9", " 7"]
    notas_lista_str = notas_str.split(',')
    
    # Creamos una lista de números (int) limpiando espacios (strip)
    notas_numeros = []
    for nota in notas_lista_str:
        notas_numeros.append(int(nota.strip()))
        
    # Guardamos en el diccionario como una tupla
    alumnos[nombre] = tuple(notas_numeros)

print(f"\nDiccionario de alumnos y notas: {alumnos}")

print("\n--- Promedios ---")
# Mostrar el promedio de cada alumno
for nombre, notas in alumnos.items():
    # 'notas' es la tupla (ej: (8, 9, 7))
    # sum(notas) suma los elementos de la tupla (8+9+7 = 24)
    # len(notas) cuenta cuántos elementos hay (3)
    promedio = sum(notas) / len(notas)
    
    # Usamos :.2f para mostrar el promedio con solo 2 decimales
    print(f"El promedio de {nombre} es: {promedio:.2f}")

# 7. Operaciones con sets

# (Creamos dos sets de ejemplo para probar)
parcial1 = {'Juan', 'Ana', 'Luis', 'Sofia', 'Pedro', 'Maria'}
parcial2 = {'Ana', 'Pedro', 'Maria', 'Carlos', 'Luis', 'Jorge'}

print(f"Aprobaron Parcial 1: {parcial1}")
print(f"Aprobaron Parcial 2: {parcial2}")

# 1. Mostrar los que aprobaron ambos parciales (INTERSECCIÓN) 
# Son los alumnos que están EN parcial1 Y TAMBIÉN EN parcial2
ambos_parciales = parcial1.intersection(parcial2)
# Alternativa: usar el operador &
# ambos_parciales = parcial1 & parcial2
print(f"\nAprobaron ambos parciales: {ambos_parciales}")


# 2. Mostrar los que aprobaron solo uno de los dos (DIFERENCIA SIMÉTRICA) 
# Son los alumnos que están en P1 pero NO en P2, o en P2 pero NO en P1.
solo_un_parcial = parcial1.symmetric_difference(parcial2)
# Alternativa: usar el operador ^
# solo_un_parcial = parcial1 ^ parcial2
print(f"Aprobaron solo uno de los dos parciales: {solo_un_parcial}")


# 3. Mostrar la lista total de estudiantes (UNIÓN) 
# Son todos los alumnos de P1, más todos los de P2, sin repetir nombres.
total_aprobados = parcial1.union(parcial2)
# Alternativa: usar el operador |
# total_aprobados = parcial1 | parcial2
print(f"Total de alumnos que aprobaron al menos un parcial: {total_aprobados}")

# 8. Gestion de Stock de Productos

stock_productos = {'Manzanas': 100, 'Naranjas': 150, 'Peras': 75}

# Creamos un menú que se repita hasta que el usuario decida salir
while True:
    print("\n--- GESTIÓN DE STOCK ---")
    print("1. Consultar stock de un producto")
    print("2. Agregar stock a un producto existente")
    print("3. Agregar un nuevo producto y su stock")
    print("4. Salir")
    
    opcion = input("Seleccione una opción (1-4): ")

    if opcion == '1':
        # 1. Consultar stock 
        producto = input("Ingrese el nombre del producto: ")
        stock_actual = stock_productos.get(producto) # Usamos .get()
        
        if stock_actual is not None:
            print(f"El stock de '{producto}' es: {stock_actual} unidades.")
        else:
            print(f"El producto '{producto}' no existe en el inventario.")

    elif opcion == '2':
        # 2. Agregar unidades si el producto ya existe 
        producto = input("Ingrese el nombre del producto: ")
        if producto in stock_productos:
            try:
                cantidad = int(input(f"¿Cuántas unidades de '{producto}' desea agregar?: "))
                stock_productos[producto] += cantidad
                print(f"Stock actualizado. Nuevo stock de '{producto}': {stock_productos[producto]}")
            except ValueError:
                print("Error: Debe ingresar un número válido.")
        else:
            print(f"El producto '{producto}' no existe. Use la opción 3 para agregarlo.")

    elif opcion == '3':
        # 3. Agregar un nuevo producto si no existe 
        producto = input("Ingrese el nombre del nuevo producto: ")
        if producto not in stock_productos:
            try:
                cantidad = int(input(f"Ingrese el stock inicial para '{producto}': "))
                stock_productos[producto] = cantidad
                print(f"Producto '{producto}' agregado con {cantidad} unidades.")
            except ValueError:
                print("Error: Debe ingresar un número válido.")
        else:
            print(f"El producto '{producto}' ya existe en el inventario.")

    elif opcion == '4':
        print("Saliendo del programa...")
        print(f"Stock final: {stock_productos}")
        break # 'break' rompe el bucle 'while True' y termina el programa

    else:
        print("Opción no válida. Por favor, ingrese un número del 1 al 4.")

# 9. Agenda de Eventos

agenda = {
    ("lunes", "10:00"): "Reunión de equipo",
    ("martes", "15:00"): "Clase de inglés",
    ("miércoles", "09:00"): "Cita con el dentista",
    ("viernes", "18:00"): "Gimnasio"
}

print("--- Consultar Agenda ---")
# Pedimos los datos por separado
dia = input("Ingrese el día (ej: lunes): ").lower() # .lower() para normalizar
hora = input("Ingrese la hora (ej: 10:00): ")

# Creamos la tupla que servirá como clave
clave_consulta = (dia, hora)

# Consultamos la agenda 
# Usamos .get() por si la clave (dia, hora) no existe
evento = agenda.get(clave_consulta)

if evento:
    print(f"El evento para el {dia} a las {hora} es: {evento}")
else:
    print(f"No hay ningún evento programado para el {dia} a las {hora}.")

# 10. Invertir el diccionario

paises_capitales = {
    "Argentina": "Buenos Aires",
    "Chile": "Santiago",
    "Brasil": "Brasilia",
    "Perú": "Lima",
    "Uruguay": "Montevideo"
}

# Creamos el diccionario vacío que vamos a llenar
capitales_paises = {}

# Recorremos el diccionario original
for pais, capital in paises_capitales.items():
    # Invertimos los roles:
    # La 'capital' (valor original) es la nueva clave
    # El 'pais' (clave original) es el nuevo valor
    capitales_paises[capital] = pais

print(f"Diccionario original: {paises_capitales}")
print(f"Diccionario invertido: {capitales_paises}")