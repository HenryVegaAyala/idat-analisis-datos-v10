import pandas as pd

df = pd.read_csv('productos.csv')

resultado = df.dropna()
print(resultado)

print("*" * 20)

resultado_por_columna = df.dropna(subset=["cantidad"])
print(resultado_por_columna)
