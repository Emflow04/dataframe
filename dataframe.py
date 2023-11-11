import pandas as pd

data_json = pd.read_json("fuentes/equipos.json")

data_excel = pd.read_excel("fuentes/equipos.xlsx", engine="openpyxl")

data_csv = pd.read_csv("fuentes/equipos.csv")

equipo_df = pd.concat([data_json, data_excel, data_csv], ignore_index=True)

print(equipo_df)
