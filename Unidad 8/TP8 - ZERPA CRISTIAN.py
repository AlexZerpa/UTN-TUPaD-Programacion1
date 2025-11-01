import os

# Nombre del archivo
NOMBRE_ARCHIVO = 'productos.txt'

def cargar_productos():
    """
    Lee el archivo productos.txt y lo carga en una lista de diccionarios.
    Cumple con las Actividades 2 (leer) y 4 (cargar en lista de diccionarios).
    """
    productos = []
    if not os.path.exists(NOMBRE_ARCHIVO):
        print(f"Error: El archivo {NOMBRE_ARCHIVO} no existe. Creándolo vacío.")
        # Creamos el archivo vacío para que el resto del programa funcione
        open(NOMBRE_ARCHIVO, 'w').close()
        return productos

    # Usamos 'with open()' como buena práctica 
    try:
        with open(NOMBRE_ARCHIVO, 'r', encoding='utf-8') as f:
            for linea in f:
                # Procesamos la línea con .strip() y .split() 
                datos = linea.strip().split(',')
                
                # Validamos que la línea tenga 3 datos
                if len(datos) == 3:
                    try:
                        # Creamos el diccionario (Actividad 4) 
                        producto = {
                            'nombre': datos[0],
                            'precio': float(datos[1]),
                            'cantidad': int(datos[2])
                        }
                        productos.append(producto)
                    except ValueError:
                        print(f"Advertencia: Omitiendo línea mal formada: {linea.strip()}")
                else:
                    print(f"Advertencia: Omitiendo línea con formato incorrecto: {linea.strip()}")

    except IOError as e:
        print(f"Error al leer el archivo: {e}")
    
    return productos

def mostrar_productos(lista_productos):
    """
    Muestra los productos de la lista con el formato solicitado.
    Cumple con la Actividad 2 (mostrar).
    """
    print("\n--- Lista de Productos ---")
    if not lista_productos:
        print("No hay productos para mostrar.")
        return
        
    for p in lista_productos:
        # Formato solicitado en la Actividad 2 
        print(f"Producto: {p['nombre']} | Precio: ${p['precio']} | Cantidad: {p['cantidad']}")
    print("----------------------------")

def agregar_producto(lista_productos):
    """
    Pide un nuevo producto y lo agrega al archivo Y a la lista en memoria.
    Cumple con la Actividad 3.
    """
    print("\n--- Agregar Nuevo Producto ---")
    try:
        # Pedimos los datos al usuario 
        nombre = input("Ingrese nombre del producto: ")
        precio = float(input("Ingrese precio: "))
        cantidad = int(input("Ingrese cantidad: "))
        
        # Abrimos el archivo en modo 'a' (append) para agregar sin borrar lo existente
        with open(NOMBRE_ARCHIVO, 'a', encoding='utf-8') as f:
            f.write(f"\n{nombre},{precio},{cantidad}")
            
        # Actualizamos también la lista en memoria
        lista_productos.append({'nombre': nombre, 'precio': precio, 'cantidad': cantidad})
        print(f"¡Producto '{nombre}' agregado con éxito!")

    except ValueError:
        print("Error: Precio y cantidad deben ser números. Intente de nuevo.")
    except IOError as e:
        print(f"Error al guardar el producto: {e}")

def buscar_producto(lista_productos):
    """
    Busca un producto por nombre en la lista de diccionarios.
    Cumple con la Actividad 5.
    """
    print("\n--- Buscar Producto ---")
    nombre_buscar = input("Ingrese el nombre del producto a buscar: ")
    
    encontrado = None
    for p in lista_productos: # Recorrer la lista 
        if p['nombre'].lower() == nombre_buscar.lower():
            encontrado = p
            break
            
    if encontrado:
        print("Producto encontrado:")
        print(f"  Nombre: {encontrado['nombre']}")
        print(f"  Precio: ${encontrado['precio']}")
        print(f"  Cantidad: {encontrado['cantidad']}")
    else:
        # Mensaje de error si no existe 
        print(f"Error: Producto '{nombre_buscar}' no encontrado.")

def guardar_productos(lista_productos):
    """
    Sobrescribe el archivo productos.txt con la lista actualizada.
    Cumple con la Actividad 6.
    """
    # Abrimos en modo 'w' (write) para sobrescribir 
    try:
        with open(NOMBRE_ARCHIVO, 'w', encoding='utf-8') as f:
            for i, p in enumerate(lista_productos):
                linea = f"{p['nombre']},{p['precio']},{p['cantidad']}"
                f.write(linea)
                # Añadir salto de línea salvo en la última línea
                if i < len(lista_productos) - 1:
                    f.write("\n")
        
        print(f"Datos guardados correctamente en {NOMBRE_ARCHIVO}.")
    except IOError as e:
        print(f"Error al guardar los datos: {e}")


def main():
    """
    Función principal que ejecuta el menú del programa.
    """
    # Cargamos los productos del archivo al iniciar
    lista_de_productos = cargar_productos()
    
    while True:
        print("\n===== GESTIÓN DE PRODUCTOS =====")
        print("1. Mostrar todos los productos")
        print("2. Agregar un producto")
        print("3. Buscar un producto")
        print("4. Guardar cambios y salir")
        print("5. Salir sin guardar")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            mostrar_productos(lista_de_productos)
        
        elif opcion == '2':
            agregar_producto(lista_de_productos)
        
        elif opcion == '3':
            buscar_producto(lista_de_productos)
            
        elif opcion == '4':
            # Actividad 6: Guardar los productos actualizados 
            guardar_productos(lista_de_productos)
            print("¡Adiós!")
            break
            
        elif opcion == '5':
            print("Saliendo sin guardar cambios. ¡Adiós!")
            break
            
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

# Punto de entrada del programa
if __name__ == "__main__":
    main()