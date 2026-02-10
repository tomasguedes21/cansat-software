import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("data/telemetria_simulada.csv")
fig, ax1 = plt.subplots(figsize=(12, 6))
# Primeiro eixo Y (esquerda) - Temperatura
color1 = "red"
ax1.set_xlabel("Tempo (segundos)")
ax1.set_ylabel("Temperatura (°C)", color=color1)
ax1.plot(df["timestamp"], df["temperatura"], color=color1, linewidth=2)
ax1.tick_params(axis="y", labelcolor=color1)
# Segundo eixo Y (direita) - Pressão
ax2 = ax1.twinx()  # eixo Y partilhando o mesmo X
color2 = "blue"
ax2.set_ylabel("Pressão (hPa)", color=color2)
ax2.plot(df["timestamp"], df["pressao"], color=color2, linewidth=2)
ax2.tick_params(axis="y", labelcolor=color2)
plt.title("Temperatura e Pressão durante o voo")
fig.tight_layout()
plt.savefig("docs/temp_pressao_dois_eixos.png", dpi=150, bbox_inches="tight")
plt.show()