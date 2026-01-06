# Simular a recolha de dados até atingir uma condição
import time

altitude = 100
pressao = 1013.25

print("Inicio da missão de simulação")

while altitude > 0:
    # Simula descida
    altitude = altitude - 5
    pressao = pressao + 2.5

    print(f"Altitude: {altitude}m | Pressão: {pressao} hPa")

    # Pausa de 0.5 segundos (simula tempo real)
    time.sleep(0.5)

print("Aterragem!")