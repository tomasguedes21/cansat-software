def celsius_para_kelvin(celsius):
    return celsius + 273.15

def pressao_valida(pressao):
    return 700 <= pressao <= 1200

def temperatura_valida(temperatura):
    return -40 <= temperatura <= 60

def calcular_altitude(pressao, pressao_ref=1013.25):
    return (pressao_ref - pressao) * 8.3