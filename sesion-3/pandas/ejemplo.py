import pandas as pd

registro = {
    "Nombre": ["Juan", "María", "Pedro", "Ana"],
    "Edad": [25, 30, 35, 28]
}

df = pd.DataFrame(registro)

print(df)

print("-----------------")

ventas = pd.Series([100, 200, 300, 400])

print(ventas)