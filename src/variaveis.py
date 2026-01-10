# Variáveis do CanSat

altitude_lancamento = 100              # metros
pressao_atual = 1013.25                # hPa
temperatura_atual = 22.7               # °C
nome_equipa = "CanSat Exploradores"    # nome inventado
satelite_ativo = True                  # booleano

# Impressão das variáveis com descrição
print(f"Altitude de lançamento: {altitude_lancamento} m")
print(f"Pressão atual: {pressao_atual} hPa")
print(f"Temperatura atual: {temperatura_atual} °C")
print(f"Nome da equipa: {nome_equipa}")
print(f"Satélite ativo: {satelite_ativo}")

print("\nTipos das variáveis:")

# Impressão do tipo de cada variável
print(f"altitude_lancamento -> {type(altitude_lancamento)}")
print(f"pressao_atual -> {type(pressao_atual)}")
print(f"temperatura_atual -> {type(temperatura_atual)}")
print(f"nome_equipa -> {type(nome_equipa)}")
print(f"satelite_ativo -> {type(satelite_ativo)}")
