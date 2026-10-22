import matplotlib.pyplot as plt

ciudades = ["Lima", "Cusco", "Arequipa"]
ventas = [500, 300, 400]

plt.bar(ciudades, ventas)

plt.title("Ventas por ciudad")
plt.xlabel("Ciudad")
plt.ylabel("Ventas")

plt.show()