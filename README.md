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



