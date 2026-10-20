import pandas as pd
from pathlib import Path

data_dir = (Path(__file__)).resolve().parent / "../dataset.txt"

df = pd.read_csv(data_dir)

resultado = (
    df.groupby("Store ID")["Total Price"]
    .sum()
    .rename("Total Price by Store ID")
    .reset_index()
)

print(resultado)
