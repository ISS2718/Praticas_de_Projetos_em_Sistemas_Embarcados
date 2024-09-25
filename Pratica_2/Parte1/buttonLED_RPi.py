import RPi.GPIO as GPIO  # Importa a biblioteca RPi.GPIO e a renomeia como GPIO
import time  # Importa a biblioteca time para usar funções de temporização

# Configura o modo de numeração dos pinos como BCM
GPIO.setmode(GPIO.BCM)

# Configura o pino 18 como saída e define seu estado inicial como LOW (desligado)
GPIO.setup(18, GPIO.OUT, initial=0)

# Configura o pino 26 como entrada com um resistor pull-up interno
GPIO.setup(26, GPIO.IN, GPIO.PUD_UP)

try:
    while True:
        # Verifica o estado do pino 26
        if GPIO.input(26):
            # Se o pino 26 estiver em HIGH (botão não pressionado), desliga o LED no pino 18
            GPIO.output(18, GPIO.LOW)
            time.sleep(0.2)  # Aguarda 0.2 segundos
        else:
            # Se o pino 26 estiver em LOW (botão pressionado), liga o LED no pino 18
            GPIO.output(18, GPIO.HIGH)
            time.sleep(0.2)  # Aguarda 0.2 segundos
except KeyboardInterrupt:
    # Captura a interrupção do teclado (Ctrl+C) para sair do loop
    pass

# Limpa a configuração dos pinos GPIO
GPIO.cleanup()