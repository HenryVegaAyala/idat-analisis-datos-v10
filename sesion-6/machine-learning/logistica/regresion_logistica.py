import pandas as pd
from sklearn.linear_model import LogisticRegression

# Cargar el conjunto de datos
df = pd.read_csv('../ampliados/datos_fuga_ampliado.csv')

# Seleccionar las características y la variable objetivo
X = df[['antiguedad', 'cuota_mensual']]
y = df['fuga']

# Crear el modelo de regresión logística
model = LogisticRegression()
model.fit(X, y)

# Realizar predicciones
nuevo = pd.DataFrame({"antiguedad": [3], "cuota_mensual": [50]})

# Predecir la probabilidad de fuga
probabilidad_fuga = model.predict(nuevo)

if probabilidad_fuga[0] == 1:
    print("El cliente tiene una alta probabilidad de fuga.")
else:
    print("El cliente tiene una baja probabilidad de fuga.")