import random
from datetime import datetime

def gerar_leitura(segundo):
    """
    Gera uma leitura simulada de telemetria.
    Os valores variam ligeiramente para parecer real.
    """
    # Temperatura base 22°C, varia ±2°C
    temperatura = 22.0 + random.uniform(-2.0, 2.0)

    # Pressão base 1013 hPa, varia ±5 hPa
    pressao = 1013.25 + random.uniform(-5.0, 5.0)

    # Altitude decresce ao longo do tempo (simula queda)
    altitude = 100 - (segundo * 3) + random.uniform(-1.0, 1.0)
    if altitude < 0:
        altitude = 0

    return {
        "timestamp": segundo,
        "temperatura": round(temperatura, 2),
        "pressao": round(pressao, 2),
        "altitude": round(altitude, 2)
    }

# Gera 30 segundos de dados
dados = []
for s in range(30):
    leitura = gerar_leitura(s)
    dados.append(leitura)
    print(leitura)
    
# Guarda em CSV

with open("data/simulacao.csv", "w") as f:
    f.write("timestamp,temperatura,pressao,altitude\n")
    for d in dados:
        f.write(f"{d['timestamp']},{d['temperatura']},{d['pressao']},{d['altitude']}\n")
print(f"\nGuardados {len(dados)} registos em data/simulacao.csv")