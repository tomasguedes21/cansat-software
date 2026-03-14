"""
Teste de Conhecimentos - Modulos 0, 1 e 2
Avaliacao abrangente do percurso completo
Executa com: python teste_m0_m1_m2_gui.py
"""

import tkinter as tk
from tkinter import ttk, messagebox
import time
from datetime import datetime

# Limite de tempo por pergunta (em segundos)
TEMPO_LIMITE = 120

# ============================================================
# DEFINICAO DAS PERGUNTAS - 40 QUESTOES
# ============================================================

PERGUNTAS = [
    # ========================================================
    # MODULO 0 - SETUP (6 perguntas)
    # ========================================================
    {
        "numero": 1,
        "modulo": "M0",
        "titulo": "PATH - Conceito",
        "pontos": 1,
        "texto": "O que e o PATH no contexto da instalacao do Python?",
        "codigo": None,
        "tipo": "escolha",
        "opcoes": [
            "O caminho para os ficheiros do projeto",
            "Uma variavel que diz ao sistema onde encontrar programas executaveis",
            "O nome da pasta onde o Python e instalado",
            "Uma extensao do VS Code"
        ],
        "correta": 1,
        "explicacao": "O PATH e uma variavel de ambiente que indica ao sistema operativo onde procurar programas quando escrevemos um comando no terminal."
    },
    {
        "numero": 2,
        "modulo": "M0",
        "titulo": "PATH - Consequencia",
        "pontos": 1,
        "texto": "O que acontece se o Python NAO estiver no PATH?",
        "codigo": None,
        "tipo": "escolha",
        "opcoes": [
            "O Python funciona mais lento",
            "O comando 'python' no terminal da erro 'comando nao encontrado'",
            "O Python so funciona no VS Code",
            "Os ficheiros .py nao abrem"
        ],
        "correta": 1,
        "explicacao": "Sem o Python no PATH, o terminal nao sabe onde encontrar o executavel do Python, dando erro de comando nao encontrado."
    },
    {
        "numero": 3,
        "modulo": "M0",
        "titulo": "Git - Comando add",
        "pontos": 1,
        "texto": "O que faz o comando 'git add .'?",
        "codigo": "git add .",
        "tipo": "escolha",
        "opcoes": [
            "Adiciona um ficheiro chamado '.' ao repositorio",
            "Adiciona todas as alteracoes da pasta atual ao staging area",
            "Cria um novo commit com todas as alteracoes",
            "Envia as alteracoes para o GitHub"
        ],
        "correta": 1,
        "explicacao": "O ponto (.) significa 'pasta atual'. O comando adiciona todas as alteracoes ao staging area, prontas para o proximo commit."
    },
    {
        "numero": 4,
        "modulo": "M0",
        "titulo": "Git - Sequencia de comandos",
        "pontos": 1,
        "texto": "Qual e a sequencia correta para guardar alteracoes no GitHub?",
        "codigo": None,
        "tipo": "escolha",
        "opcoes": [
            "git push -> git commit -> git add",
            "git commit -> git add -> git push",
            "git add -> git commit -> git push",
            "git add -> git push -> git commit"
        ],
        "correta": 2,
        "explicacao": "Primeiro adicionas ao staging (add), depois crias o commit (commit), e finalmente envias para o servidor (push)."
    },
    {
        "numero": 5,
        "modulo": "M0",
        "titulo": "Controlo de versoes - Conceito",
        "pontos": 1,
        "texto": "Qual e a principal vantagem do controlo de versoes com Git?",
        "codigo": None,
        "tipo": "escolha",
        "opcoes": [
            "Torna o codigo mais rapido",
            "Permite voltar a versoes anteriores e ver o historico de alteracoes",
            "Comprime os ficheiros para ocupar menos espaco",
            "Protege os ficheiros com password"
        ],
        "correta": 1,
        "explicacao": "O controlo de versoes regista todas as alteracoes, permitindo voltar atras se algo correr mal e ver quem fez o que."
    },
    {
        "numero": 6,
        "modulo": "M0",
        "titulo": "GitHub - Local vs Remoto",
        "pontos": 1,
        "texto": "Qual e a diferenca entre o repositorio local e o repositorio no GitHub?",
        "codigo": None,
        "tipo": "escolha",
        "opcoes": [
            "Nao ha diferenca, sao a mesma coisa",
            "O local esta no teu computador, o GitHub esta na nuvem (servidor)",
            "O local so tem codigo, o GitHub so tem documentacao",
            "O GitHub e mais rapido que o local"
        ],
        "correta": 1,
        "explicacao": "O repositorio local esta no teu computador; o GitHub guarda uma copia na nuvem, acessivel de qualquer lugar."
    },

    # ========================================================
    # MODULO 1 - PYTHON BASICO (18 perguntas)
    # ========================================================
    {
        "numero": 7,
        "modulo": "M1",
        "titulo": "Tipos - int vs str",
        "pontos": 1,
        "texto": "Qual e a diferenca entre estas duas linhas?",
        "codigo": "altitude = 100\naltitude = \"100\"",
        "tipo": "escolha",
        "opcoes": [
            "Nao ha diferenca, sao iguais",
            "A primeira e um numero (int), a segunda e texto (str)",
            "A primeira e texto, a segunda e numero",
            "A segunda da erro porque tem aspas"
        ],
        "correta": 1,
        "explicacao": "Sem aspas e um numero inteiro (int), com aspas e uma string (texto). Isto afeta as operacoes possiveis."
    },
    {
        "numero": 8,
        "modulo": "M1",
        "titulo": "Tipos - Output de operacao",
        "pontos": 1,
        "texto": "O que aparece no ecra?",
        "codigo": "x = 10\ny = 3\nprint(x / y)",
        "tipo": "escolha",
        "opcoes": ["3", "3.3333...", "3.0", "Erro"],
        "correta": 1,
        "explicacao": "A divisao com / em Python sempre retorna um float (numero decimal), mesmo entre inteiros."
    },
    {
        "numero": 9,
        "modulo": "M1",
        "titulo": "Listas - Indices",
        "pontos": 1,
        "texto": "Se tiveres uma lista com 100 elementos e quiseres o elemento numero 50, qual indice usas?",
        "codigo": "leituras = [...]  # 100 elementos",
        "tipo": "escolha",
        "opcoes": ["50", "49", "51", "100"],
        "correta": 1,
        "explicacao": "Em Python, os indices comecam em 0. O primeiro elemento e indice 0, logo o 50o elemento esta no indice 49."
    },
    {
        "numero": 10,
        "modulo": "M1",
        "titulo": "Listas - Output",
        "pontos": 1,
        "texto": "O que aparece no ecra?",
        "codigo": "dados = [10, 20, 30]\ndados.append(40)\nprint(len(dados))",
        "tipo": "escolha",
        "opcoes": ["3", "4", "40", "[10, 20, 30, 40]"],
        "correta": 1,
        "explicacao": "append() adiciona um elemento ao fim da lista. len() retorna o numero de elementos, que passa de 3 para 4."
    },
    {
        "numero": 11,
        "modulo": "M1",
        "titulo": "Listas - Metodo pop",
        "pontos": 1,
        "texto": "O que faz lista.pop()?",
        "codigo": "dados = [10, 20, 30]\nx = dados.pop()\nprint(x)",
        "tipo": "escolha",
        "opcoes": [
            "Remove e retorna o primeiro elemento (10)",
            "Remove e retorna o ultimo elemento (30)",
            "Limpa toda a lista",
            "Da erro porque falta um argumento"
        ],
        "correta": 1,
        "explicacao": "pop() sem argumento remove e retorna o ultimo elemento da lista."
    },
    {
        "numero": 12,
        "modulo": "M1",
        "titulo": "Dicionarios - Acesso",
        "pontos": 1,
        "texto": "O que aparece no ecra?",
        "codigo": "sensor = {\"temp\": 25, \"pressao\": 1013}\nprint(sensor[\"temp\"] + 5)",
        "tipo": "escolha",
        "opcoes": ["25", "30", "temp + 5", "Erro"],
        "correta": 1,
        "explicacao": "sensor[\"temp\"] acede ao valor 25, que somado a 5 da 30."
    },
    {
        "numero": 13,
        "modulo": "M1",
        "titulo": "Dicionarios - KeyError",
        "pontos": 1,
        "texto": "O que acontece ao executar este codigo?",
        "codigo": "sensor = {\"temp\": 25}\nprint(sensor[\"altitude\"])",
        "tipo": "escolha",
        "opcoes": [
            "Aparece 0",
            "Aparece None",
            "Erro KeyError",
            "Cria a chave automaticamente"
        ],
        "correta": 2,
        "explicacao": "Aceder a uma chave que nao existe com [] causa um KeyError."
    },
    {
        "numero": 14,
        "modulo": "M1",
        "titulo": "Dicionarios - get()",
        "pontos": 1,
        "texto": "O que aparece no ecra?",
        "codigo": "sensor = {\"temp\": 25}\nprint(sensor.get(\"altitude\", 0))",
        "tipo": "escolha",
        "opcoes": ["None", "0", "Erro KeyError", "\"altitude\""],
        "correta": 1,
        "explicacao": "O metodo .get() retorna o valor padrao (0) se a chave nao existir, evitando o erro."
    },
    {
        "numero": 15,
        "modulo": "M1",
        "titulo": "Funcoes - Output",
        "pontos": 1,
        "texto": "O que aparece no ecra?",
        "codigo": "def dobro(x):\n    return x * 2\n\nresultado = dobro(5)\nprint(resultado)",
        "tipo": "escolha",
        "opcoes": ["5", "10", "x * 2", "None"],
        "correta": 1,
        "explicacao": "A funcao retorna 5 * 2 = 10, que e guardado em 'resultado' e depois impresso."
    },
    {
        "numero": 16,
        "modulo": "M1",
        "titulo": "Funcoes - print vs return",
        "pontos": 1,
        "texto": "Qual e a diferenca entre print() e return numa funcao?",
        "codigo": None,
        "tipo": "escolha",
        "opcoes": [
            "Sao iguais, fazem a mesma coisa",
            "print() mostra no ecra, return devolve o valor para usar noutro sitio",
            "return mostra no ecra, print devolve o valor",
            "print() so funciona com texto"
        ],
        "correta": 1,
        "explicacao": "print() escreve no ecra mas nao devolve nada util. return devolve um valor que pode ser guardado ou usado."
    },
    {
        "numero": 17,
        "modulo": "M1",
        "titulo": "Funcoes - Sem return",
        "pontos": 1,
        "texto": "O que aparece no ecra?",
        "codigo": "def mostrar(x):\n    print(x * 2)\n\nresultado = mostrar(5)\nprint(resultado)",
        "tipo": "escolha",
        "opcoes": ["10", "10\\nNone", "None", "5"],
        "correta": 1,
        "explicacao": "A funcao imprime 10, mas como nao tem return, devolve None. Sao impressos '10' e depois 'None'."
    },
    {
        "numero": 18,
        "modulo": "M1",
        "titulo": "Ficheiros - Modo w",
        "pontos": 1,
        "texto": "Se o ficheiro dados.txt ja existir com conteudo, o que acontece?",
        "codigo": "with open(\"dados.txt\", \"w\") as f:\n    f.write(\"Novo texto\")",
        "tipo": "escolha",
        "opcoes": [
            "O novo texto e adicionado no fim",
            "O conteudo antigo e apagado e substituido",
            "Da erro porque o ficheiro ja existe",
            "Nada acontece"
        ],
        "correta": 1,
        "explicacao": "O modo 'w' (write) apaga o conteudo existente e escreve de novo. Para adicionar, usa-se 'a' (append)."
    },
    {
        "numero": 19,
        "modulo": "M1",
        "titulo": "Ficheiros - with statement",
        "pontos": 1,
        "texto": "Para que serve o 'with' ao abrir ficheiros?",
        "codigo": "with open(\"dados.txt\", \"r\") as f:\n    texto = f.read()",
        "tipo": "escolha",
        "opcoes": [
            "So serve para dar um nome ao ficheiro",
            "Garante que o ficheiro e fechado automaticamente",
            "Permite ler mais rapido",
            "Protege o ficheiro contra escrita"
        ],
        "correta": 1,
        "explicacao": "O 'with' garante que o ficheiro e fechado automaticamente, mesmo se ocorrer um erro no codigo."
    },
    {
        "numero": 20,
        "modulo": "M1",
        "titulo": "Ficheiros - CSV",
        "pontos": 1,
        "texto": "O que significa CSV?",
        "codigo": None,
        "tipo": "escolha",
        "opcoes": [
            "Code Source Version",
            "Comma Separated Values",
            "Computer Standard Variable",
            "Central Storage Value"
        ],
        "correta": 1,
        "explicacao": "CSV significa Comma Separated Values - valores separados por virgulas. E um formato simples para dados tabulares."
    },
    {
        "numero": 21,
        "modulo": "M1",
        "titulo": "Condicionais - Output",
        "pontos": 1,
        "texto": "O que aparece no ecra?",
        "codigo": "temp = 25\nif temp > 30:\n    print(\"Quente\")\nelif temp > 20:\n    print(\"Agradavel\")\nelse:\n    print(\"Frio\")",
        "tipo": "escolha",
        "opcoes": ["Quente", "Agradavel", "Frio", "Nada"],
        "correta": 1,
        "explicacao": "25 nao e maior que 30, mas e maior que 20, logo entra no elif e imprime 'Agradavel'."
    },
    {
        "numero": 22,
        "modulo": "M1",
        "titulo": "Condicionais - Operador or",
        "pontos": 1,
        "texto": "O que aparece no ecra?",
        "codigo": "temp = 15\npressao = 800\n\nif temp > 30 or pressao < 900:\n    print(\"Alerta\")\nelse:\n    print(\"OK\")",
        "tipo": "escolha",
        "opcoes": ["OK", "Alerta", "Erro", "Nada"],
        "correta": 1,
        "explicacao": "Com 'or', basta UMA condicao ser verdadeira. pressao < 900 e True (800 < 900), logo imprime 'Alerta'."
    },
    {
        "numero": 23,
        "modulo": "M1",
        "titulo": "Ciclos - for com lista",
        "pontos": 1,
        "texto": "O que aparece no ecra?",
        "codigo": "valores = [10, 20, 30]\ntotal = 0\nfor v in valores:\n    total = total + v\nprint(total)",
        "tipo": "escolha",
        "opcoes": ["30", "60", "10, 20, 30", "Erro"],
        "correta": 1,
        "explicacao": "O ciclo soma 10 + 20 + 30 = 60."
    },
    {
        "numero": 24,
        "modulo": "M1",
        "titulo": "Ciclos - for vs while",
        "pontos": 1,
        "texto": "Quando deves usar 'while' em vez de 'for'?",
        "codigo": None,
        "tipo": "escolha",
        "opcoes": [
            "Quando sabes quantas vezes vai repetir",
            "Quando a repeticao depende de uma condicao que pode mudar",
            "Quando queres percorrer uma lista",
            "Nao ha diferenca, sao iguais"
        ],
        "correta": 1,
        "explicacao": "Usa 'for' quando sabes quantas iteracoes. Usa 'while' quando a repeticao depende de uma condicao variavel."
    },
    {
        "numero": 25,
        "modulo": "M1",
        "titulo": "Bibliotecas - import",
        "pontos": 1,
        "texto": "Qual e a diferenca entre estas duas formas de import?",
        "codigo": "import math\n# vs\nfrom math import sqrt",
        "tipo": "escolha",
        "opcoes": [
            "Nao ha diferenca",
            "A primeira importa tudo, a segunda so a funcao sqrt",
            "A segunda e mais rapida",
            "A primeira da erro"
        ],
        "correta": 1,
        "explicacao": "'import math' importa o modulo inteiro (usas math.sqrt). 'from math import sqrt' importa so a funcao sqrt."
    },

    # ========================================================
    # MODULO 2 - DADOS E GRAFICOS (16 perguntas)
    # ========================================================
    {
        "numero": 26,
        "modulo": "M2",
        "titulo": "Pandas - DataFrame",
        "pontos": 1,
        "texto": "O que e um DataFrame do pandas?",
        "codigo": None,
        "tipo": "escolha",
        "opcoes": [
            "Um tipo de grafico",
            "Uma estrutura de dados em forma de tabela (linhas e colunas)",
            "Um ficheiro de configuracao",
            "Uma funcao para calcular medias"
        ],
        "correta": 1,
        "explicacao": "Um DataFrame e como uma tabela Excel em Python - tem linhas e colunas, permitindo operacoes eficientes sobre dados."
    },
    {
        "numero": 27,
        "modulo": "M2",
        "titulo": "Pandas - Convencoes de import",
        "pontos": 1,
        "texto": "Qual e a convencao padrao para importar pandas e matplotlib?",
        "codigo": None,
        "tipo": "escolha",
        "opcoes": [
            "import pandas\\nimport matplotlib",
            "import pandas as pd\\nimport matplotlib.pyplot as plt",
            "from pandas import *\\nfrom matplotlib import *",
            "import pd\\nimport plt"
        ],
        "correta": 1,
        "explicacao": "A convencao e usar 'pd' para pandas e 'plt' para matplotlib.pyplot. Vais ver isto em todos os tutoriais."
    },
    {
        "numero": 28,
        "modulo": "M2",
        "titulo": "Pandas - read_csv",
        "pontos": 1,
        "texto": "Quantas linhas de codigo precisas para carregar um CSV com pandas?",
        "codigo": "# Carregar dados.csv para um DataFrame",
        "tipo": "escolha",
        "opcoes": [
            "1 linha: df = pd.read_csv(\"dados.csv\")",
            "3 linhas: abrir, ler, fechar",
            "5 linhas: configurar, abrir, ler, processar, fechar",
            "Depende do tamanho do ficheiro"
        ],
        "correta": 0,
        "explicacao": "Com pandas, carregar um CSV e uma unica linha! Compara com o codigo manual que fizeste no M1."
    },
    {
        "numero": 29,
        "modulo": "M2",
        "titulo": "Pandas - Series vs DataFrame",
        "pontos": 1,
        "texto": "Qual e a diferenca entre df[\"temp\"] e df[[\"temp\"]]?",
        "codigo": "df = pd.read_csv(\"dados.csv\")\na = df[\"temp\"]\nb = df[[\"temp\"]]",
        "tipo": "escolha",
        "opcoes": [
            "Nao ha diferenca",
            "df[\"temp\"] retorna uma Series, df[[\"temp\"]] retorna um DataFrame",
            "df[\"temp\"] retorna um DataFrame, df[[\"temp\"]] retorna uma Series",
            "A segunda da erro"
        ],
        "correta": 1,
        "explicacao": "Uma parentese retorna uma Series (coluna). Duas parenteses retornam um DataFrame com uma coluna."
    },
    {
        "numero": 30,
        "modulo": "M2",
        "titulo": "Pandas - head e tail",
        "pontos": 1,
        "texto": "O que faz df.head(3)?",
        "codigo": "df = pd.read_csv(\"dados.csv\")\nprint(df.head(3))",
        "tipo": "escolha",
        "opcoes": [
            "Mostra as ultimas 3 linhas",
            "Mostra as primeiras 3 linhas",
            "Remove as primeiras 3 linhas",
            "Mostra 3 colunas"
        ],
        "correta": 1,
        "explicacao": "head(n) mostra as primeiras n linhas. tail(n) mostra as ultimas n linhas."
    },
    {
        "numero": 31,
        "modulo": "M2",
        "titulo": "Pandas - describe",
        "pontos": 1,
        "texto": "Que tipo de informacao mostra df.describe()?",
        "codigo": None,
        "tipo": "escolha",
        "opcoes": [
            "Os tipos de dados de cada coluna",
            "Estatisticas: media, min, max, desvio padrao, etc.",
            "O nome das colunas",
            "O numero de linhas"
        ],
        "correta": 1,
        "explicacao": "describe() mostra estatisticas descritivas: contagem, media, desvio padrao, minimo, maximo e quartis."
    },
    {
        "numero": 32,
        "modulo": "M2",
        "titulo": "Pandas - Filtrar dados",
        "pontos": 1,
        "texto": "Como filtrar um DataFrame para mostrar so linhas onde temperatura > 20?",
        "codigo": None,
        "tipo": "escolha",
        "opcoes": [
            "df.filter(temperatura > 20)",
            "df[df[\"temperatura\"] > 20]",
            "df.where(\"temperatura\", 20)",
            "df.select(temperatura > 20)"
        ],
        "correta": 1,
        "explicacao": "A sintaxe df[condicao] filtra o DataFrame. A condicao df[\"temperatura\"] > 20 cria uma mascara booleana."
    },
    {
        "numero": 33,
        "modulo": "M2",
        "titulo": "Pandas - Nova coluna",
        "pontos": 1,
        "texto": "Como criar uma coluna 'dobro' que e o dobro da coluna 'valor'?",
        "codigo": None,
        "tipo": "escolha",
        "opcoes": [
            "df.add_column(\"dobro\", df[\"valor\"] * 2)",
            "df[\"dobro\"] = df[\"valor\"] * 2",
            "df.create(\"dobro\", valor * 2)",
            "df.dobro = valor * 2"
        ],
        "correta": 1,
        "explicacao": "Criar uma nova coluna e simples: df[\"nova_coluna\"] = calculo. O pandas aplica a operacao a todas as linhas."
    },
    {
        "numero": 34,
        "modulo": "M2",
        "titulo": "Pandas - diff()",
        "pontos": 1,
        "texto": "O que faz df[\"altitude\"].diff()?",
        "codigo": "# altitude: [100, 150, 220, 300]\ndf[\"variacao\"] = df[\"altitude\"].diff()",
        "tipo": "escolha",
        "opcoes": [
            "Calcula a diferenca entre o primeiro e ultimo valor",
            "Calcula a diferenca entre cada valor e o anterior",
            "Ordena os valores do menor para o maior",
            "Remove valores duplicados"
        ],
        "correta": 1,
        "explicacao": "diff() calcula a diferenca entre cada linha e a anterior. Resultado: [NaN, 50, 70, 80]"
    },
    {
        "numero": 35,
        "modulo": "M2",
        "titulo": "Pandas - groupby",
        "pontos": 1,
        "texto": "O que faz df.groupby(\"fase\")[\"temp\"].mean()?",
        "codigo": None,
        "tipo": "escolha",
        "opcoes": [
            "Calcula a media de todas as temperaturas",
            "Agrupa por fase e calcula a media da temperatura para cada grupo",
            "Cria uma nova coluna chamada 'fase'",
            "Ordena o DataFrame por fase"
        ],
        "correta": 1,
        "explicacao": "groupby agrupa os dados por um criterio, e depois podes aplicar funcoes (mean, sum, count) a cada grupo."
    },
    {
        "numero": 36,
        "modulo": "M2",
        "titulo": "Matplotlib - Plot basico",
        "pontos": 1,
        "texto": "O que cria este codigo?",
        "codigo": "plt.plot(df[\"tempo\"], df[\"altitude\"])\nplt.show()",
        "tipo": "escolha",
        "opcoes": [
            "Um grafico de barras",
            "Um grafico de linha",
            "Um grafico circular (pie)",
            "Um histograma"
        ],
        "correta": 1,
        "explicacao": "plt.plot() cria um grafico de linha. O primeiro argumento e o eixo X, o segundo e o eixo Y."
    },
    {
        "numero": 37,
        "modulo": "M2",
        "titulo": "Matplotlib - Titulos",
        "pontos": 1,
        "texto": "Como adicionar um titulo ao grafico?",
        "codigo": None,
        "tipo": "escolha",
        "opcoes": [
            "plt.name(\"Titulo\")",
            "plt.title(\"Titulo\")",
            "plt.header(\"Titulo\")",
            "plt.label(\"Titulo\")"
        ],
        "correta": 1,
        "explicacao": "plt.title() define o titulo. plt.xlabel() e plt.ylabel() definem as legendas dos eixos."
    },
    {
        "numero": 38,
        "modulo": "M2",
        "titulo": "Matplotlib - savefig vs show",
        "pontos": 1,
        "texto": "Qual e a diferenca entre plt.savefig() e plt.show()?",
        "codigo": None,
        "tipo": "escolha",
        "opcoes": [
            "Nao ha diferenca",
            "savefig() guarda como imagem, show() abre uma janela",
            "show() guarda como imagem, savefig() abre uma janela",
            "savefig() so funciona no VS Code"
        ],
        "correta": 1,
        "explicacao": "savefig() guarda o grafico como ficheiro (PNG, PDF, etc.). show() abre uma janela interativa."
    },
    {
        "numero": 39,
        "modulo": "M2",
        "titulo": "Matplotlib - Subplots",
        "pontos": 1,
        "texto": "O que cria fig, axes = plt.subplots(2, 2)?",
        "codigo": None,
        "tipo": "escolha",
        "opcoes": [
            "Um grafico com 2 linhas",
            "Uma grelha de 2x2 = 4 graficos",
            "2 graficos lado a lado",
            "Um grafico com 2 eixos Y"
        ],
        "correta": 1,
        "explicacao": "subplots(2, 2) cria uma grelha de 2 linhas x 2 colunas = 4 espacos para graficos."
    },
    {
        "numero": 40,
        "modulo": "M2",
        "titulo": "CanSat - Interpretacao fisica",
        "pontos": 1,
        "texto": "Num grafico de Temperatura vs Altitude do CanSat, que padrao esperarias ver?",
        "codigo": None,
        "tipo": "escolha",
        "opcoes": [
            "Temperatura aumenta com a altitude",
            "Temperatura diminui com a altitude (correlacao negativa)",
            "Temperatura mantem-se constante",
            "Nao ha relacao entre temperatura e altitude"
        ],
        "correta": 1,
        "explicacao": "A temperatura diminui com a altitude porque o ar e aquecido pela superficie terrestre. Isto e fisica basica da atmosfera!"
    }
]


# ============================================================
# INTERFACE GRAFICA
# ============================================================

class TesteApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Teste M0-M2 - Avaliacao de Conhecimentos")
        self.root.geometry("900x750")
        self.root.minsize(850, 700)
        self.root.configure(bg="#f0f0f0")

        # Variaveis
        self.pergunta_atual = 0
        self.pontuacao = 0
        self.respostas = []
        self.tempo_inicio_pergunta = None
        self.tempo_inicio_teste = None
        self.selected_option = tk.IntVar(value=-1)

        # Criar interface
        self.criar_tela_inicial()

    def criar_tela_inicial(self):
        """Tela inicial com instrucoes"""
        self.limpar_tela()

        frame = tk.Frame(self.root, bg="#f0f0f0", padx=40, pady=30)
        frame.pack(expand=True, fill="both")

        tk.Label(frame, text="TESTE DE CONHECIMENTOS", font=("Arial", 24, "bold"),
                bg="#f0f0f0", fg="#333").pack(pady=(0, 5))
        tk.Label(frame, text="Modulos 0, 1 e 2 - Avaliacao Completa", font=("Arial", 16),
                bg="#f0f0f0", fg="#666").pack(pady=(0, 20))

        # Info do teste
        info_frame = tk.Frame(frame, bg="#e3f2fd", padx=20, pady=15, relief="ridge", bd=2)
        info_frame.pack(fill="x", pady=10)

        tk.Label(info_frame, text="Conteudo do Teste:", font=("Arial", 14, "bold"),
                bg="#e3f2fd", anchor="w").pack(fill="x")

        conteudos = [
            "M0 - Setup: PATH, Git, GitHub, controlo de versoes (6 questoes)",
            "M1 - Python Basico: variaveis, listas, funcoes, ficheiros, ciclos (18 questoes)",
            "M2 - Dados e Graficos: pandas, matplotlib, DataFrames, graficos (16 questoes)"
        ]
        for c in conteudos:
            tk.Label(info_frame, text=f"  {c}", font=("Arial", 11),
                    bg="#e3f2fd", anchor="w").pack(fill="x", pady=1)

        # Regras
        regras_frame = tk.Frame(frame, bg="#fff", padx=20, pady=15, relief="ridge", bd=2)
        regras_frame.pack(fill="x", pady=10)

        tk.Label(regras_frame, text="Regras:", font=("Arial", 14, "bold"),
                bg="#fff", anchor="w").pack(fill="x")

        regras = [
            "Responde sem ajuda (sem internet, sem ChatGPT, sem codigo)",
            "Le bem cada pergunta antes de responder",
            "Tens 2 minutos por pergunta",
            "Total: 40 perguntas = 40 pontos"
        ]
        for regra in regras:
            tk.Label(regras_frame, text=f"  {regra}", font=("Arial", 11),
                    bg="#fff", anchor="w").pack(fill="x", pady=1)

        # Classificacao
        class_frame = tk.Frame(frame, bg="#fff3e0", padx=20, pady=15, relief="ridge", bd=2)
        class_frame.pack(fill="x", pady=10)

        tk.Label(class_frame, text="Classificacao:", font=("Arial", 14, "bold"),
                bg="#fff3e0", anchor="w").pack(fill="x")

        classificacoes = [
            ">= 32/40 (80%): Excelente",
            ">= 24/40 (60%): Bom",
            ">= 16/40 (40%): Suficiente",
            "< 16/40: Precisa de reforco"
        ]
        for c in classificacoes:
            tk.Label(class_frame, text=f"  {c}", font=("Arial", 11),
                    bg="#fff3e0", anchor="w").pack(fill="x", pady=1)

        tk.Button(frame, text="COMECAR TESTE", font=("Arial", 16, "bold"),
                 bg="#4CAF50", fg="white", padx=30, pady=15,
                 command=self.iniciar_teste, cursor="hand2").pack(pady=30)

    def iniciar_teste(self):
        """Inicia o teste"""
        self.tempo_inicio_teste = time.time()
        self.mostrar_pergunta()

    def mostrar_pergunta(self):
        """Mostra a pergunta atual"""
        self.limpar_tela()
        self.selected_option.set(-1)

        pergunta = PERGUNTAS[self.pergunta_atual]
        self.tempo_inicio_pergunta = time.time()

        # Frame principal
        main_frame = tk.Frame(self.root, bg="#f0f0f0", padx=25, pady=12)
        main_frame.pack(expand=True, fill="both")

        # Cabecalho
        header_frame = tk.Frame(main_frame, bg="#f0f0f0")
        header_frame.pack(fill="x", pady=(0, 8))

        # Info esquerda
        left_info = tk.Frame(header_frame, bg="#f0f0f0")
        left_info.pack(side="left")

        tk.Label(left_info, text=f"Pergunta {self.pergunta_atual + 1} de {len(PERGUNTAS)}",
                font=("Arial", 12), bg="#f0f0f0", fg="#666").pack(side="left")

        # Etiqueta do modulo
        modulo_cor = {"M0": "#9C27B0", "M1": "#2196F3", "M2": "#FF9800"}
        tk.Label(left_info, text=f" [{pergunta['modulo']}]",
                font=("Arial", 12, "bold"), bg="#f0f0f0",
                fg=modulo_cor.get(pergunta['modulo'], "#666")).pack(side="left", padx=(10, 0))

        # Info direita
        right_info = tk.Frame(header_frame, bg="#f0f0f0")
        right_info.pack(side="right")

        self.label_tempo = tk.Label(right_info, text="0s", font=("Arial", 12),
                                    bg="#f0f0f0", fg="#666")
        self.label_tempo.pack(side="right", padx=(20, 0))

        tk.Label(right_info, text=f"{pergunta['pontos']} pt",
                font=("Arial", 12, "bold"), bg="#f0f0f0", fg="#4CAF50").pack(side="right")

        # Barra de progresso
        progress = ttk.Progressbar(main_frame, length=400, mode='determinate',
                                   value=(self.pergunta_atual / len(PERGUNTAS)) * 100)
        progress.pack(fill="x", pady=(0, 12))

        # Titulo da pergunta
        tk.Label(main_frame, text=pergunta["titulo"], font=("Arial", 15, "bold"),
                bg="#f0f0f0", fg="#333").pack(anchor="w", pady=(0, 6))

        # Texto da pergunta
        tk.Label(main_frame, text=pergunta["texto"], font=("Arial", 12),
                bg="#f0f0f0", fg="#333", wraplength=800, justify="left").pack(anchor="w", pady=(0, 10))

        # Codigo (se houver)
        if pergunta["codigo"]:
            code_frame = tk.Frame(main_frame, bg="#2d2d2d", padx=15, pady=10)
            code_frame.pack(fill="x", pady=(0, 12))

            tk.Label(code_frame, text=pergunta["codigo"], font=("Consolas", 11),
                    bg="#2d2d2d", fg="#f8f8f2", justify="left", anchor="w").pack(anchor="w")

        # Opcoes
        opcoes_frame = tk.Frame(main_frame, bg="#f0f0f0")
        opcoes_frame.pack(fill="x", pady=6)

        for i, opcao in enumerate(pergunta["opcoes"]):
            rb = tk.Radiobutton(opcoes_frame, text=opcao, variable=self.selected_option,
                               value=i, font=("Arial", 11), bg="#f0f0f0",
                               activebackground="#f0f0f0", cursor="hand2",
                               anchor="w", padx=10, pady=4, wraplength=750)
            rb.pack(fill="x", pady=2)

        # Botao confirmar
        btn_frame = tk.Frame(main_frame, bg="#f0f0f0")
        btn_frame.pack(fill="x", pady=(15, 8))

        self.btn_confirmar = tk.Button(btn_frame, text="CONFIRMAR RESPOSTA",
                                       font=("Arial", 14, "bold"),
                                       bg="#4CAF50", fg="white", padx=25, pady=10,
                                       command=self.confirmar_resposta, cursor="hand2",
                                       relief="raised", bd=3)
        self.btn_confirmar.pack(pady=8)

        self.atualizar_timer()

    def atualizar_timer(self):
        """Atualiza o timer da pergunta"""
        if self.tempo_inicio_pergunta:
            tempo = int(time.time() - self.tempo_inicio_pergunta)
            cor = "#666" if tempo < TEMPO_LIMITE else "#f44336"
            self.label_tempo.config(text=f"{tempo}s", fg=cor)
            self.root.after(1000, self.atualizar_timer)

    def confirmar_resposta(self):
        """Processa a resposta selecionada"""
        if self.selected_option.get() == -1:
            messagebox.showwarning("Aviso", "Seleciona uma opcao antes de confirmar!")
            return

        tempo_resposta = int(time.time() - self.tempo_inicio_pergunta)
        self.tempo_inicio_pergunta = None

        pergunta = PERGUNTAS[self.pergunta_atual]
        opcao_selecionada = self.selected_option.get()
        correto = opcao_selecionada == pergunta["correta"]

        pontos_obtidos = pergunta["pontos"] if correto else 0
        self.pontuacao += pontos_obtidos

        self.respostas.append({
            "pergunta": self.pergunta_atual + 1,
            "modulo": pergunta["modulo"],
            "correto": correto,
            "pontos": pontos_obtidos,
            "max": pergunta["pontos"],
            "tempo": tempo_resposta
        })

        self.mostrar_feedback(correto, pergunta, pontos_obtidos)

    def mostrar_feedback(self, correto, pergunta, pontos):
        """Mostra feedback da resposta"""
        self.limpar_tela()

        frame = tk.Frame(self.root, bg="#f0f0f0", padx=40, pady=30)
        frame.pack(expand=True, fill="both")

        if correto:
            tk.Label(frame, text="CORRETO!", font=("Arial", 28, "bold"),
                    bg="#f0f0f0", fg="#4CAF50").pack(pady=15)
            tk.Label(frame, text=f"+{pontos} ponto{'s' if pontos != 1 else ''}",
                    font=("Arial", 18), bg="#f0f0f0", fg="#4CAF50").pack()
        else:
            tk.Label(frame, text="INCORRETO", font=("Arial", 28, "bold"),
                    bg="#f0f0f0", fg="#f44336").pack(pady=15)
            tk.Label(frame, text=f"Resposta certa: {pergunta['opcoes'][pergunta['correta']]}",
                    font=("Arial", 13), bg="#f0f0f0", fg="#333", wraplength=700).pack(pady=8)

        # Explicacao
        exp_frame = tk.Frame(frame, bg="#fff3e0", padx=20, pady=12, relief="ridge", bd=1)
        exp_frame.pack(fill="x", pady=15)
        tk.Label(exp_frame, text="Explicacao:", font=("Arial", 12, "bold"),
                bg="#fff3e0", fg="#e65100", anchor="w").pack(fill="x")
        tk.Label(exp_frame, text=pergunta["explicacao"], font=("Arial", 11),
                bg="#fff3e0", fg="#333", wraplength=700, justify="left").pack(fill="x", pady=(5, 0))

        # Botao continuar
        self.pergunta_atual += 1
        texto_btn = "PROXIMA PERGUNTA" if self.pergunta_atual < len(PERGUNTAS) else "VER RESULTADO"
        comando = self.mostrar_pergunta if self.pergunta_atual < len(PERGUNTAS) else self.mostrar_resultado

        tk.Button(frame, text=texto_btn, font=("Arial", 14, "bold"),
                 bg="#2196F3", fg="white", padx=25, pady=10,
                 command=comando, cursor="hand2").pack(pady=25)

    def mostrar_resultado(self):
        """Mostra o resultado final"""
        self.limpar_tela()

        tempo_total = int(time.time() - self.tempo_inicio_teste)
        minutos = tempo_total // 60
        segundos = tempo_total % 60

        frame = tk.Frame(self.root, bg="#f0f0f0", padx=35, pady=20)
        frame.pack(expand=True, fill="both")

        tk.Label(frame, text="RESULTADO DO TESTE", font=("Arial", 24, "bold"),
                bg="#f0f0f0", fg="#333").pack(pady=(0, 15))

        # Pontuacao
        cor_nota = "#4CAF50" if self.pontuacao >= 24 else ("#ff9800" if self.pontuacao >= 16 else "#f44336")
        tk.Label(frame, text=f"{self.pontuacao:.0f} / 40", font=("Arial", 48, "bold"),
                bg="#f0f0f0", fg=cor_nota).pack()

        tk.Label(frame, text=f"Tempo total: {minutos}m {segundos}s", font=("Arial", 14),
                bg="#f0f0f0", fg="#666").pack(pady=(8, 15))

        # Classificacao
        if self.pontuacao >= 32:
            classificacao = "EXCELENTE! Dominas todos os conceitos."
            cor_class = "#4CAF50"
        elif self.pontuacao >= 24:
            classificacao = "BOM! Tens uma boa base. Reve os erros."
            cor_class = "#8BC34A"
        elif self.pontuacao >= 16:
            classificacao = "SUFICIENTE. Alguns conceitos precisam de reforco."
            cor_class = "#ff9800"
        else:
            classificacao = "PRECISA DE REFORCO. Reve os modulos com mais erros."
            cor_class = "#f44336"

        class_frame = tk.Frame(frame, bg=cor_class, padx=20, pady=12)
        class_frame.pack(fill="x", pady=10)
        tk.Label(class_frame, text=classificacao, font=("Arial", 13, "bold"),
                bg=cor_class, fg="white").pack()

        # Resultados por modulo
        modulos = {"M0": {"acertos": 0, "total": 0}, "M1": {"acertos": 0, "total": 0}, "M2": {"acertos": 0, "total": 0}}
        for r in self.respostas:
            modulos[r["modulo"]]["total"] += 1
            if r["correto"]:
                modulos[r["modulo"]]["acertos"] += 1

        mod_frame = tk.Frame(frame, bg="#fff", padx=15, pady=12, relief="ridge", bd=1)
        mod_frame.pack(fill="x", pady=10)

        tk.Label(mod_frame, text="Resultados por Modulo:", font=("Arial", 12, "bold"),
                bg="#fff", anchor="w").pack(fill="x", pady=(0, 8))

        modulo_nomes = {"M0": "Setup", "M1": "Python Basico", "M2": "Dados e Graficos"}
        for mod, dados in modulos.items():
            pct = (dados["acertos"] / dados["total"] * 100) if dados["total"] > 0 else 0
            cor = "#4CAF50" if pct >= 70 else ("#ff9800" if pct >= 50 else "#f44336")
            tk.Label(mod_frame, text=f"  {mod} - {modulo_nomes[mod]}: {dados['acertos']}/{dados['total']} ({pct:.0f}%)",
                    font=("Arial", 11), bg="#fff", fg=cor, anchor="w").pack(fill="x")

        # Detalhes
        details_frame = tk.Frame(frame, bg="#fff", padx=12, pady=10, relief="ridge", bd=1)
        details_frame.pack(fill="x", pady=10)

        tk.Label(details_frame, text="Detalhes:", font=("Arial", 12, "bold"),
                bg="#fff", anchor="w").pack(fill="x", pady=(0, 8))

        canvas = tk.Canvas(details_frame, bg="#fff", height=120)
        scrollbar = ttk.Scrollbar(details_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg="#fff")

        scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        for r in self.respostas:
            simbolo = "OK" if r["correto"] else "X"
            cor = "#4CAF50" if r["correto"] else "#f44336"
            texto = f"  P{r['pergunta']:02d} [{r['modulo']}]: {simbolo} ({r['tempo']}s)"
            tk.Label(scrollable_frame, text=texto, font=("Consolas", 10),
                    bg="#fff", fg=cor, anchor="w").pack(fill="x")

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Botoes
        btn_frame = tk.Frame(frame, bg="#f0f0f0")
        btn_frame.pack(pady=15)

        tk.Button(btn_frame, text="GUARDAR RESULTADO", font=("Arial", 12),
                 bg="#607D8B", fg="white", padx=18, pady=8,
                 command=self.guardar_resultado, cursor="hand2").pack(side="left", padx=8)

        tk.Button(btn_frame, text="FECHAR", font=("Arial", 12),
                 bg="#9E9E9E", fg="white", padx=18, pady=8,
                 command=self.root.quit, cursor="hand2").pack(side="left", padx=8)

    def guardar_resultado(self):
        """Guarda o resultado num ficheiro"""
        data = datetime.now().strftime("%Y-%m-%d_%H-%M")
        nome_ficheiro = f"resultado_teste_m0_m1_m2_{data}.txt"

        tempo_total = int(time.time() - self.tempo_inicio_teste)
        minutos = tempo_total // 60
        segundos = tempo_total % 60

        # Calcular por modulo
        modulos = {"M0": {"acertos": 0, "total": 0}, "M1": {"acertos": 0, "total": 0}, "M2": {"acertos": 0, "total": 0}}
        for r in self.respostas:
            modulos[r["modulo"]]["total"] += 1
            if r["correto"]:
                modulos[r["modulo"]]["acertos"] += 1

        with open(nome_ficheiro, "w", encoding="utf-8") as f:
            f.write(f"Teste M0-M1-M2 - {datetime.now().strftime('%Y-%m-%d %H:%M')}\n")
            f.write(f"{'='*50}\n\n")

            f.write("RESULTADOS POR MODULO:\n")
            modulo_nomes = {"M0": "Setup", "M1": "Python Basico", "M2": "Dados e Graficos"}
            for mod, dados in modulos.items():
                pct = (dados["acertos"] / dados["total"] * 100) if dados["total"] > 0 else 0
                f.write(f"  {mod} - {modulo_nomes[mod]}: {dados['acertos']}/{dados['total']} ({pct:.0f}%)\n")

            f.write(f"\nDETALHES:\n")
            for r in self.respostas:
                simbolo = "OK" if r["correto"] else "X"
                f.write(f"  P{r['pergunta']:02d} [{r['modulo']}]: {simbolo} ({r['tempo']}s)\n")

            f.write(f"\nTOTAL: {self.pontuacao:.0f}/40 ({self.pontuacao/40*100:.0f}%)\n")
            f.write(f"Tempo total: {minutos}m {segundos}s\n")

        messagebox.showinfo("Guardado", f"Resultado guardado em:\n{nome_ficheiro}")

    def limpar_tela(self):
        """Remove todos os widgets"""
        for widget in self.root.winfo_children():
            widget.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = TesteApp(root)
    root.mainloop()
