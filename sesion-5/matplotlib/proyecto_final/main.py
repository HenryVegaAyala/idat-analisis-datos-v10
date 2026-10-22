import marshal
import pandas as pd
import matplotlib.pyplot as plt

# 1. Cargar los datos desde un archivo CSV
mensual = pd.read_csv('datos/ventas_mensuales.csv')
ciudades = pd.read_csv('datos/ventas_ciudad.csv')
clientes = pd.read_csv('datos/clientes.csv')
publicidad = pd.read_csv('datos/publicidad.csv')
gastos = pd.read_csv('datos/gastos_categoria.csv')

# 2. ingresos vs gastos
plt.figure()
plt.plot(mensual["mes"], mensual["ingresos"], label="Ingresos", color="green", marker="o")
plt.plot(mensual["mes"], mensual["gastos"], label="Gastos", color="red", marker="o")
plt.title("Ingresos vs Gastos 2026")
plt.xlabel("Mes")
plt.ylabel("Monto (S/)")
plt.legend()
plt.savefig("salidas/ingresos_vs_gastos.png")
plt.close()

plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.plot(mensual["mes"], mensual["ingresos"], label="Ingresos", color="green", marker="o")
plt.plot(mensual["mes"], mensual["gastos"], label="Gastos", color="red", marker="o")
plt.title("Ingresos vs Gastos 2026")
plt.xlabel("Mes")
plt.ylabel("Monto (S/)")
plt.legend()

plt.subplot(2, 2, 2)
plt.bar(ciudades["ciudad"], ciudades["ventas"], color="blue")
plt.title("Ventas por Ciudad 2026")

plt.subplot(2, 2, 3)
plt.hist(clientes["edad"], bins=8, color="orange", edgecolor="black")
plt.title("Distribución de Edad de Clientes 2026")
plt.xlabel("Edad")
plt.ylabel("Frecuencia")

plt.tight_layout()
plt.savefig("salidas/tablero.png", dpi=300)
plt.close()