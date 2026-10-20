import pandas as pd
from pathlib import Path

data_dir = (Path(__file__)).resolve().parent / "../dataset.txt"

df = pd.read_csv(data_dir)

# filtrado = df[df["Store ID"] == 8091]  # Filtrado simple

filtrado = df[
    (df["Store ID"] == 8091) # Primera condición
    & # conector condicional
    (df["Units Sold"] > 30) # Segunda condición
    ]

print(filtrado.info())
