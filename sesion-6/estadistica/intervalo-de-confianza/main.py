import pandas as pd
import scipy.stats as st

data = pd.read_csv('gastos.csv')

gasto = data["gasto"]

ic = st.t.interval(
    0.95, # Intervalo de confianza del 95%
    len(data) - 1, # Grados de libertad
    loc=gasto.mean(), # Media de la muestra
    scale=st.sem(gasto) # Error estándar de la media
)

print(f"Entre s/{ic[0]:.2f}y S/{ic[1]:.2f} con un 95% de confianza.")