import matplotlib.pyplot as plt

tienda_a = [10, 15, 20]
tienda_b = [5, 25, 10]

plt.plot(tienda_a, label="Tienda norte")
plt.plot(tienda_b, label="Tienda sur")
plt.legend()

plt.title("Comparación de ventas por tienda")
plt.xlabel("Meses")
plt.ylabel("Ventas")

plt.grid(True)

plt.show()
