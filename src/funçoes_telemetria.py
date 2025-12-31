#Conversão de temperatura de Celsius para Kelvin
def celsius_para_kelvin(celsius):
    kelvin = celsius + 273.15
    return kelvin

#Função de validação de pressão
def pressao_valida(pressao):
    if 800 <= pressao <= 1200:
        return True
    else:
        return False
    
#Função de calculo de altitude aproximada
def calcular_altitude_aproximada(pressao):
    altitude = (1013.25 - pressao) * 8.3
    return altitude
    
celcius = 20
kelvin = celsius_para_kelvin(celcius)
print(kelvin)

pressao = 950
valida = pressao_valida(pressao)
print(valida)

pressao = 900
altitude = calcular_altitude_aproximada(pressao)
print(altitude)

def processar_mensagem(timestamp, temperatura, pressao):
    """
    Processa uma mensagem de telemetria.
    Retorna um dicionário com os dados processados.
    """
    
    # 1. Calcula altitude a partir da pressão (usando sua função)
    altitude = calcular_altitude_aproximada(pressao)
    
    # 2. Converte temperatura para Kelvin (usando sua função)
    temp_k = celsius_para_kelvin(temperatura)
    
    # 3. Verifica se pressão é válida (usando sua função)
    valida = pressao_valida(pressao)
    
    # 4. Retorna dicionário com tudo organizado
    return {
        "timestamp": timestamp,
        "temperatura_c": temperatura,
        "temperatura_k": temp_k,
        "pressao": pressao,
        "pressao_valida": valida,
        "altitude_estimada": altitude
    }

# Exemplo de uso para testar:
resultado = processar_mensagem(0, 22.5, 1010.0)
print(resultado)