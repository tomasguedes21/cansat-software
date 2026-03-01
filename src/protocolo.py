#src/protocolo.py

def calcular_checksum(dados: str) -> str:
    """
    Calcula o checksum XOR de todos os caracteres da string 'dados'
    Retorna o valor em hexadecimal (2 caracteres, maiúsculas)
    """
    checksum = 0
    for c in dados:
        checksum ^= ord(c)
    return f"{checksum:02X}"


def criar_mensagem(timestamp, temperatura, pressao, altitude) -> str:
    """
    Cria uma mensagem no formato:
    $CANSAT,<timestamp>,<temperatura>,<pressao>,<altitude>,<checksum>
    """
    corpo = f"CANSAT,{timestamp},{temperatura},{pressao},{altitude}"
    checksum = calcular_checksum(corpo)
    return f"${corpo},{checksum}"


def validar_mensagem(mensagem: str) -> bool:
    """
    Verifica se o checksum da mensagem é válido
    """
    mensagem = mensagem.strip()

    if not mensagem.startswith("$"):
        return False

    try:
        conteudo = mensagem[1:]
        dados, checksum_recebido = conteudo.rsplit(",", 1)
    except ValueError:
        return False

    checksum_calculado = calcular_checksum(dados)
    return checksum_calculado == checksum_recebido


def processar_mensagem(mensagem: str):
    """
    Valida a mensagem e devolve:
    (True, dados_dict) se válida
    (False, erro_str) se inválida
    """

    mensagem = mensagem.strip()

    # 1️⃣ Validar checksum
    if not validar_mensagem(mensagem):
        return False, "Checksum inválido ou formato incorreto"

    try:
        conteudo = mensagem[1:]
        dados_str, _ = conteudo.rsplit(",", 1)

        partes = dados_str.split(",")

        if len(partes) != 5:
            return False, "Número de campos incorreto"

        _, timestamp, temperatura, pressao, altitude = partes

        dados = {
            "timestamp": int(timestamp),
            "temperatura": float(temperatura),
            "pressao": float(pressao),
            "altitude": float(altitude),
        }

        # 2️⃣ Validação física
        if not (-50 <= dados["temperatura"] <= 60):
            return False, "Temperatura fora de limites"

        if not (0 <= dados["pressao"] <= 1100):
            return False, "Pressão fora de limites"

        if not (-100 <= dados["altitude"] <= 50000):
            return False, "Altitude fora de limites"

        return True, dados

    except Exception as e:
        return False, f"Erro ao processar mensagem: {e}"
