import numpy as np

print(np.__version__)

lista = [1, 2, 3, 4, 5]

resultado = lista * 20
print(resultado)

print("-" * 20)

array = np.array(lista)
resultado = array * 20
print(resultado)
