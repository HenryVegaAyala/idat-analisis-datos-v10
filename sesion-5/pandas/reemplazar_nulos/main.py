import pandas as pd

df = pd.read_csv('productos.csv')

df["cantidad"] = df["cantidad"].fillna(0)
print(df)

print("*" * 20)

df["precio_unitario"] = df["precio_unitario"].fillna(df["precio_unitario"].mean())
print(df)