import pandas as pd

data = [20, 22, 22, 25, 61]

resultado = pd.Series(data)

media = resultado.mean()
print(f"La media es: {media}")

mediana = resultado.median()
print(f"La mediana es: {mediana}")

moda = resultado.mode()
print(f"La moda es: {moda.values[0]}")