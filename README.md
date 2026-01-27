# CanSat Software

Software para o projeto CanSat Júnior.

## Autor
Tomás Guedes

## Objetivo
Desenvolver o sistema de telemetria para o satélite e estação terrestre.

## Estrutura
- `src/` - Código fonte
- `data/` - Dados e logs
- `docs/` - Documentação
- `tests/` - Testes

## Notas de Aprendizagem

### Pergunta M0.1: Porque é importante o PATH?
O PATH é importante porque diz ao sistema operativo onde procurar programas executáveis quando escrevemos um comando no terminal.

### Pergunta M0.2: Diferença entre editor de texto e IDE?
Editor de texto: serve apenas para escrever e editar texto/código, com poucas funcionalidades.
IDE: é um ambiente completo para programar, que além de escrever código permite executar, depurar, detetar erros e gerir projetos.

### Pergunta M0.3: O que é controlo de versões?
Controlo de versões é um sistema que regista e gere as alterações feitas a ficheiros ao longo do tempo, permitindo voltar a versões anteriores, acompanhar mudanças e trabalhar em equipa sem perder trabalho.

### Pergunta M0.4
No comando git add ., o ponto (.) significa “este diretório”, ou seja, todos os ficheiros e subpastas a partir da pasta atual.
Assim, o comando adiciona todas as alterações dessa pasta ao próximo commit.

### Pergunta M1.1 Qual é a diferença entre altitude = 100 e altitude = "100"? Porque é que isto importa?
altitude = 100 é um número (inteiro) que pode ser usado em cálculos, enquanto altitude = "100" é uma string (texto).
Isto importa porque operações matemáticas, comparações e gráficos só funcionam corretamente com números, não com texto.

### Pergunta M1.2 Se tiveres uma lista com 100 leituras e quiseres aceder à leitura número 50, qual índice usas? E porquê?
Usas o índice 49, porque em Python as listas começam a contar no 0, não no 1.
Assim, a leitura 1 está no índice 0, a leitura 50 no índice 49.

### Pergunta M1.3: Qual é a vantagem de usar mensagem["temperatura"] em vez de mensagem[1] (como numa lista)?
Usa-se mensagem["temperatura"] porque o dicionário permite aceder aos dados pelo seu significado, tornando o código mais claro, seguro e independente da ordem dos valores, ao contrário de mensagem[1] numa lista.

### Pergunta M1.4: Qual é a diferença entre print() dentro de uma função e return? Quando deves usar cada um?
print() serve para mostrar valores no ecrã, enquanto return serve para devolver um valor da função para ser usado noutras partes do programa.

### Pegunta M1.5 O que significa o with em with open(...) as f:? O que aconteceria se não o usasses?
O with garante que o ficheiro seja fechado automaticamente, mesmo que ocorra um erro no código. Sem ele, seria necessário usar ficheiro.close() manualmente para evitar fugas de memória ou ficheiros bloqueados pelo sistema. É uma forma mais segura e limpa de gerir recursos no Python.

### Pergunta M1.6 Qual é a diferença entre for e while? Em que situações usarias cada um?
O ciclo for é usado quando sabemos à partida quantas vezes o código vai repetir ou quando percorremos uma lista, enquanto o while é usado quando a repetição depende de uma condição que pode mudar ao longo do tempo.
No for, o controlo das iterações é automático; no while, o programador tem de garantir que a condição deixa de ser verdadeira para evitar ciclos infinitos.

### Pergunta M1.7 Qual é a diferença entre import math e from math import sqrt? Quando usarias cada um?
"import math" importa todo o módulo e obriga a usar o prefixo math. (por exemplo, math.sqrt(9)), o que torna o código mais explícito e evita conflitos de nomes.
from math import sqrt importa apenas a função sqrt, permitindo usá-la diretamente (sqrt(9)), sendo útil quando só precisas dessa função e queres código mais curto.

### Pergunta M1.8 Se fosses adicionar uma nova funcionalidade (ex: detetar anomalias), como organizarias o código? Adicionarias uma nova função ou modificarias uma existente? Porquê?
Eu criaria uma função chamada detetar_anomalias(leitura) ou analisar_tendencia(dados). Esta função seria inserida no fluxo de processamento, logo após a leitura dos dados, mas antes de gerar o relatório.
Existem três razões principais (que são pilares da boa programação):

Princípio da Responsabilidade Única: Cada função deve fazer apenas uma coisa bem feita. A função validar_leitura já tem o trabalho de verificar se os dados são "lixo" (como o None ou o 10000). A "deteção de anomalias" é algo mais inteligente (ex: detetar um incêndio ou uma queda brusca), por isso merece o seu próprio espaço.

Facilidade de Teste: Se o teu programa der erro, é muito mais fácil descobrir se o problema está na validação ou na deteção de anomalias se elas estiverem separadas.

Código Limpo (Reutilização): Se um dia quiseres usar este simulador para outra missão (ex: um rover em vez de um CanSat), podes querer manter a mesma validação de dados, mas mudar completamente as regras de deteção de anomalias. Se estiverem separadas, basta trocar uma função.

### Pergunta M2.1 Qual é a diferença entre uma lista de dicionários (como usaste no M1) e um DataFrame do pandas? Que vantagens vês no DataFrame?
Uma lista de dicionários é simples e faz parte do Python “puro”, mas exige mais código para filtrar, calcular estatísticas ou tratar dados.
Um DataFrame do pandas organiza os dados em forma de tabela (linhas e colunas) e permite fazer essas operações de forma muito mais rápida, legível e eficiente, sendo ideal para análise e estatísticas.

### Pergunta M2.2 Qual é a diferença entre df["temperatura"] e df[["temperatura"]]?
Um DataFrame é uma estrutura de dados do pandas em forma de tabela, com linhas e colunas (semelhante a uma folha de Excel).
Uma Series é uma estrutura de dados do pandas unidimensional, semelhante a uma coluna de uma tabela, que associa cada valor a um índice.
df["temperatura"] devolve uma Series (uma única coluna), enquanto df[["temperatura"]] devolve um DataFrame com uma coluna.
Usa a primeira quando queres trabalhar com valores (cálculos, médias) e a segunda quando precisas de manter o formato de tabela.

### Pergunta M2.3 No contexto do CanSat, porque é útil calcular a "variação de altitude" entre leituras? Que problema poderias detetar se este valor fosse 0 durante muito tempo?
No CanSat, a variação de altitude permite perceber se o satélite está a subir, em queda ou parado, ajudando a identificar as diferentes fases da missão.
Se este valor fosse 0 durante muito tempo, poderia indicar um sensor de altitude bloqueado, falha na transmissão de dados ou que o CanSat ficou preso e deixou de se mover.

### Pergunta M2.4 Porque é importante guardar os gráficos como imagens (PNG) em vez de apenas mostrar na janela? Pensa no contexto de um relatório de missão.
Num relatório de missão, é importante guardar os gráficos como imagens (PNG) porque permite incluí-los no relatório, partilhá-los e analisá-los mais tarde, mesmo sem executar o código.
Mostrar apenas na janela não deixa um registo permanente dos resultados nem garante que todos veem exatamente a mesma informação.

### Pergunta M2.5 No gráfico scatter "Temperatura vs Altitude", que padrão observas? Porque é que isto faz sentido fisicamente?
No gráfico, observa-se uma correlação linear negativa, onde a temperatura diminui de forma constante à medida que a altitude sobe. Fisicamente, isto acontece porque o ar é aquecido principalmente pela superfície terrestre e não diretamente pelo Sol; logo, quanto mais longe do solo, menor o calor. Além disso, a subida do ar causa a sua expansão devido à menor pressão atmosférica, um processo termodinâmico que resulta no arrefecimento natural da massa de ar.

### Reposta Desafio M2.6
O júri não avalia só programação ou gráficos. Eles querem perceber três coisas:
O CanSat funcionou?
Os dados são credíveis?
Aprenderam algo com a missão?
Portanto, eu dividiria a apresentação do dashboard em missão → dados → conclusões.

Dados gerais da missão:
Mesmo antes dos gráficos:
Duração total do voo (s)
Altitude máxima atingida (m)
Velocidade máxima de subida/descida (m/s)
Número total de leituras válidas
Taxa de amostragem (ex: 1 Hz)
Isto mostra controlo da missão.

Indicação clara das fases do voo:
O júri gosta MUITO de ver isto.
Exemplo:
Linhas verticais no gráfico da altitude a marcar:
Lançamento
Início da descida
Cores diferentes por fase

Gráfico MAIS importante: Perfil do voo (Altitude vs Tempo)
Porquê?
Prova que o CanSat:
Subiu
Atingiu altitude significativa
Desceu de forma controlada

2.º Mais importante: Velocidade vertical
Porquê?
Demonstra:
Separação correta
Funcionamento do paraquedas
Segurança da descida

3.º Mais Importante: Temperatura e/ou pressão vs altitude
Porquê?
Mostra coerência física:
Temperatura ↓ com altitude
Pressão ↓ com altitude

O que EU acrescentaria para impressionar o júri
Anotações inteligentes:
No dashboard:
“Altitude máxima: 742 m”
“Início da descida aos 118 s”
“Velocidade média de descida: 3.2 m/s”

Em suma, para apresentar este dashboard a um júri CanSat, eu incluiria métricas globais da missão, como altitude máxima, duração do voo e número de leituras válidas. Os gráficos mais importantes seriam o perfil do voo, que comprova o sucesso do lançamento e da recuperação, a velocidade vertical, que valida o funcionamento do paraquedas, e a evolução da temperatura e da pressão, que demonstra coerência física e fiabilidade dos sensores. Estes elementos permitem concluir que a missão foi bem-sucedida tanto do ponto de vista técnico como científico.

### Pergunta M3.1 Porque e que usamos um checksum em vez de simplesmente confiar que a mensagem chegou correta? Pensa no contexto de transmissao radio.
No contexto de rádio (como o teu CanSat), a transmissão é muito suscetível a ruído eletromagnético, interferências de outros sinais e obstáculos físicos. Estes fatores podem corromper bits individuais, alterando, por exemplo, um valor de temperatura de $25$ para $85$ sem que o sistema perceba o erro.O checksum serve como um "selo de garantia": o recetor refaz o cálculo matemático com os dados recebidos e, se o resultado não coincidir com o selo enviado, ele sabe que a mensagem é lixo e deve ser descartada em vez de processada.
