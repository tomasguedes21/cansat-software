import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("data/telemetria_simulada.csv")
plt.figure(figsize=(10, 6))
# Gráfico de altitude com área preenchida
plt.fill_between(df["timestamp"], df["altitude"], alpha=0.3, color="blue")
plt.plot(df["timestamp"], df["altitude"], color="blue", linewidth=2)
plt.title("Altitude durante o voo do CanSat")
plt.xlabel("Tempo (segundos)")
plt.ylabel("Altitude (m)")
plt.grid(True, alpha=0.3)
plt.savefig("docs/altitude.png", dpi=150, bbox_inches="tight")
print("Gráfico guardado em docs/altitude.png")
plt.show()