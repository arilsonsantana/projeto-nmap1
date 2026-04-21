# Automação de Varredura de Rede com Python e Nmap

## Descrição
Este projeto automatiza varreduras de rede utilizando Python integrado ao Nmap, permitindo identificar hosts ativos, portas abertas e serviços expostos.

## Objetivo
Simular a fase de reconhecimento em um cenário de cibersegurança, identificando possíveis superfícies de ataque em ambiente controlado.

## Tecnologias utilizadas
- Python
- Nmap
- Kali Linux

## Ambiente de testes
- Máquina de ataque: Kali Linux
- Alvo: servidor com Wazuh
- Rede interna virtualizada

## Execução
python3 scanner.py

Exemplo de entrada:
192.168.0.17

## Exemplo de resultado
Host: 192.168.0.17
Estado: up

Protocolo: tcp
Porta: 22  | Estado: open | Serviço: ssh
Porta: 443 | Estado: open | Serviço: https

## Análise de segurança
A identificação das portas 22 (SSH) e 443 (HTTPS) abertas indica a presença de serviços acessíveis na rede. Esses serviços podem ser explorados por atacantes, caso existam falhas de configuração, credenciais fracas ou ausência de controles de segurança adequados.

## Contexto de cibersegurança
Este projeto simula a fase inicial de reconhecimento, permitindo mapear serviços expostos e apoiar análises de superfície de ataque em laboratório.

## Melhorias futuras
- Exportação de resultados para arquivo
- Integração com Wazuh
- Geração de alertas automatizados

## Autor

Arilson Santana  
Projeto desenvolvido em laboratório de cibersegurança (homelab)
