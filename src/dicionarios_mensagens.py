# Criar um dicionario
mensagem_cansat = {
    "timestamp": 0,  # segundos
    "temperatura": 23.5,  # graus Celsius
    "pressao": 1013.25,  # hPa
    "altitude": 98,  # metros
    "bateria": 85,  # porcentagem
    "valido": True,
}

print(mensagem_cansat)

# Aceder a elementos do dicionario (exemplo com `mensagem_cansat`)
print(f"Timestamp = {mensagem_cansat['timestamp']} s")
print(f"Temperatura = {mensagem_cansat['temperatura']} °C")
print(f"Pressão = {mensagem_cansat['pressao']} hPa")
print(f"Altitude = {mensagem_cansat['altitude']} m")
print(f"Bateria = {mensagem_cansat['bateria']} %")
print(f"Válido = {mensagem_cansat['valido']}")

telemetria = [
    {
        "timestamp": 0,
        "temperatura": 23.5,
        "pressao": 1013.25,
        "altitude": 98,
        "bateria": 85,
        "valido": True
    },
    {
        "timestamp": 1,
        "temperatura": 23.7,
        "pressao": 1012.80,
        "altitude": 100,
        "bateria": 84,
        "valido": True
    },
    {
        "timestamp": 2,
        "temperatura": 24.0,
        "pressao": 1012.50,
        "altitude": 102,
        "bateria": 83,
        "valido": True
    }
]
temperaturas = []

for item in telemetria:
    temperaturas.append(item["temperatura"])

print(temperaturas)

# Calcular a média das temperaturas
soma_temperaturas = sum(temperaturas)
media_temperaturas = soma_temperaturas / len(temperaturas)
print(f"Média das temperaturas: {media_temperaturas} °C")

# Encontrar a altitude mínima
altitudes = [item["altitude"] for item in telemetria]
altitude_minima = min(altitudes)
print(f"Altitude mínima: {altitude_minima} m")
