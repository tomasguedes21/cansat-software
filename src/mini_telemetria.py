import random
import csv
import os

def gerar_missao(duracao_segundos):
    dados = []
    altitude = 100.0
    for t in range(duracao_segundos):
        leitura = {
            "timestamp": t,
            "temperatura": round(random.uniform(15, 25), 2),
            "pressao": round(random.uniform(950, 1050), 2),
            "altitude": round(altitude, 2)
        }
        # Descida gradual
        altitude -= random.uniform(0.5, 2.0)

        # 5% de erros propositados
        if random.random() < 0.05:
            erro = random.choice(["temperatura", "pressao", "altitude"])
            leitura[erro] = random.choice([-100, 10000, None])
        dados.append(leitura)
    return dados

def validar_leitura(leitura):
    try:
        # Ajustei o limite da altitude para 500 para filtrar o erro de 10000
        if not (-40 <= leitura["temperatura"] <= 80): return False
        if not (300 <= leitura["pressao"] <= 1100): return False
        if not (0 <= leitura["altitude"] <= 500): return False
        
        # Verifica se algum valor essencial é None
        if None in leitura.values(): return False
    except (KeyError, TypeError):
        return False
    return True

def guardar_csv(dados, caminho):
    # Cria a pasta 'data' se não existir
    pasta = os.path.dirname(caminho)
    if pasta and not os.path.exists(pasta):
        os.makedirs(pasta)
    
    with open(caminho, "w", newline="", encoding="utf-8") as f:
        if not dados: return
        writer = csv.DictWriter(f, fieldnames=dados[0].keys())
        writer.writeheader()
        writer.writerows(dados)

def ler_csv(caminho):
    dados = []
    with open(caminho, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for linha in reader:
            d = {}
            try:
                d["timestamp"] = int(linha["timestamp"])
                for campo in ["temperatura", "pressao", "altitude"]:
                    valor = linha[campo]
                    d[campo] = float(valor) if valor != "None" and valor != "" else None
                dados.append(d)
            except ValueError:
                continue
    return dados

def calcular_estatisticas(dados):
    # Só entra aqui se houver dados válidos
    temps = [d["temperatura"] for d in dados]
    press = [d["pressao"] for d in dados]
    alts = [d["altitude"] for d in dados]
    
    return {
        "temp_min": min(temps), "temp_max": max(temps), "temp_media": sum(temps)/len(temps),
        "pres_min": min(press), "pres_max": max(press), "pres_media": sum(press)/len(press),
        "alt_max": max(alts)
    }

def gerar_relatorio(stats, total, validos, invalidos):
    p_val = (validos / total) * 100
    p_inv = (invalidos / total) * 100

    print("\n==========================================")
    print("           RELATÓRIO DE MISSÃO            ")
    print("==========================================\n")
    
    print(f"Duração: {total} segundos")
    print(f"Total de leituras: {total}")
    print(f"  - Válidas: {validos} ({p_val:.1f}%)")
    print(f"  - Inválidas: {invalidos} ({p_inv:.1f}%)\n")

    print("TEMPERATURA")
    print(f"  Mínima: {stats['temp_min']:.1f} °C")
    print(f"  Máxima: {stats['temp_max']:.1f} °C")
    print(f"  Média:  {stats['temp_media']:.1f} °C\n")

    print("PRESSÃO")
    print(f"  Mínima: {stats['pres_min']:.1f} hPa")
    print(f"  Máxima: {stats['pres_max']:.1f} hPa")
    print(f"  Média:  {stats['pres_media']:.1f} hPa\n")

    print("ALTITUDE")
    print(f"  Máxima: {stats['alt_max']:.1f} m\n")
    
    print("==========================================")
    print("             MISSÃO CONCLUÍDA             ")
    print("==========================================")

# --- BLOCO PRINCIPAL ---
if __name__ == "__main__":
    print("=== SIMULADOR DE MISSÃO CANSAT ===\n")
    print("A gerar dados da missão...")
    
    # 1. Gerar e salvar dados brutos
    caminho_bruto = "data/missao_bruta.csv"
    dados_gerados = gerar_missao(60)
    guardar_csv(dados_gerados, caminho_bruto)
    print(f"Guardados {len(dados_gerados)} registos em {caminho_bruto}")

    # 2. Ler e processar para validar
    dados_lidos = ler_csv(caminho_bruto)
    lista_validos = [d for d in dados_lidos if validar_leitura(d)]
    invalidos_count = len(dados_lidos) - len(lista_validos)

    caminho_valido = "data/missao_valida.csv"
    guardar_csv(lista_validos, caminho_valido)
    
    # 4. Gerar relatório se houver dados
    if lista_validos:
        stats = calcular_estatisticas(lista_validos)
        gerar_relatorio(stats, len(dados_lidos), len(lista_validos), invalidos_count)
    else:
        print("\nErro: Nenhuma leitura válida encontrada para o relatório.")