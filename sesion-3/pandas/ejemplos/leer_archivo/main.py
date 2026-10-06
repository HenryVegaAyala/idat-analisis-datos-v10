import pandas as pd

df = pd.read_csv('ventas_enero_2026.csv')
print(df)

print("-" * 30)

df = pd.read_excel('Estudiantes - 682129 (1).xlsx')
print(df)

print("-" * 30)

df = pd.read_excel("Multiples_hojas.xlsx", sheet_name='Notas')
print(df)