import pandas as pd

df = pd.read_excel("Estudiantes - 682129 (1).xlsx")

print(df.head(10))  # Muestra las primeras 10 filas del DataFrame
print(df.tail(5)) # Muestra las últimas 5 filas del DataFrame
print(df.sample(5)) # Muestra 5 filas aleatorias del DataFrame