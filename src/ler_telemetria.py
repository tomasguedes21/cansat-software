def ler_telemetria():
    # Caminho do ficheiro
    caminho = 'data/telemetria.csv'
    
    # Lista onde vamos guardar os dicionários
    dados_recuperados = []

    try:
        # 1. Abre data/telemetria.csv
        with open(caminho, 'r', encoding='utf-8') as ficheiro:
            linhas = ficheiro.readlines()
            
            # 2. Salta a primeira linha (cabeçalho)
            # Usamos [1:] para começar a ler a partir do índice 1
            for linha in linhas[1:]:
                # Limpa espaços/quebras de linha e separa pelos campos (vírgula)
                # 3. Para cada linha, separa pelos campos
                campos = linha.strip().split(',')
                
                if len(campos) == 4: # Garante que a linha tem todos os dados
                    # 4. Converte para números e guarda numa lista de dicionários
                    dicionario_leitura = {
                        "timestamp": int(campos[0]),
                        "temperatura": float(campos[1]),
                        "pressao": float(campos[2]),
                        "altitude": float(campos[3])
                    }
                    dados_recuperados.append(dicionario_leitura)

        # 5. Imprime as mensagens recuperadas
        print("Mensagens recuperadas:")
        for mensagem in dados_recuperados:
            print(mensagem)

    except FileNotFoundError:
        print(f"Erro: O ficheiro em {caminho} não foi encontrado.")

# Executar a função
if __name__ == "__main__":
    ler_telemetria()