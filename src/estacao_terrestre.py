import sys
import time
from protocolo import processar_mensagem
from logger_telemetria import LoggerTelemetria


def executar(ficheiro, realtime=False):
    logger = LoggerTelemetria("logs")

    logger.registar_evento("Estação terrestre iniciada")

    total = 0
    validas = 0
    invalidas = 0

    with open(ficheiro, "r", encoding="utf-8") as f:
        for linha in f:
            mensagem = linha.strip()
            total += 1

            valida, resultado = processar_mensagem(mensagem)

            if valida:
                logger.registar_dados(resultado)
                validas += 1
                print("✔ Válida:", resultado)
            else:
                logger.registar_erro(mensagem, resultado)
                invalidas += 1
                print("✖ Inválida:", resultado)

            if realtime:
                time.sleep(1)

    logger.registar_evento("Processamento terminado")

    print("\n=== RELATÓRIO FINAL ===")
    print(f"Total: {total}")
    print(f"Válidas: {validas}")
    print(f"Inválidas: {invalidas}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python src/estacao_terrestre.py <ficheiro> [--realtime]")
        sys.exit(1)

    ficheiro = sys.argv[1]
    realtime = "--realtime" in sys.argv

    executar(ficheiro, realtime)