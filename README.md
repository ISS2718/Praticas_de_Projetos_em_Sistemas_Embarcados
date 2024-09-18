# Documentação da Atividade Prática - SEL0630: Projetos em Sistemas Embarcados

## Resumo

Esta atividade prática foi dividida em três partes, explorando conceitos fundamentais de programação em sistemas embarcados com a Raspberry Pi. Cada parte se concentrou em diferentes aspectos, incluindo manipulação de GPIO, controle por PWM, uso de sensores, e a introdução à computação paralela com threads e processos.

O uso das bibliotecas `gpiozero` e `RPi.GPIO` para facilitar o controle dos pinos GPIO foi um ponto que permeou as três práticas. 

## Parte 1: Introdução ao GPIO e Contagem Regressiva

Na primeira parte da prática, o foco foi a manipulação de entradas e saídas digitais da Raspberry Pi utilizando a linguagem Python. Os conceitos principais abordados foram:

- **GPIO (General Purpose Input/Output):** Interação direta com os pinos GPIO da Raspberry Pi, que podem ser programados para funcionar como entradas ou saídas.

- **Ambiente Virtual Python:** Configuração de um ambiente isolado para garantir que as bibliotecas utilizadas não conflitem com outros projetos.

## Parte 2: PWM e Sensores

Na segunda parte, o objetivo foi explorar o controle de dispositivos usando PWM (modulação por largura de pulso) e a interação com sensores. PWM permite controlar o tempo em que um sinal fica em nível alto ou baixo, simulando diferentes níveis de tensão. Esta parte incluiu:

- **PWM:** Utilizado para controlar dispositivos como LEDs com diferentes níveis de brilho ou motores.

- **Sensores:** Implementação de scripts que interagem com sensores conectados à Raspberry Pi, como sensores de distância.

## Parte 3: Computação Paralela com Threads e Processos

A terceira parte introduziu os conceitos de computação paralela, com o uso de threads e processos. O foco foi criar aplicações multitarefa, em que várias funções são executadas simultaneamente, sem que uma bloqueie a outra. Conceitos adicionais abordados incluíram:

- **Threads:** Execução paralela de funções dentro do mesmo processo, usando threading.

- **Processos:** Execução de funções em processos separados com multiprocessing, o que pode alocar tarefas para diferentes núcleos da CPU.

- **Mutex e Semáforos:** Ferramentas usadas para garantir sincronização entre tarefas concorrentes, evitando problemas como condições de corrida.
<div align="center">
    <img src="./img/montagem3.gif" width="250" />
</div>