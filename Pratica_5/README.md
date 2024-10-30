# Prática 5 - Introdução aos Sistemas Operacionais de Tempo Real e Projeto Final 🚀

## Descrição 📚

Nesta prática, foi explorado o conceito de **Sistemas Operacionais de Tempo Real (RTOS)**, utilizando o **FreeRTOS** no microcontrolador **ESP32**. O foco é implementar tarefas concorrentes com diferentes prioridades e compreender a previsibilidade no controle de recursos em sistemas embarcados.

A prática está dividida em duas partes:

1. **Parte 1**: Implementação de duas **tasks** no **ESP32** com **FreeRTOS**, mostrando o gerenciamento de multitarefas com diferentes níveis de prioridade.
2. **Parte 2**: Desenvolvimento de um **projeto final** que integra uma **Single Board Computer (SBC)**, como a **Raspberry Pi**, rodando **Linux** e o **ESP32** com **FreeRTOS**. Essa integração demonstra a capacidade de combinar o processamento de alto nível da SBC com o controle em tempo real do ESP32.

## Objetivos 🎯

1. Compreender o funcionamento de **Sistemas Operacionais de Tempo Real** e sua aplicação em sistemas embarcados.
2. Utilizar o **FreeRTOS** para gerenciar múltiplas tarefas no **ESP32**.
3. Desenvolver um projeto de integração entre uma **SBC** e o **ESP32**, utilizando comunicação serial ou sem fio para realizar tarefas em tempo real e de alto nível.

## Configuração do Ambiente 🛠️

1. Instalar o **Visual Studio Code** com a extensão **PlatformIO**.
2. Conectar a **ESP32** via porta **USB** e verificar a configuração da porta COM.
3. Configurar a **Raspberry Pi** (ou outra SBC) com **Linux** e preparar o ambiente de desenvolvimento com **Python** ou outra linguagem compatível.

## Implementação 💻

### Parte 1: Implementação de Tarefas no FreeRTOS

- Duas **tasks** foram implementadas no **ESP32** usando **FreeRTOS**:
  - **Task 1**: Pisca um LED a cada 200ms.
  - **Task 2**: Imprime uma contagem na Serial a cada 1 segundo, demonstrando o gerenciamento de multitarefas.

### Parte 2: Projeto Final de Integração

**Nosso projeto é o [**Live Share**](https://github.com/ikuyorih9/LocalShare).**

[![LocalShare_capa](https://github.com/user-attachments/assets/6fbdff6e-75de-410b-9383-fa7181344ce6)](https://github.com/ikuyorih9/LocalShare)

## Resultados 📈

- **Parte 1**: As duas tasks foram executadas com sucesso no **ESP32**, demonstrando a capacidade do **FreeRTOS** de gerenciar tarefas com diferentes prioridades.
- **Parte 2**: Está no repositório [**Live Share**](https://github.com/ikuyorih9/LocalShare).
