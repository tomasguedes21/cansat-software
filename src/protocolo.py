# src/protocolo.py

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
    mensagem = f"${corpo},{checksum}"
    return mensagem


def validar_mensagem(mensagem: str) -> bool:
    """
    Verifica se o checksum da mensagem é válido
    """
    if not mensagem.startswith("$"):
        return False

    try:
        conteudo, checksum_recebido = mensagem[1:].rsplit(",", 1)
    except ValueError:
        return False

    checksum_calculado = calcular_checksum(conteudo)
    return checksum_calculado == checksum_recebido

from protocolo import criar_mensagem, validar_mensagem

msg = criar_mensagem(42, 21.5, 985.3, 523.7)
print(msg)

print("Mensagem válida?", validar_mensagem(msg))
