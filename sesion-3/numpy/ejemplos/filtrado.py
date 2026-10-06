import numpy as np

edades = [15, 20, 18, 12, 30, 25]

array = np.array(edades)

# Filtrado de edades mayores a 18

print(edades)
print(array >= 18)  # Aquí solo se enfoca en filtrar y obtener un array de booleanos

resultado = array[array >= 18]  # Aquí se filtra el array original y se enmascara
print(resultado)
