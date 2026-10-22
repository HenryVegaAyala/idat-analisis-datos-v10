import pandas as pd

df = pd.read_csv('productos.csv')

print(df.isna().sum())
print(df.isna().sum().sum())