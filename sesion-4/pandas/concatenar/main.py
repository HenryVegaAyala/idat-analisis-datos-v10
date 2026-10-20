import pandas as pd

# leer cada archivo csv.
df_enero = pd.read_csv('files/ventas_enero_2026.csv')
df_febrero = pd.read_csv('files/ventas_febrero_2026.csv')
df_marzo = pd.read_csv('files/ventas_marzo_2026.csv')

resultado = pd.concat([df_enero, df_febrero, df_marzo], ignore_index=True)

print(resultado)