import pandas as pd

df = pd.read_csv("data/telemetria_simulada.csv")

# Primeiro, vamos adicionar a coluna de fase
def classificar_fase(row):
    if row["altitude"] < 200:
        return "lancamento"
    elif row["altitude"] < 600:
        return "subida"
    else:
        return "alta_altitude"

df["fase"] = df.apply(classificar_fase, axis=1)

# Agrupar por fase e calcular estatísticas
print("=== Estatísticas por fase do voo ===")
estatisticas = df.groupby("fase").agg({
    "temperatura": ["mean", "min", "max"],
    "pressao": ["mean", "min", "max"],
    "altitude": ["count", "min", "max"]
})
print(estatisticas)
print()

# Versão mais simples: média por fase
print("=== Média por fase ===")
medias = df.groupby("fase")[["temperatura", "pressao"]].mean()
print(medias)