import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("data/telemetria_simulada.csv")
plt.figure(figsize=(10, 6))
plt.plot(df["timestamp"], df["temperatura"], color="red", linewidth=2)
plt.title("Temperatura durante o voo do CanSat")
plt.xlabel("Tempo (segundos)")
plt.ylabel("Temperatura (°C)")
plt.grid(True, alpha=0.3)
# Guardar como PNG
plt.savefig("docs/temperatura.png", dpi=150, bbox_inches="tight")
print("Gráfico guardado em docs/temperatura.png")
# Também podes mostrar
plt.show()