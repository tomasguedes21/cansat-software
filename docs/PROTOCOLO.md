# Protocolo de Comunicação CanSat

## 1. Introdução

Este documento descreve o protocolo de comunicação utilizado no projeto CanSat
para transmissão de dados de telemetria entre o satélite e a estação de solo.

O protocolo é baseado em mensagens de texto simples, fáceis de debugar e analisar.

---

## 2. Formato da Mensagem

Cada mensagem segue o formato:
$CANSAT,<timestamp>,<temperatura>,<pressao>,<altitude>,<checksum>

### Descrição dos campos

- **$CANSAT** – Identificador do protocolo
- **timestamp** – Tempo desde o início da missão (segundos)
- **temperatura** – Temperatura em graus Celsius
- **pressao** – Pressão atmosférica em hPa
- **altitude** – Altitude em metros
- **checksum** – Código de verificação de erros em hexadecimal

---

## 3. Checksum

O checksum é calculado através da operação XOR entre os valores ASCII de todos
os caracteres da mensagem, desde `CANSAT` até ao último valor antes do checksum.

Exemplo:
CANSAT,42,21.5,985.3,523.7

O resultado do XOR é convertido para hexadecimal com dois caracteres.

---

## 4. Validação da Mensagem

Uma mensagem é considerada válida se:

- Começar por `$`
- Tiver todos os campos esperados
- O checksum calculado coincidir com o checksum recebido

---

## 5. Exemplo de Mensagem

$CANSAT,42,21.5,985.3,523.7,A3

---

## 6. Vantagens do Protocolo

- Simples e legível
- Fácil de implementar em microcontroladores
- Deteta erros de transmissão
- Adequado para telemetria em tempo real