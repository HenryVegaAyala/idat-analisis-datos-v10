import pandas as pd
import scipy.stats as st

df = pd.read_csv("tiempos.csv")

vehiculo_electrico = df[df["vehiculo"] == "Electrica"]["minutos"]
vehiculo_tradicional = df[df["vehiculo"] == "Tradicional"]["minutos"]

ic_electrico = st.t.interval(
    0.95,
    len(vehiculo_electrico) - 1,
    loc=vehiculo_electrico.mean(),
    scale=st.sem(vehiculo_electrico),
)

ic_tradicional = st.t.interval(
    0.95,
    len(vehiculo_tradicional) - 1,
    loc=vehiculo_tradicional.mean(),
    scale=st.sem(vehiculo_tradicional)
)

print(f"Intervalo de confianza para el tiempo del "
      f"vehiculo eléctrico: {ic_electrico[0]:.2f} - {ic_electrico[1]:.2f} minutos")

print(f"Intervalo de confianza para el tiempo del "
      f"vehiculo tradicional: {ic_tradicional[0]:.2f} - {ic_tradicional[1]:.2f} minutos")

resultado = st.ttest_ind(vehiculo_tradicional, vehiculo_electrico)

if resultado.pvalue < 0.05:
    print("Se rechaza la hipótesis nula. Hay una diferencia significativa "
          "entre los tiempos de los vehículos eléctricos y tradicionales.")
else:
    print("No se rechaza la hipótesis nula. No hay una diferencia significativa "
          "entre los tiempos de los vehículos eléctricos y tradicionales.")