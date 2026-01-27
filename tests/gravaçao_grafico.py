import matplotlib.pyplot as plt
import random

plt.ion()  # modo interativo

tempos = []
temperaturas = []
altitudes = []
pressoes = []

temp_atual = 23.5        # °C
altitude_atual = 100.0   # m
pressao_atual = 1013.25  # hPa

fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(8, 8))

for t in range(30):
    tempos.append(t)

    # variações suaves e realistas
    temp_atual += random.uniform(-0.1, 0.1)
    altitude_atual -= random.uniform(0.05, 0.2)
    pressao_atual += random.uniform(-0.3, 0.3)

    temperaturas.append(temp_atual)
    altitudes.append(altitude_atual)
    pressoes.append(pressao_atual)

    ax1.clear()
    ax2.clear()
    ax3.clear()

    # Temperatura
    ax1.plot(tempos, temperaturas, marker="o")
    ax1.set_ylabel("Temperatura (°C)")
    ax1.set_ylim(22, 25)
    ax1.grid(True)

    # Altitude
    ax2.plot(tempos, altitudes, marker="o")
    ax2.set_ylabel("Altitude (m)")
    ax2.set_ylim(90, 102)
    ax2.grid(True)

    # Pressão
    ax3.plot(tempos, pressoes, marker="o")
    ax3.set_xlabel("Tempo (s)")
    ax3.set_ylabel("Pressão (hPa)")
    ax3.set_ylim(1008, 1018)
    ax3.grid(True)

    fig.suptitle("Telemetria do CanSat em tempo real")

    plt.pause(0.3)

plt.ioff()
plt.show()
