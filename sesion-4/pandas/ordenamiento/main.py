import pandas as pd
from pathlib import Path

data_dir = (Path(__file__)).resolve().parent / "../dataset.txt"

df = pd.read_csv(data_dir)

# ordenamiento de una columna específica
resultado = df["Store ID"].sort_values()
# print(resultado)

# ordenamiento de varias del dataframe
resultado = df.sort_values(["Store ID"])
print(resultado)