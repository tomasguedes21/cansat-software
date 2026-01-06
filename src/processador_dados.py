import csv
from typing import List, Dict, Tuple


def processar_telemetria(path: str = "data/telemetria.csv") -> Tuple[List[Dict], List[Dict]]:
    dados_validos: List[Dict] = []
    dados_invalidos: List[Dict] = []

    with open(path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for i, row in enumerate(reader, start=1):
            entrada = dict(row)
            motivo = []
            try:
                temperatura = float(row.get('temperatura', ''))
            except Exception:
                temperatura = None
                motivo.append('temperatura inválida')

            try:
                pressao = float(row.get('pressao', ''))
            except Exception:
                pressao = None
                motivo.append('pressão inválida')

            if temperatura is None or not (-40 <= temperatura <= 60):
                if 'temperatura inválida' not in motivo:
                    motivo.append('temperatura fora do intervalo')

            if pressao is None or not (700 <= pressao <= 1200):
                if 'pressão inválida' not in motivo:
                    motivo.append('pressão fora do intervalo')

            if not motivo:
                entrada['temperatura'] = temperatura
                entrada['pressao'] = pressao
                dados_validos.append(entrada)
            else:
                entrada['motivo'] = '; '.join(motivo)
                entrada['linha'] = i
                dados_invalidos.append(entrada)

    return dados_validos, dados_invalidos


def imprimir_resumo(dados_validos: List[Dict], dados_invalidos: List[Dict]) -> None:
    print(f"Dados válidos: {len(dados_validos)}")
    print(f"Dados inválidos: {len(dados_invalidos)}")
    if dados_invalidos:
        print("Registos inválidos:")
        for inv in dados_invalidos:
            linha = inv.get('linha')
            motivo = inv.get('motivo')
            print(f"  Linha {linha}: {inv} - Motivo: {motivo}")


if __name__ == '__main__':
    validos, invalidos = processar_telemetria()
    imprimir_resumo(validos, invalidos)
