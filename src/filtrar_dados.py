import pandas as pd

df = pd.read_csv("data/telemetria_simulada.csv")

print(f"Total de leituras: {len(df)}")
print()

# Filtrar: temperaturas abaixo de 20 graus
frio = df[df["temperatura"] < 20]
print(f"Leituras com temperatura < 20°C: {len(frio)}")
print(frio.head())
print()

# Filtrar: altitude acima de 500m
alto = df[df["altitude"] > 500]
print(f"Leituras com altitude > 500m: {len(alto)}")
print(alto.head())
print()

# Filtrar com múltiplas condições (usar & para AND, | para OR)
# Leituras onde temperatura < 20 E altitude > 500
critico = df[(df["temperatura"] < 20) & (df["altitude"] > 500)]
print(f"Leituras críticas (temp<20 E alt>500): {len(critico)}")
print(critico)