import pandas as pd
from sklearn.linear_model import LinearRegression

# Cargar los datos desde un archivo CSV
df = pd.read_csv('../ampliados/datos_marketing_ampliado.csv')

X = df[["marketing"]] # es un dataframe
y = df["ventas"] # es una serie

# Crear el modelo de regresión lineal
modelo = LinearRegression()
modelo.fit(X, y)

# Realizar predicciones
valor_a_consultar = input("Introduce el valor de marketing para predecir las ventas: ") # Dinámico y se ingresa por teclado
consultar_prediccion = pd.DataFrame({"marketing": [valor_a_consultar]})

# Predicción de ventas para el valor de marketing ingresado
prediccion = modelo.predict(consultar_prediccion)

print(f"La predicción de ventas para un valor de "
      f"marketing de {consultar_prediccion['marketing'][0]} es: {prediccion[0]}")