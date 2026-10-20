import pandas as pd
from pathlib import Path

data_dir = (Path(__file__)).resolve().parent / "../dataset.txt"

df = pd.read_csv(data_dir)

df["impuesto"] = df["Total Price"] * 0.18
df["valor_estático"] = 0

print(df.head())