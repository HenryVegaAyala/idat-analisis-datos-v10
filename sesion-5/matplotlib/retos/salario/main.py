import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('salarios.csv')

plt.bar(df["nombre"], df["sueldo"], color=["red", "#113355", "green", "orange"])

plt.title("salarios")
plt.xlabel("nombre")
plt.ylabel("sueldo")

plt.show()
