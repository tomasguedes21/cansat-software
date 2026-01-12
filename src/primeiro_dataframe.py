import pandas as pd
# Criar um DataFrame a partir de um dicionário
dados = {
    "timestamp": [0, 1, 2, 3, 4],
    "temperatura": [23.5, 23.2, 22.8, 22.5, 22.1],
    "pressao": [1013.25, 1010.50, 1008.00, 1005.50, 1003.00]
}
df = pd.DataFrame(dados)
print("O meu primeiro DataFrame:")
print(df)
print()
print(f"Tipo: {type(df)}")
print(f"Forma: {df.shape} (linhas, colunas)")