temperatura = 25
pressao = 1013

if temperatura > 30:
    print("ALERTA: Temperatura muito alta!")
elif temperatura < 10:
    print("ALERTA: Temperatura muito baixa!")
else:
    print("Temperatura normal.")

#Criar uma função para verificar a leitura (pressao e temperatura)
def verificar_leitura(temperatura, pressao):
    if temperatura > 50 and pressao < 700:
        return "Crítico"
    elif temperatura < 35 and pressao > 850:
        return "ALERTA"
    else:
        return "OK"
status = verificar_leitura(temperatura, pressao)
print(f"Status da leitura: {status}")

# Percorrer lista
temperaturas = [22.5, 23.1, 35.5, 22.8, 51.0, 23.5]

for temp in [22.5, 23.1, 35.5, 22.8, 51.0, 23.5]:
    estado = verificar_leitura(temp, 1013.0)
    print(f"Temp: {temp}°C -> {estado}")

# Contar quantos "OK", "Alerta" e "Crítico" existem na lista
contagem_status = {"OK": 0, "ALERTA": 0, "Crítico": 0}
for temp in temperaturas:
    estado = verificar_leitura(temp, 1013.0)
    contagem_status[estado] += 1
print("Contagem de status:")
for status, contagem in contagem_status.items():
    print(f"{status}: {contagem}")