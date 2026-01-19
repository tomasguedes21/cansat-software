import pandas as pd
import matplotlib.pyplot as plt
# Carregar dados
df = pd.read_csv("data/telemetria_simulada.csv")
# Criar gráfico de linha
plt.plot(df["timestamp"], df["temperatura"])
# Mostrar
plt.show()