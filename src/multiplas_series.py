import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("data/telemetria_simulada.csv")
plt.figure(figsize=(12, 6))
# Plotar temperatura e pressão no mesmo gráfico
# Problema: têm escalas muito diferentes!
plt.plot(df["timestamp"], df["temperatura"], label="Temperatura (°C)", color="red")
plt.plot(df["timestamp"], df["pressao"], label="Pressão (hPa)", color="blue")
plt.title("Temperatura e Pressão (escalas diferentes - difícil de ler!)")
plt.xlabel("Tempo (segundos)")
plt.legend()
plt.grid(True, alpha=0.3)
plt.savefig("docs/temp_pressao_problema.png", dpi=150, bbox_inches="tight")
plt.show()