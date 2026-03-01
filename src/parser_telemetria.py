from protocolo import validar_mensagem


class ParserTelemetria:
    def __init__(self):
        self.validas = []
        self.invalidas = 0

    def processar_mensagem(self, msg):
        # 1. Validar checksum
        if not validar_mensagem(msg):
            self.invalidas += 1
            return

        # 2. Separar campos
        partes = msg.strip().split(",")
        try:
            dados = {
                "timestamp": int(partes[1]),
                "temperatura": float(partes[2]),
                "pressao": float(partes[3]),
                "altitude": float(partes[4]),
            }
        except (ValueError, IndexError):
            self.invalidas += 1
            return

        # 3. Validar limites físicos
        if not self._validar_valores(dados):
            self.invalidas += 1
            return

        # 4. Guardar leitura válida
        self.validas.append(dados)

    def _validar_valores(self, dados):
        return (
            -50 <= dados["temperatura"] <= 60
            and 0 <= dados["pressao"] <= 1100
            and -100 <= dados["altitude"] <= 50000
        )

    def get_estatisticas(self):
        return {
            "total": len(self.validas) + self.invalidas,
            "validas": len(self.validas),
            "invalidas": self.invalidas,
        }
