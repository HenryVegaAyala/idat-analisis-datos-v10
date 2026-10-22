import matplotlib.pyplot as plt

horas = [1, 2, 3, 4, 5]
tazas_vendidas = [10, 20, 25, 30, 40]

plt.plot(horas, tazas_vendidas)
plt.title("Tazas vendidas por hora")
plt.xlabel("Horas de día")
plt.ylabel("Tazas vendidas por hora")
plt.show()