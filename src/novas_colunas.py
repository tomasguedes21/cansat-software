import pandas as pd

df = pd.read_csv("data/telemetria_simulada.csv")

# Criar coluna: temperatura em Fahrenheit
df["temperatura_f"] = df["temperatura"] * 9/5 + 32

# Criar coluna: variação de altitude (diferença para a leitura anterior)
df["variacao_altitude"] = df["altitude"].diff()

# Criar coluna: velocidade vertical (m/s) - variação / tempo (1 segundo)
df["velocidade_vertical"] = df["variacao_altitude"]  # já está em m/s

# Criar coluna: classificação de fase do voo
def classificar_fase(row):
    if row["altitude"] < 200:
        return "lancamento"
    elif row["altitude"] < 600:
        return "subida"
    else:
        return "alta_altitude"

df["fase"] = df.apply(classificar_fase, axis=1)

print(df[["timestamp", "altitude", "variacao_altitude", "fase"]].head(10))
print()
print(df[["timestamp", "altitude", "variacao_altitude", "fase"]].tail(10))