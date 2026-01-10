#Criar primeira lista com valores de pressao hPa (entre 900 - 1100)
leituras_pressao = [920,930,967,984,992,1003,1029,1034,1058,1096]

#Criar segunda lista de timestamps s (segundos)
timestamps = [0,1,2,3,4,5,6,7,8,9]

#Aceder a elementos
print(leituras_pressao[0]) #primeiro elemento
print(leituras_pressao[-1]) #ultimo elemento
print(len(leituras_pressao)) #tamanho da lista

#Adicionar elemento
leituras_pressao.append(1015.5)
print(leituras_pressao)

# Soma de todos os valores
soma = sum(leituras_pressao)
print(f"Soma: {soma}")

# Maior e menor valor
maior = max(leituras_pressao)
menor = min(leituras_pressao)
print(f"Máximo: {maior}, Mínimo: {menor}")

# Média (soma / quantidade)
media = soma / len(leituras_pressao)
print(f"Média: {media}")

timestamps.append(10)

import random

pressao_aleatoria = leituras_pressao.copy()
random.shuffle(pressao_aleatoria)

for i in range(len(timestamps)):
    print(f"tempo = {timestamps[i]} s → pressão = {pressao_aleatoria[i]} hPa")