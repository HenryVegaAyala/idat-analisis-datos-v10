def convertir_soles(usd, cambio=3.80):
    return usd * cambio

# Caso 1 - Posicionales
resultado = convertir_soles(100, 3.75)
print(resultado)

# Caso 2 - Valor por defecto
resultado = convertir_soles(100)
print(resultado)

# Caso 3 - Argumentos nombrados
resultado = convertir_soles(cambio=3.85, usd=100)
print(resultado)