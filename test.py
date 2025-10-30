# 10. Invertir diccionario
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