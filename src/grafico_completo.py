import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("data/telemetria_simulada.csv")
# Criar figura com tamanho específico
plt.figure(figsize=(10, 6))
# Plotar com label para a legenda
plt.plot(df["timestamp"], df["temperatura"], label="Temperatura")
# Adicionar títulos
plt.title("Temperatura durante o voo do CanSat")
plt.xlabel("Tempo (segundos)")
plt.ylabel("Temperatura (°C)")
# Adicionar legenda
plt.legend()
# Adicionar grelha
plt.grid(True, alpha=0.3)
# Mostrar
plt.show()