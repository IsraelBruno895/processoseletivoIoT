Identificação do Candidato
Nome completo: Israel Bruno

GitHub: IsraelBruno895

Visão Geral da Solução
Objetivo do projeto: Desenvolver um contador de produção não-intrusivo para monitoramento industrial.

O que o sistema embarcado simulado faz: Executa firmware em MicroPython utilizando um ESP32 para gerenciar sensores e comunicação serial.

Como o usuário interage com ele: Por meio de um botão físico e leituras automatizadas em simulação via Wokwi.

Arquitetura do Sistema Embarcado
Fluxo principal do programa (main.py): Inicializa os componentes e executa um loop contínuo de escuta e monitoramento.

Estrutura de estados, loops ou temporizações: Arquitetura não-bloqueante para evitar perda de sincronia nas janelas de tempo dos testes do simulador.

Interação entre os componentes: O microcontrolador lê sinais analógicos do sensor óptico e estados digitais do botão de controle.

Componentes Utilizados na Simulação (diagram.json)
Placa ESP32 DevKit C v4 (esp): Unidade controladora central.

Sensor LDR (ldr1): Responsável pela detecção de passagem de itens na linha.

Botão Pushbutton (btn1): Utilizado para comandos e reset do sistema.

Decisões Técnicas Relevantes
Organização do código: Estrutura modular limpa e voltada para testes automatizados.

Arquitetura Não-Bloqueante: Essencial para garantir a compatibilidade com a esteira de CI/CD sem perder pulsos ou timing.

Casamento de Strings: Rigor absoluto nas mensagens de log serial para atender às asserções do Wokwi CI.

Resultados Obtidos
Comportamento final do sistema: Inicialização correta dos módulos com mensagens exatas no console serial.

Requisitos atendidos: Ambiente configurado via DevContainer, integração do Wokwi CLI via GitHub Secrets (WOKWI_CLI_TOKEN) e aprovação nos testes automatizados.

Resultado no Wokwi: Simulações e validações concluídas com sucesso no pipeline.

Comentários Adicionais
Principais aprendizados: Aperfeiçoamento prático em automação de testes para sistemas embarcados utilizando Wokwi CLI e GitHub Actions.