"""
Teste de Compreensão - Módulo 1 (Interface Gráfica)
Executa com: python teste_m1_gui.py
"""

import tkinter as tk
from tkinter import ttk, messagebox
import time
from datetime import datetime

# Limite de tempo por pergunta (em segundos)
TEMPO_LIMITE = 120

# Definição das perguntas
PERGUNTAS = [
    {
        "numero": 1,
        "titulo": "Output de código",
        "pontos": 3,
        "texto": "O que aparece no ecrã quando este código corre?",
        "codigo": """valores = [10, 20, 30]
total = 0
for v in valores:
    total = total + v
print(total)""",
        "tipo": "escolha",
        "opcoes": ["30", "60", "10, 20, 30", "Erro"],
        "correta": 1,  # índice da opção correta (0-based)
        "explicacao": "O ciclo soma 10+20+30 = 60"
    },
    {
        "numero": 2,
        "titulo": "Dicionários - Output",
        "pontos": 1.5,
        "texto": "O que aparece no ecrã?",
        "codigo": """sensor = {"temp": 25, "pressao": 1013}
print(sensor["temp"] + 5)""",
        "tipo": "escolha",
        "opcoes": ["25", "30", "temp + 5", "Erro"],
        "correta": 1,
        "explicacao": "sensor[\"temp\"] é 25, mais 5 dá 30"
    },
    {
        "numero": 3,
        "titulo": "Dicionários - Chave inexistente",
        "pontos": 1.5,
        "texto": "E se fizermos sensor[\"altitude\"], o que acontece?",
        "codigo": """sensor = {"temp": 25, "pressao": 1013}
print(sensor["altitude"])""",
        "tipo": "escolha",
        "opcoes": ["Aparece 0", "Aparece None", "Erro KeyError", "Cria a chave automaticamente"],
        "correta": 2,
        "explicacao": "A chave \"altitude\" não existe, dá erro KeyError"
    },
    {
        "numero": 4,
        "titulo": "Funções - Output linha 1",
        "pontos": 1.5,
        "texto": "O que aparece na PRIMEIRA linha do output?",
        "codigo": """def verificar(valor):
    if valor > 100:
        return "Alto"
    else:
        return "Normal"

resultado = verificar(50)
print(resultado)
print(verificar(150))""",
        "tipo": "escolha",
        "opcoes": ["Alto", "Normal", "50", "Nada"],
        "correta": 1,
        "explicacao": "verificar(50): 50 não é > 100, logo retorna \"Normal\""
    },
    {
        "numero": 5,
        "titulo": "Funções - Output linha 2",
        "pontos": 1.5,
        "texto": "E na SEGUNDA linha do output?",
        "codigo": """def verificar(valor):
    if valor > 100:
        return "Alto"
    else:
        return "Normal"

resultado = verificar(50)
print(resultado)
print(verificar(150))""",
        "tipo": "escolha",
        "opcoes": ["Alto", "Normal", "150", "Nada"],
        "correta": 0,
        "explicacao": "verificar(150): 150 é > 100, logo retorna \"Alto\""
    },
    {
        "numero": 6,
        "titulo": "Funções - print vs return",
        "pontos": 1,
        "texto": "Qual é a diferença entre print() e return numa função?",
        "codigo": None,
        "tipo": "escolha",
        "opcoes": [
            "São iguais, fazem a mesma coisa",
            "print() mostra no ecrã, return devolve o valor para usar noutro sítio",
            "return mostra no ecrã, print devolve o valor",
            "print() só funciona com números"
        ],
        "correta": 1,
        "explicacao": "print() escreve no ecrã; return devolve um valor que pode ser guardado ou usado"
    },
    {
        "numero": 7,
        "titulo": "Encontrar o bug",
        "pontos": 4,
        "texto": "Este código devia contar quantos números são maiores que 10, mas tem um ERRO. Qual é?",
        "codigo": """numeros = [5, 15, 8, 20, 3]
contador = 0
for n in numeros:
    if n > 10:
    contador = contador + 1
print(contador)""",
        "tipo": "escolha",
        "opcoes": [
            "A variável 'contador' devia começar em 1",
            "Falta indentação na linha 'contador = contador + 1'",
            "O operador > devia ser >=",
            "Falta um return no final"
        ],
        "correta": 1,
        "explicacao": "A linha dentro do if precisa de estar indentada (com espaços)"
    },
    {
        "numero": 8,
        "titulo": "Ficheiros - modo 'w'",
        "pontos": 1,
        "texto": "O que significa o \"w\" no open()?",
        "codigo": """with open("dados.txt", "w") as f:
    f.write("Olá")""",
        "tipo": "escolha",
        "opcoes": [
            "w = wait (esperar)",
            "w = write (escrita)",
            "w = watch (observar)",
            "w = web (internet)"
        ],
        "correta": 1,
        "explicacao": "w significa 'write' - abrir o ficheiro para escrita"
    },
    {
        "numero": 9,
        "titulo": "Ficheiros - sobrescrever",
        "pontos": 1,
        "texto": "Se dados.txt já existir com conteúdo, o que acontece ao conteúdo antigo?",
        "codigo": """with open("dados.txt", "w") as f:
    f.write("Olá")""",
        "tipo": "escolha",
        "opcoes": [
            "O novo texto é adicionado no fim",
            "O conteúdo antigo é apagado e substituído",
            "Dá erro porque o ficheiro já existe",
            "O conteúdo antigo fica protegido"
        ],
        "correta": 1,
        "explicacao": "O modo 'w' apaga o conteúdo existente e escreve de novo"
    },
    {
        "numero": 10,
        "titulo": "Ficheiros - with",
        "pontos": 1,
        "texto": "Para que serve o 'with' neste código?",
        "codigo": """with open("dados.txt", "w") as f:
    f.write("Olá")""",
        "tipo": "escolha",
        "opcoes": [
            "Só serve para dar um nome ao ficheiro",
            "Garante que o ficheiro é fechado automaticamente",
            "Permite escrever várias linhas",
            "Protege o ficheiro com password"
        ],
        "correta": 1,
        "explicacao": "O 'with' garante que o ficheiro é fechado mesmo se houver erro"
    },
    {
        "numero": 11,
        "titulo": "Lógica - Output",
        "pontos": 1.5,
        "texto": "O que aparece no ecrã?",
        "codigo": """temp = 60
pressao = 800

if temp > 50 or pressao < 700:
    print("Crítico")
else:
    print("OK")""",
        "tipo": "escolha",
        "opcoes": ["OK", "Crítico", "Erro", "Nada"],
        "correta": 1,
        "explicacao": "temp > 50 é True (60 > 50), com 'or' basta uma condição ser verdadeira"
    },
    {
        "numero": 12,
        "titulo": "Lógica - Explicação",
        "pontos": 1.5,
        "texto": "Porque é que aparece esse resultado? (pensa no 'or')",
        "codigo": """temp = 60
pressao = 800

if temp > 50 or pressao < 700:
    print("Crítico")
else:
    print("OK")""",
        "tipo": "escolha",
        "opcoes": [
            "Porque ambas as condições são verdadeiras",
            "Porque temp > 50 é True, e com 'or' basta uma ser verdadeira",
            "Porque pressao < 700 é True",
            "Porque o else nunca é executado"
        ],
        "correta": 1,
        "explicacao": "Com 'or', basta UMA condição ser True. temp > 50 é True (60 > 50)"
    }
]


class TesteApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Teste M1 - Compreensão de Python")
        self.root.geometry("850x700")
        self.root.minsize(800, 650)
        self.root.configure(bg="#f0f0f0")

        # Variáveis
        self.pergunta_atual = 0
        self.pontuacao = 0
        self.respostas = []
        self.tempo_inicio_pergunta = None
        self.tempo_inicio_teste = None
        self.selected_option = tk.IntVar(value=-1)

        # Criar interface
        self.criar_tela_inicial()

    def criar_tela_inicial(self):
        """Tela inicial com instruções"""
        self.limpar_tela()

        frame = tk.Frame(self.root, bg="#f0f0f0", padx=40, pady=40)
        frame.pack(expand=True, fill="both")

        tk.Label(frame, text="TESTE DE COMPREENSÃO", font=("Arial", 24, "bold"),
                bg="#f0f0f0", fg="#333").pack(pady=(0, 5))
        tk.Label(frame, text="Módulo 1 - Python Básico", font=("Arial", 16),
                bg="#f0f0f0", fg="#666").pack(pady=(0, 30))

        regras_frame = tk.Frame(frame, bg="#fff", padx=20, pady=20, relief="ridge", bd=2)
        regras_frame.pack(fill="x", pady=20)

        tk.Label(regras_frame, text="Regras:", font=("Arial", 14, "bold"),
                bg="#fff", anchor="w").pack(fill="x")

        regras = [
            "• Responde sem ajuda (sem ChatGPT, sem código)",
            "• Lê bem cada pergunta antes de responder",
            "• Tens 2 minutos por pergunta",
            "• Total: 12 perguntas, 20 pontos"
        ]
        for regra in regras:
            tk.Label(regras_frame, text=regra, font=("Arial", 12),
                    bg="#fff", anchor="w").pack(fill="x", pady=2)

        tk.Button(frame, text="COMEÇAR TESTE", font=("Arial", 16, "bold"),
                 bg="#4CAF50", fg="white", padx=30, pady=15,
                 command=self.iniciar_teste, cursor="hand2").pack(pady=40)

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
        main_frame = tk.Frame(self.root, bg="#f0f0f0", padx=30, pady=15)
        main_frame.pack(expand=True, fill="both")

        # Cabeçalho (fixo no topo)
        header_frame = tk.Frame(main_frame, bg="#f0f0f0")
        header_frame.pack(fill="x", pady=(0, 10))

        tk.Label(header_frame, text=f"Pergunta {self.pergunta_atual + 1} de {len(PERGUNTAS)}",
                font=("Arial", 12), bg="#f0f0f0", fg="#666").pack(side="left")

        # Timer no cabeçalho
        self.label_tempo = tk.Label(header_frame, text="⏱ 0s", font=("Arial", 12),
                                    bg="#f0f0f0", fg="#666")
        self.label_tempo.pack(side="right", padx=(20, 0))

        tk.Label(header_frame, text=f"{pergunta['pontos']} ponto{'s' if pergunta['pontos'] != 1 else ''}",
                font=("Arial", 12, "bold"), bg="#f0f0f0", fg="#4CAF50").pack(side="right")

        # Barra de progresso
        progress = ttk.Progressbar(main_frame, length=400, mode='determinate',
                                   value=(self.pergunta_atual / len(PERGUNTAS)) * 100)
        progress.pack(fill="x", pady=(0, 15))

        # Título da pergunta
        tk.Label(main_frame, text=pergunta["titulo"], font=("Arial", 16, "bold"),
                bg="#f0f0f0", fg="#333").pack(anchor="w", pady=(0, 8))

        # Texto da pergunta
        tk.Label(main_frame, text=pergunta["texto"], font=("Arial", 13),
                bg="#f0f0f0", fg="#333", wraplength=750, justify="left").pack(anchor="w", pady=(0, 12))

        # Código (se houver)
        if pergunta["codigo"]:
            code_frame = tk.Frame(main_frame, bg="#2d2d2d", padx=15, pady=12)
            code_frame.pack(fill="x", pady=(0, 15))

            tk.Label(code_frame, text=pergunta["codigo"], font=("Consolas", 11),
                    bg="#2d2d2d", fg="#f8f8f2", justify="left", anchor="w").pack(anchor="w")

        # Opções
        opcoes_frame = tk.Frame(main_frame, bg="#f0f0f0")
        opcoes_frame.pack(fill="x", pady=8)

        for i, opcao in enumerate(pergunta["opcoes"]):
            rb = tk.Radiobutton(opcoes_frame, text=opcao, variable=self.selected_option,
                               value=i, font=("Arial", 12), bg="#f0f0f0",
                               activebackground="#f0f0f0", cursor="hand2",
                               anchor="w", padx=10, pady=5, wraplength=700)
            rb.pack(fill="x", pady=2)

        # Frame para o botão (fixo em baixo)
        btn_frame = tk.Frame(main_frame, bg="#f0f0f0")
        btn_frame.pack(fill="x", pady=(20, 10))

        # Botão confirmar - bem visível
        self.btn_confirmar = tk.Button(btn_frame, text="✓  CONFIRMAR RESPOSTA",
                                       font=("Arial", 16, "bold"),
                                       bg="#4CAF50", fg="white", padx=30, pady=12,
                                       command=self.confirmar_resposta, cursor="hand2",
                                       relief="raised", bd=3)
        self.btn_confirmar.pack(pady=10)

        self.atualizar_timer()

    def atualizar_timer(self):
        """Atualiza o timer da pergunta"""
        if self.tempo_inicio_pergunta:
            tempo = int(time.time() - self.tempo_inicio_pergunta)
            cor = "#666" if tempo < TEMPO_LIMITE else "#f44336"
            self.label_tempo.config(text=f"⏱ {tempo}s", fg=cor)
            self.root.after(1000, self.atualizar_timer)

    def confirmar_resposta(self):
        """Processa a resposta selecionada"""
        if self.selected_option.get() == -1:
            messagebox.showwarning("Aviso", "Seleciona uma opção antes de confirmar!")
            return

        tempo_resposta = int(time.time() - self.tempo_inicio_pergunta)
        self.tempo_inicio_pergunta = None  # Para o timer

        pergunta = PERGUNTAS[self.pergunta_atual]
        opcao_selecionada = self.selected_option.get()
        correto = opcao_selecionada == pergunta["correta"]

        pontos_obtidos = pergunta["pontos"] if correto else 0
        self.pontuacao += pontos_obtidos

        self.respostas.append({
            "pergunta": self.pergunta_atual + 1,
            "correto": correto,
            "pontos": pontos_obtidos,
            "max": pergunta["pontos"],
            "tempo": tempo_resposta
        })

        # Mostrar feedback
        self.mostrar_feedback(correto, pergunta, pontos_obtidos)

    def mostrar_feedback(self, correto, pergunta, pontos):
        """Mostra feedback da resposta"""
        self.limpar_tela()

        frame = tk.Frame(self.root, bg="#f0f0f0", padx=40, pady=40)
        frame.pack(expand=True, fill="both")

        if correto:
            tk.Label(frame, text="✓ CORRETO!", font=("Arial", 28, "bold"),
                    bg="#f0f0f0", fg="#4CAF50").pack(pady=20)
            tk.Label(frame, text=f"+{pontos} ponto{'s' if pontos != 1 else ''}",
                    font=("Arial", 18), bg="#f0f0f0", fg="#4CAF50").pack()
        else:
            tk.Label(frame, text="✗ INCORRETO", font=("Arial", 28, "bold"),
                    bg="#f0f0f0", fg="#f44336").pack(pady=20)
            tk.Label(frame, text=f"Resposta certa: {pergunta['opcoes'][pergunta['correta']]}",
                    font=("Arial", 14), bg="#f0f0f0", fg="#333", wraplength=600).pack(pady=10)

        # Explicação
        exp_frame = tk.Frame(frame, bg="#fff3e0", padx=20, pady=15, relief="ridge", bd=1)
        exp_frame.pack(fill="x", pady=20)
        tk.Label(exp_frame, text="Explicação:", font=("Arial", 12, "bold"),
                bg="#fff3e0", fg="#e65100", anchor="w").pack(fill="x")
        tk.Label(exp_frame, text=pergunta["explicacao"], font=("Arial", 12),
                bg="#fff3e0", fg="#333", wraplength=650, justify="left").pack(fill="x", pady=(5, 0))

        # Botão continuar
        self.pergunta_atual += 1
        texto_btn = "PRÓXIMA PERGUNTA" if self.pergunta_atual < len(PERGUNTAS) else "VER RESULTADO"
        comando = self.mostrar_pergunta if self.pergunta_atual < len(PERGUNTAS) else self.mostrar_resultado

        tk.Button(frame, text=texto_btn, font=("Arial", 14, "bold"),
                 bg="#2196F3", fg="white", padx=30, pady=12,
                 command=comando, cursor="hand2").pack(pady=30)

    def mostrar_resultado(self):
        """Mostra o resultado final"""
        self.limpar_tela()

        tempo_total = int(time.time() - self.tempo_inicio_teste)
        minutos = tempo_total // 60
        segundos = tempo_total % 60

        frame = tk.Frame(self.root, bg="#f0f0f0", padx=40, pady=30)
        frame.pack(expand=True, fill="both")

        tk.Label(frame, text="RESULTADO DO TESTE", font=("Arial", 24, "bold"),
                bg="#f0f0f0", fg="#333").pack(pady=(0, 20))

        # Pontuação
        cor_nota = "#4CAF50" if self.pontuacao >= 12 else ("#ff9800" if self.pontuacao >= 8 else "#f44336")
        tk.Label(frame, text=f"{self.pontuacao:.1f} / 20", font=("Arial", 48, "bold"),
                bg="#f0f0f0", fg=cor_nota).pack()

        tk.Label(frame, text=f"Tempo total: {minutos}m {segundos}s", font=("Arial", 14),
                bg="#f0f0f0", fg="#666").pack(pady=(10, 20))

        # Classificação
        if self.pontuacao >= 16:
            classificacao = "EXCELENTE! Dominas os conceitos do M1."
            cor_class = "#4CAF50"
            emoji = "🟢"
        elif self.pontuacao >= 12:
            classificacao = "BOM! Tens uma boa base. Revê os erros."
            cor_class = "#8BC34A"
            emoji = "🟡"
        elif self.pontuacao >= 8:
            classificacao = "SUFICIENTE. Alguns conceitos precisam de reforço."
            cor_class = "#ff9800"
            emoji = "🟠"
        else:
            classificacao = "PRECISA DE REFORÇO. Revê o Módulo 1."
            cor_class = "#f44336"
            emoji = "🔴"

        class_frame = tk.Frame(frame, bg=cor_class, padx=20, pady=15)
        class_frame.pack(fill="x", pady=20)
        tk.Label(class_frame, text=f"{emoji} {classificacao}", font=("Arial", 14, "bold"),
                bg=cor_class, fg="white").pack()

        # Detalhes por pergunta
        details_frame = tk.Frame(frame, bg="#fff", padx=15, pady=15, relief="ridge", bd=1)
        details_frame.pack(fill="x", pady=10)

        tk.Label(details_frame, text="Detalhes:", font=("Arial", 12, "bold"),
                bg="#fff", anchor="w").pack(fill="x", pady=(0, 10))

        # Criar canvas com scrollbar para os detalhes
        canvas = tk.Canvas(details_frame, bg="#fff", height=150)
        scrollbar = ttk.Scrollbar(details_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg="#fff")

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        for r in self.respostas:
            simbolo = "✓" if r["correto"] else "✗"
            cor = "#4CAF50" if r["correto"] else "#f44336"
            texto = f"  P{r['pergunta']}: {simbolo} {r['pontos']:.1f}/{r['max']} pts ({r['tempo']}s)"
            tk.Label(scrollable_frame, text=texto, font=("Consolas", 10),
                    bg="#fff", fg=cor, anchor="w").pack(fill="x")

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Botões
        btn_frame = tk.Frame(frame, bg="#f0f0f0")
        btn_frame.pack(pady=20)

        tk.Button(btn_frame, text="GUARDAR RESULTADO", font=("Arial", 12),
                 bg="#607D8B", fg="white", padx=20, pady=8,
                 command=self.guardar_resultado, cursor="hand2").pack(side="left", padx=10)

        tk.Button(btn_frame, text="FECHAR", font=("Arial", 12),
                 bg="#9E9E9E", fg="white", padx=20, pady=8,
                 command=self.root.quit, cursor="hand2").pack(side="left", padx=10)

    def guardar_resultado(self):
        """Guarda o resultado num ficheiro"""
        data = datetime.now().strftime("%Y-%m-%d_%H-%M")
        nome_ficheiro = f"resultado_teste_m1_{data}.txt"

        tempo_total = int(time.time() - self.tempo_inicio_teste)
        minutos = tempo_total // 60
        segundos = tempo_total % 60

        with open(nome_ficheiro, "w", encoding="utf-8") as f:
            f.write(f"Teste M1 - {datetime.now().strftime('%Y-%m-%d %H:%M')}\n")
            f.write(f"{'='*40}\n\n")

            for r in self.respostas:
                simbolo = "✓" if r["correto"] else "✗"
                f.write(f"Pergunta {r['pergunta']}: {simbolo} {r['pontos']:.1f}/{r['max']} ({r['tempo']}s)\n")

            f.write(f"\nTOTAL: {self.pontuacao:.1f}/20\n")
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
