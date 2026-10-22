import pandas as pd

df = pd.read_csv('productos.csv')

df["precio_total"] = df["cantidad"] * df["precio_unitario"]

df.to_csv("consolidado_productos.csv", index=False)

df.to_excel("consolidado_productos.xlsx", index=False)