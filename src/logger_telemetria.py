import os
import csv
from datetime import datetime


class LoggerTelemetria:
    def __init__(self, pasta="logs"):
        """
        Cria a pasta de logs (se não existir)
        Inicializa ficheiros CSV e log
        """
        self.pasta = pasta
        os.makedirs(self.pasta, exist_ok=True)

        self.caminho_csv = os.path.join(self.pasta, "telemetria.csv")
        self.caminho_log = os.path.join(self.pasta, "erros.log")

        # Criar CSV com cabeçalho se não existir
        if not os.path.exists(self.caminho_csv):
            with open(self.caminho_csv, mode="w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(["timestamp", "temperatura", "pressao", "altitude"])

    def registar_dados(self, dados):
        """
        Guarda dados válidos no CSV
        """
        with open(self.caminho_csv, mode="a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow([
                dados["timestamp"],
                dados["temperatura"],
                dados["pressao"],
                dados["altitude"],
            ])

    def registar_erro(self, mensagem_original, erro):
        """
        Guarda erros no ficheiro de log
        """
        with open(self.caminho_log, mode="a", encoding="utf-8") as f:
            f.write(f"[{datetime.now().isoformat()}] ERRO: {erro}\n")
            f.write(f"Mensagem: {mensagem_original}\n\n")

    def registar_evento(self, evento):
        """
        Guarda eventos gerais no log
        """
        with open(self.caminho_log, mode="a", encoding="utf-8") as f:
            f.write(f"[{datetime.now().isoformat()}] EVENTO: {evento}\n")