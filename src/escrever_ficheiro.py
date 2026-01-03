# Abrir ficheiro para escrita (cria se não existir)
with open("data/teste.txt", "w") as ficheiro:
    ficheiro.write("Primeira linha\n")
    ficheiro.write("Segunda linha\n")

print("Ficheiro criado!")