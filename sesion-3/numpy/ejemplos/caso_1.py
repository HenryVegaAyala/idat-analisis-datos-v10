import numpy as np

# Crear un array de ejemplo
data = np.array([10, 20, 30, 40, 50])

sub = data[1:4] # Subarray que contiene los elementos desde el índice 1 hasta el índice 3

print(sub)
# [20 30 40]
#  0  1  2

sub[0] = 999

print(sub)
# [999  30  40]

print(data.copy())