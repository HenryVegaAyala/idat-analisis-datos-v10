import pandas as pd

data = [10, 12, 0, 10, 11, None, 85, 11, 0]

resultado = pd.Series(data)

# Reemplazar valor None por una mediana
resultado.fillna(resultado.median(), inplace=True)

print(resultado)

# Ejemplo de imputar.
respuesta = resultado.replace(0, resultado.median())
print(f"respuesta: {respuesta}")

# filtrar valores menores a 18
data_limpia = respuesta[resultado < 18]
print(f"data_limpia: {data_limpia}")