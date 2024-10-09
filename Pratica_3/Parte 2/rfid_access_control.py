import RPi.GPIO as GPIO  # Importa a biblioteca RPi.GPIO e a renomeia como GPIO
from mfrc522 import SimpleMFRC522  # Importa a classe SimpleMFRC522 da biblioteca mfrc522
from time import sleep  # Importa a função sleep da biblioteca time

# Configura o modo de numeração dos pinos como BCM
GPIO.setmode(GPIO.BCM)

# Configura o pino 1 como saída e define seu estado inicial como LOW (desligado)
GPIO.setup(1, GPIO.OUT, initial=0)

# Configura o pino 7 como saída e define seu estado inicial como LOW (desligado)
GPIO.setup(7, GPIO.OUT, initial=0)

leitor = SimpleMFRC522()  # Inicia o leitor RFID

print("Aproxime o leitor:")  # Solicita ao usuário para aproximar o cartão RFID
while True:
    id, texto = leitor.read()  # Lê o ID e o texto do cartão RFID
    if id == 238563335769 or id == 658019992804:  # Verifica se o ID é permitido
        print("Acesso permitido!")  # Informa que o acesso foi permitido
        GPIO.output(1, GPIO.HIGH)  # Liga o LED verde
    else:
        print("Acesso negado!")  # Informa que o acesso foi negado
        GPIO.output(7, GPIO.HIGH)  # Liga o LED vermelho
    print("ID: " + str(id))  # Exibe o ID do cartão lido
    sleep(2)  # Aguarda 2 segundos
    GPIO.output(1, GPIO.LOW)  # Desliga o LED verde
    GPIO.output(7, GPIO.LOW)  # Desliga o LED vermelho