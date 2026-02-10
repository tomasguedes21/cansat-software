import pandas as pd
import matplotlib.pyplot as plt

# =========================
# 1. Carregar dados
# =========================
df = pd.read_csv("data/telemetria_simulada.csv")

# =========================
# 2. Processamento de dados
# =========================

# Variação de altitude (diferença entre leituras)
df["variacao_altitude"] = df["altitude"].diff().fillna(0)

# Velocidade vertical (m/s) – assumindo 1 segundo entre leituras
df["velocidade_vertical"] = df["variacao_altitude"]

# Classificação da fase do voo
def classificar_fase(row):
    if row["altitude"] < 200:
        return "lancamento"
    elif row["altitude"] < 600:
        return "subida"
    else:
        return "alta_altitude"

df["fase"] = df.apply(classificar_fase, axis=1)

# =========================
# 3. Criar dashboard
# =========================
fig, axs = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle("Dashboard da Missão CanSat", fontsize=16)

# -------------------------
# Gráfico 1 – Perfil do voo
# -------------------------
axs[0, 0].plot(df["timestamp"], df["altitude"])
axs[0, 0].set_title("Perfil do Voo")
axs[0, 0].set_xlabel("Tempo (s)")
axs[0, 0].set_ylabel("Altitude (m)")
axs[0, 0].grid(True)

# -------------------------
# Gráfico 2 – Condições atmosféricas
# -------------------------
axs[0, 1].plot(df["timestamp"], df["temperatura"], label="Temperatura (°C)")
axs[0, 1].plot(df["timestamp"], df["pressao"], label="Pressão (hPa)")
axs[0, 1].set_title("Condições Atmosféricas")
axs[0, 1].set_xlabel("Tempo (s)")
axs[0, 1].legend()
axs[0, 1].grid(True)

# -------------------------
# Gráfico 3 – Análise de dados
# -------------------------
axs[1, 0].plot(df["timestamp"], df["velocidade_vertical"])
axs[1, 0].set_title("Velocidade Vertical ao Longo do Tempo")
axs[1, 0].set_xlabel("Tempo (s)")
axs[1, 0].set_ylabel("Velocidade (m/s)")
axs[1, 0].grid(True)

# -------------------------
# Gráfico 4 – Estatísticas
# -------------------------
medias_por_fase = df.groupby("fase")["velocidade_vertical"].mean()

axs[1, 1].bar(medias_por_fase.index, medias_por_fase.values)
axs[1, 1].set_title("Velocidade Vertical Média por Fase")
axs[1, 1].set_ylabel("Velocidade Média (m/s)")
axs[1, 1].grid(axis="y")

# Ajustar layout
plt.tight_layout(rect=[0, 0, 1, 0.96])

# =========================
# 4. Guardar imagem
# =========================
plt.savefig("docs/dashboard_missao.png", dpi=300)
plt.close()

print("Dashboard guardado em docs/dashboard_missao.png")
