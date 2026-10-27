import pandas as pd
from sklearn.linear_model import LinearRegression

# Cargar los datos desde un archivo CSV
df = pd.read_csv("../ampliados/datos_salarios_ampliado.csv")

# Seleccionar las características (X) y la variable objetivo (y)
X = df[['experiencia', 'estudios']]
y = df['salario']

# Crear el modelo de regresión lineal
model = LinearRegression()
model.fit(X, y)

# Hacer predicciones
nuevo = pd.DataFrame({'experiencia': [4], 'estudios': [5]})
prediccion = model.predict(nuevo)

print(f"Predicción del salario para 4 años de experiencia "
      f"y 5 años de estudios: {prediccion[0]:.2f}")