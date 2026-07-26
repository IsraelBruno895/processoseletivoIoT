Relatório de Projeto: Contador de Produção Não-Intrusivo
Identificação do Candidato

Nome completo: Israel Bruno Rodrigues de França

GitHub: IsraelBruno895/processoseletivoIoT

1. Visão Geral da Solução

Objetivo do projeto: Criar um sistema de baixo custo para contar peças em uma linha de produção, eliminando a necessidade de anotações manuais.

O que o sistema faz: Ele atua como um "olho eletrônico" na esteira. Quando uma peça passa, ele registra; se a esteira travar, ele emite um alerta; e permite iniciar um novo turno ao toque de um botão.

Como o usuário interage: O operador da máquina apenas acompanha os números atualizados na tela (ou sistema) e usa um botão físico para zerar a contagem quando o turno acaba.

2. Arquitetura do Sistema

Funcionamento contínuo: O programa funciona em um ciclo infinito e rápido. Ele não "trava" em nenhuma etapa, o que significa que pode ler o sensor e o botão ao mesmo tempo sem perder a contagem de nenhuma peça que passe rápido pela esteira.

Ação e Reação: O "cérebro" do sistema avalia constantemente a luz do ambiente. Se a luz cair drasticamente, ele entende que uma peça passou.

3. Componentes Utilizados (Simulação)

Placa ESP32: O cérebro do projeto, responsável por processar as informações e enviar os dados.

Sensor de Luz (LDR): O "olho" que detecta a sombra das peças passando pela esteira.

Botão Físico: Uma chave de controle simples para o operador reiniciar o sistema (reset de turno).

4. Decisões Técnicas Relevantes

Código Ágil: O sistema foi programado para não ter pausas longas (delays extensos), garantindo que responda imediatamente aos eventos da fábrica.

Ajuste de Sensibilidade (Luz): A lógica do sensor foi invertida e ajustada para lidar perfeitamente com variações de luz, diferenciando de forma clara uma esteira vazia de uma peça bloqueando o caminho.

Precisão nas Mensagens: Os textos de alerta do sistema foram programados para serem exatos, facilitando a leitura por sistemas automatizados de supervisão.

5. Resultados Obtidos

Funcionamento Validado: O sistema contou as peças corretamente, identificou micro-paradas (esteira travada) no tempo exigido e zerou os contadores com precisão.

Aprovação Automática: Todas as simulações e testes automáticos na nuvem (via GitHub Actions e Wokwi) foram concluídos e aprovados com 100% de sucesso.

6. Comentários Adicionais

Principais aprendizados: O projeto proporcionou uma excelente experiência prática sobre como unir o desenvolvimento de hardware com testes automáticos de software. Ficou claro como ajustar o comportamento de componentes físicos (como o ruído de um botão ou a sensibilidade da luz) para que funcionem perfeitamente dentro de ambientes rigorosos de validação.
