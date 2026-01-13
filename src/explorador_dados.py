import pandas as pd

df = pd.read_csv("data/telemetria.csv")

# Ver as primeiras linhas
print("=== Primeiras 2 linhas (head) ===")
print(df.head(2))
print()

# Ver as últimas linhas
print("=== Últimas 2 linhas (tail) ===")
print(df.tail(2))
print()

# Informação sobre o DataFrame
print("=== Informação (info) ===")
print(df.info())
print()

# Estatísticas básicas
print("=== Estatísticas (describe) ===")
print(df.describe())