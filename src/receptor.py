from parser_telemetria import ParserTelemetria


def main():
    parser = ParserTelemetria()

    with open("data/telemetria_simulada.txt", "r", encoding="utf-8") as f:
        for linha in f:
            parser.processar_mensagem(linha)

    estatisticas = parser.get_estatisticas()

    print("=== RELATÓRIO DA ESTAÇÃO TERRESTRE ===")
    print(f"Total de mensagens: {estatisticas['total']}")
    print(f"Mensagens válidas: {estatisticas['validas']}")
    print(f"Mensagens inválidas: {estatisticas['invalidas']}")

    if estatisticas["validas"] > 0:
        print("\nPrimeira leitura válida:")
        print(parser.validas[0])

        print("\nÚltima leitura válida:")
        print(parser.validas[-1])


if __name__ == "__main__":
    main()
