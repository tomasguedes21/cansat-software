import time
import random
from protocolo import criar_mensagem


class SimuladorCanSat:
    def __init__(self, altitude_max=800):
        # Tempo
        self.timestamp = 0

        # Altitude
        self.altitude = 0.0
        self.altitude_max = altitude_max
        self.subida = True

        # Condições ao nível do mar
        self.T0 = 20.0       # ºC
        self.P0 = 1013.25    # hPa

        # Valores iniciais
        self.temperatura = self.T0
        self.pressao = self.P0

    def atualizar(self):
        """Simula 1 segundo de voo"""

        # Atualizar tempo
        self.timestamp += 1

        # Simular subida e descida
        if self.subida:
            self.altitude += random.uniform(5, 10)
            if self.altitude >= self.altitude_max:
                self.subida = False
        else:
            self.altitude -= random.uniform(5, 10)
            if self.altitude < 0:
                self.altitude = 0

        # Modelo físico da temperatura (com ruído)
        self.temperatura = self.T0 - (self.altitude / 1000) * 6.5
        self.temperatura += random.uniform(-0.3, 0.3)

        # Modelo físico da pressão (com ruído)
        self.pressao = self.P0 * (1 - self.altitude / 44330) ** 5.255
        self.pressao += random.uniform(-1.0, 1.0)

    def criar_mensagem(self):
        """Cria mensagem no formato do protocolo"""
        return criar_mensagem(
            self.timestamp,
            round(self.temperatura, 2),
            round(self.pressao, 2),
            round(self.altitude, 2)
        )


def main():
    simulador = SimuladorCanSat(altitude_max=800)

    with open("data/telemetria_simulada.txt", "w", encoding="utf-8") as f:
        for _ in range(120):  # missão de 120 segundos
            simulador.atualizar()
            mensagem = simulador.criar_mensagem()
            f.write(mensagem + "\n")
            print(mensagem)
            time.sleep(1)


if __name__ == "__main__":
    main()
