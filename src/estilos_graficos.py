import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("data/telemetria_simulada.csv")
# Ver estilos disponíveis
print("Estilos disponíveis:")
print(plt.style.available[:10])  # primeiros 10
# Usar um estilo profissional
plt.style.use("seaborn-v0_8-whitegrid")  # ou "ggplot", "dark_background", etc.
fig, axes = plt.subplots(1, 3, figsize=(15, 5))
# Diferentes tipos de linha
axes[0].plot(df["timestamp"], df["temperatura"], 
             color="#E74C3C",  # cor em hexadecimal
             linewidth=2,
             linestyle="-",    # sólida
             marker="o",       # pontos
             markersize=3,
             markevery=5)      # marcador a cada 5 pontos
axes[0].set_title("Com marcadores")
axes[1].plot(df["timestamp"], df["temperatura"],
             color="#3498DB",
             linewidth=3,
             linestyle="--")   # tracejado
axes[1].set_title("Tracejado")
axes[2].plot(df["timestamp"], df["temperatura"],
             color="#2ECC71",
             linewidth=2,
             linestyle="-.")   # traço-ponto
axes[2].set_title("Traço-ponto")
for ax in axes:
    ax.set_xlabel("Tempo (s)")
    ax.set_ylabel("Temperatura (°C)")
    ax.grid(True, alpha=0.3)
plt.suptitle("Diferentes estilos de linha")
plt.tight_layout()
plt.savefig("docs/estilos_linha.png", dpi=150, bbox_inches="tight")
plt.show()