import RPi.GPIO as GPIO  # Importa a biblioteca RPi.GPIO e a renomeia como GPIO
import time  # Importa a biblioteca time para usar funções de temporização

# Configura o modo de numeração dos pinos como BCM
GPIO.setmode(GPIO.BCM)

# Configura o pino 18 como saída e define seu estado inicial como LOW (desligado)
GPIO.setup(18, GPIO.OUT, initial=0)

try:
    # Solicita ao usuário um valor inteiro em segundos
    tempo = int(input("Insira um valor inteiro, em segundos: "))
except ValueError:
    # Captura a exceção se o valor inserido não for um inteiro e exibe uma mensagem de erro
    print("Insira um valor válido.")

try:
    while True:
        if tempo > 0:
            # Calcula os minutos e segundos restantes
            minutos = tempo // 60
            segundos = tempo % 60

            # Exibe a contagem regressiva no formato MM:SS
            print(f"Contagem: {minutos:02}:{segundos:02}...", end="\r")
            tempo = tempo - 1  # Decrementa o tempo em 1 segundo
            time.sleep(1)  # Aguarda 1 segundo

            if tempo == 0:
                # Quando o tempo chega a zero, exibe 00:00 e liga o LED
                print(f"Contagem: 00:00")
                time.sleep(1)  # Aguarda 1 segundo
                GPIO.output(18, GPIO.HIGH)  # Liga o LED no pino 18
                print("Seu LED ligou!")
                tempo = -1  # Define o tempo como -1 para sair do loop
except KeyboardInterrupt:
    # Captura a interrupção do teclado (Ctrl+C) para sair do loop
    pass

# Limpa a configuração dos pinos GPIO
GPIO.cleanup()