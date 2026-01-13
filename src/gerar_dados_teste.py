import pandas as pd
import random

# Simular 60 segundos de telemetria (1 leitura por segundo)
dados = {
    "timestamp": [],
    "temperatura": [],
    "pressao": [],
    "altitude": []
}

temp = 25.0  # temperatura inicial
pressao = 1013.25  # pressão ao nível do mar
altitude = 0  # altitude inicial

for t in range(60):
    dados["timestamp"].append(t)
    dados["temperatura"].append(round(temp, 1))
    dados["pressao"].append(round(pressao, 2))
    dados["altitude"].append(round(altitude, 1))
    
    # Simular subida do CanSat (valores mudam)
    temp -= random.uniform(0.1, 0.3)  # arrefece
    pressao -= random.uniform(1, 3)    # pressão diminui
    altitude += random.uniform(10, 20) # altitude aumenta

df = pd.DataFrame(dados)
df.to_csv("data/telemetria_simulada.csv", index=False)

print(f"Criado data/telemetria_simulada.csv com {len(df)} leituras")
print(df.head())
print("...")
print(df.tail())