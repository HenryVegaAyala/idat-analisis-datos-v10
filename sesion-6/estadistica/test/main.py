import pandas as pd
import scipy.stats as st

data = pd.read_csv('satisfaccion.csv')

grupo_a = data[data["embalaje"] == "A"]["puntuacion"]
grupo_b = data[data["embalaje"] == "B"]["puntuacion"]

resultado = st.ttest_ind(grupo_a, grupo_b)

print("Estadístico t:", resultado.pvalue)

if resultado.pvalue < 0.05:
    print("Rechazamos la hipótesis nula: hay diferencias significativas entre los grupos.")
else:
    print("No rechazamos la hipótesis nula: no hay diferencias significativas entre los grupos.")