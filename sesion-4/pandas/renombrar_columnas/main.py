import pandas as pd
from pathlib import Path

data_dir = (Path(__file__)).resolve().parent / "../dataset.txt"

df = pd.read_csv(data_dir)

print(df.head(1))

df = df.rename(columns={"Total Price": "Total"})

print(df.head(1))