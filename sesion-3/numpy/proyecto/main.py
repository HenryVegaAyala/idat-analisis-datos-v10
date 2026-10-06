import numpy as np


class Estudiante:
    def __init__(self, nombre, notas):
        self.nombre = nombre
        self.notas = np.array(notas)

    def calcular_promedio(self):
        return np.mean(self.notas)

    def evaluar(self):
        promedio = self.calcular_promedio()

        if promedio >= 11:
            return f"{self.nombre}: Aprobado con promedio {promedio}"
        else:
            return f"{self.nombre}: Reprobado con promedio {promedio}"


maria = Estudiante("Maria", [14, 18, 15, 12])
resultado = maria.evaluar()
print(resultado)
