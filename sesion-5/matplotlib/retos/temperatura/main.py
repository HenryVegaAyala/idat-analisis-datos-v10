import matplotlib.pyplot as plt
from matplotlib.lines import lineStyles

# Datos de temperatura
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
maximas = [25, 28, 26, 30, 31]
minimas = [15, 14, 16, 18, 17]

# Gráfica de líneas para temperaturas máximas y mínimas
plt.plot(dias, maximas, color="orange", label="Maximas", marker="o")

plt.plot(dias, minimas, color="blue", label="Minimas", marker="o")

# Títulos y etiquetas
plt.title("Pronostico del clima")
plt.xlabel("Día")
plt.ylabel("Temperatura")

# Leyenda y grilla
plt.legend()
plt.grid(True, linestyle="--", alpha=0.4)

# Mostrar la gráfica
plt.tight_layout()
plt.show()
