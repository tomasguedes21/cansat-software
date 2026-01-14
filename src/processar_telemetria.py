import pandas as pd

# Carregar dados
df = pd.read_csv("data/telemetria_simulada.csv")

# Processar: adicionar colunas calculadas
df["temperatura_f"] = df["temperatura"] * 9/5 + 32
df["variacao_altitude"] = df["altitude"].diff().fillna(0)  # fillna(0) para a primeira linha

def classificar_fase(row):
    if row["altitude"] < 200:
        return "lancamento"
    elif row["altitude"] < 600:
        return "subida"
    else:
        return "alta_altitude"

df["fase"] = df.apply(classificar_fase, axis=1)

# Guardar dados processados
df.to_csv("data/telemetria_processada.csv", index=False)
print("Dados processados guardados em data/telemetria_processada.csv")
print()
print(df.head(10))