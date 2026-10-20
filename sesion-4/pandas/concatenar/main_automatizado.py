import pandas as pd
import glob

# buscar todos los archivos con extension .csv en la carpeta files

buscar_archivos = glob.glob("files/ventas_*.csv")

print(f"Se encontraron {len(buscar_archivos)} archivos")

data_frames = []  # Variable temporal de información
for archivo in buscar_archivos:
    df = pd.read_csv(archivo) # Leer el archivo csv encontrado
    data_frames.append(df) # Agregar el resultado en el dataframe

consolidado = pd.concat(data_frames, ignore_index=True)

print(consolidado)