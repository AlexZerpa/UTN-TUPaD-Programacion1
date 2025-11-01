# EJERCICIO 1

def factorial(n):
    """Calcula el factorial de n de forma recursiva."""
    if n == 0:
        return 1  # Caso base
    else:
        return n * factorial(n - 1)  # Caso recursivo

# --- Programa principal ---
try:
    num_usuario = int(input("Ingrese un número entero para calcular factoriales: "))
    
    if num_usuario < 0:
        print("El factorial no está definido para números negativos.")
    else:
        print(f"--- Factoriales desde 1 hasta {num_usuario} ---")
        for i in range(1, num_usuario + 1):
            print(f"Factorial de {i} = {factorial(i)}")

except ValueError:
    print("Error: Por favor, ingrese un número entero válido.")

# EJERCICIO 2

def fibonacci(n):
    """Calcula el valor de Fibonacci en la posición n."""
    if n == 0:
        return 0  # Caso base 1
    elif n == 1:
        return 1  # Caso base 2
    else:
        # Caso recursivo
        return fibonacci(n - 1) + fibonacci(n - 2)

# --- Programa principal ---
try:
    pos_usuario = int(input("Ingrese una posición para la serie de Fibonacci: "))

    if pos_usuario < 0:
        print("La posición debe ser un número positivo.")
    else:
        print(f"--- Serie de Fibonacci hasta la posición {pos_usuario} ---")
        # Iteramos para mostrar cada término de la serie
        for i in range(pos_usuario + 1):
            print(fibonacci(i), end=" ")
        print() # Para un salto de línea al final

except ValueError:
    print("Error: Por favor, ingrese un número entero válido.")

# EJERCICIO 3
def potencia(base, exponente):
    """Calcula la potencia de una base elevada a un exponente."""
    if exponente == 0:
        return 1  # Caso base
    else:
        # Caso recursivo
        return base * potencia(base, exponente - 1)

# --- Programa principal ---
try:
    b = int(input("Ingrese el número base: "))
    e = int(input("Ingrese el exponente: "))

    if e < 0:
        print("Este ejemplo solo funciona con exponentes positivos.")
    else:
        resultado = potencia(b, e)
        print(f"{b} elevado a {e} es: {resultado}")

except ValueError:
    print("Error: Por favor, ingrese números enteros válidos.")

# EJERCICIO 4
def decimal_a_binario(n):
    """Convierte un número decimal a binario como string."""
    # Caso base especial para el 0
    if n == 0:
        return "0"
    else:
        # Función auxiliar para manejar la recursión principal
        return _binario_recursivo(n)

def _binario_recursivo(n):
    """Función auxiliar que maneja la recursión."""
    # Caso base de la recursión: se detiene cuando el cociente es 0
    if n == 0:
        return ""
    else:
        cociente = n // 2
        resto = n % 2
        # Llama recursivamente y concatena el resto al final
        return _binario_recursivo(cociente) + str(resto)

# --- Programa principal ---
try:
    num_decimal = int(input("Ingrese un número decimal positivo: "))

    if num_decimal < 0:
        print("Este ejemplo solo funciona con números positivos.")
    else:
        resultado_binario = decimal_a_binario(num_decimal)
        print(f"El número {num_decimal} en binario es: {resultado_binario}")

except ValueError:
    print("Error: Por favor, ingrese un número entero válido.")

# EJERCICIO 5
def es_palindromo(palabra):
    """Verifica si una palabra es un palíndromo de forma recursiva."""
    
    # Caso base 1: Éxito (palabra vacía o de 1 letra)
    if len(palabra) <= 1:
        return True
    
    # Caso base 2: Fracaso (letras de extremos no coinciden)
    if palabra[0] != palabra[-1]:
        return False
    
    # Caso recursivo: llamar a la función con la sub-palabra interna
    # (desde el segundo carácter hasta el penúltimo)
    return es_palindromo(palabra[1:-1])

# --- Programa principal ---
# Prueba con los ejemplos clásicos
print(f"¿'ana' es palíndromo?: {es_palindromo('ana')}")
print(f"¿'neuquen' es palíndromo?: {es_palindromo('neuquen')}")
print(f"¿'radar' es palíndromo?: {es_palindromo('radar')}")
print(f"¿'python' es palíndromo?: {es_palindromo('python')}")

# EJERCICIO 6
def suma_digitos(n):
    """Suma los dígitos de un número n recursivamente."""
    
    # Caso base: n tiene un solo dígito
    if n < 10:
        return n
    else:
        # Caso recursivo:
        # n % 10 -> obtiene el último dígito
        # n // 10 -> obtiene el número sin el último dígito
        return (n % 10) + suma_digitos(n // 10)

# --- Programa principal ---
# Ejemplos del PDF ...
print(f"Suma de dígitos de 1234: {suma_digitos(1234)}") # 1+2+3+4 = 10
print(f"Suma de dígitos de 9: {suma_digitos(9)}")
print(f"Suma de dígitos de 305: {suma_digitos(305)}") # 3+0+5 = 8

# EJERCICIO 7
def contar_bloques(n):
    """Suma el total de bloques en una pirámide de base n."""
    
    # Caso base: el nivel superior tiene 1 bloque
    if n == 1:
        return 1
    # Caso recursivo: n + el total de una pirámide de (n-1)
    else:
        return n + contar_bloques(n - 1)

# --- Programa principal ---
# Ejemplos del PDF [cite: 55, 57, 58]
print(f"Bloques en pirámide de base 1: {contar_bloques(1)}") # 1
print(f"Bloques en pirámide de base 2: {contar_bloques(2)}") # 2+1 = 3
print(f"Bloques en pirámide de base 4: {contar_bloques(4)}") # 4+3+2+1 = 10

# EJERCICIO 8
def contar_digito(numero, digito):
    """Cuenta cuántas veces aparece 'digito' en 'numero'."""
    
    # Caso base: el número tiene un solo dígito
    if numero < 10:
        return 1 if numero == digito else 0
    
    # Caso recursivo
    # 1. Contamos si el último dígito coincide
    conteo_ultimo = 0
    if (numero % 10) == digito:
        conteo_ultimo = 1
        
    # 2. Sumamos el conteo (0 o 1) al resultado de la recursión 
    #    con el resto del número (numero // 10)
    return conteo_ultimo + contar_digito(numero // 10, digito)

# --- Programa principal ---
# Ejemplos del PDF...
print(f"Contar (12233421, 2): {contar_digito(12233421, 2)}") # 3
print(f"Contar (5555, 5): {contar_digito(5555, 5)}")       # 4
print(f"Contar (123456, 7): {contar_digito(123456, 7)}") # 0
print(f"Contar (100, 0): {contar_digito(100, 0)}")         # 2
