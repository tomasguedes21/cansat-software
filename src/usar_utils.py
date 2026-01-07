# Importar funções do teu módulo
from utils import celsius_para_kelvin, pressao_valida
temp_c = 22.5
temp_k = celsius_para_kelvin(temp_c)
print(f"{temp_c}°C = {temp_k}K")
pressao = 1050
if pressao_valida(pressao):
    print("Pressão OK")
else:
    print("Pressão fora do intervalo!")