from json import encoder

import pandas as pd

df = pd.read_csv('datos_latin1.csv', encoding='latin-1')

print(df)