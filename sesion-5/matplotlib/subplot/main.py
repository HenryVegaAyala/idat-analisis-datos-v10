import matplotlib.pyplot as plt

# Crear una figura y un eje
plt.subplot(2, 2, 1)
plt.title("1. lineas")
plt.plot([1, 2, 3], [1, 4, 9])

plt.subplot(2, 2, 2)
plt.title("2. barras")
plt.bar([1, 2, 3], [1, 4, 9])

plt.subplot(2, 2, 3)
plt.title("3. dispersión")
plt.scatter([1, 2, 3], [1, 4, 9])

plt.subplot(2, 2, 4)
plt.title("4. pastel")
plt.pie([1, 4, 9], labels=["A", "B", "C"])

# Ajustar el espacio entre subplots
plt.tight_layout()

# Mostrar la figura
plt.show()