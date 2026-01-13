import pandas as pd

df = pd.read_csv("data/telemetria.csv")

# Selecionar uma coluna (retorna uma Series)
temperaturas = df["temperatura"]
print("Coluna temperatura:")
print(temperaturas)
print(f"Tipo: {type(temperaturas)}")
print()

# Selecionar várias colunas (retorna um DataFrame)
subset = df[["timestamp", "temperatura"]]
print("Duas colunas:")
print(subset)
print()

# Selecionar uma linha pelo índice
primeira_linha = df.iloc[0]  # iloc = index location
print("Primeira linha:")
print(primeira_linha)
print()

# Selecionar um valor específico
temp_segundo = df.iloc[1]["temperatura"]  # linha 1, coluna temperatura
print(f"Temperatura no segundo 1: {temp_segundo}")