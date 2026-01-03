# Abrir ficheiro para leitura
with open("data/teste.txt", "r") as ficheiro:
    conteudo = ficheiro.read()
    print(conteudo)

# Ler linha a linha
with open("data/teste.txt", "r") as ficheiro:
    for linha in ficheiro:
        print(f"Linha: {linha.strip()}")