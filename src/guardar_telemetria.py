mensagens = [
    {"timestamp": 0, "temperatura": 23.5, "pressao": 1013.25, "altitude": 100},
    {"timestamp": 1, "temperatura": 23.2, "pressao": 1010.50, "altitude": 95},
    {"timestamp": 2, "temperatura": 22.8, "pressao": 1008.00, "altitude": 88}
]

with open("data/telemetria.csv", "w") as f:
    # Escreve o cabeçalho
    f.write("timestamp,temperatura,pressao,altitude\n")
    # Escreve cada mensagem
    for msg in mensagens:
        f.write(f"{msg['timestamp']},{msg['temperatura']},{msg['pressao']},{msg['altitude']}\n")