import pandas as pd
from pathlib import Path

pd.set_option('display.max_columns', None)
pd.set_option("display.max_rows", None)
pd.set_option("display.width", None)

data_dir = (Path(__file__)).resolve().parent / "../dataset.txt"

df = pd.read_csv(data_dir)

resultado = df[df["Store ID"].isin([8091, 8095])]

print(resultado.info())