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
