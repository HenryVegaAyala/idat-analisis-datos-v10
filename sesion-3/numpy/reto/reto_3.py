import numpy as np

ventas = [1500, 2300, 1800, 2100, 2500]

total = np.sum(ventas)
promedio = np.mean(ventas)
maximo = np.max(ventas)

print(f"Total de ventas: {total}")
print(f"Promedio de ventas: {promedio}")
print(f"Venta máxima: {maximo}")

listado_ventas = np.array(ventas)

# Filtrado de ventas
sobre = listado_ventas[listado_ventas > promedio]

print(f"Ventas sobre el promedio: {sobre.size}")