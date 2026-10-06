import pandas as pd

df = pd.read_excel("Estudiantes - 682129 (1).xlsx")

print(df.info())

# Seleccionar columnas específicas
resultado = df["Nombres"]

print(resultado.head(5))

# Seleccionar multiples columnas específicas
resultado = df[["Nombres", "Estado"]]

print(resultado.head(5))