import RPi.GPIO as GPIO  # Importa a biblioteca RPi.GPIO e a renomeia como GPIO
from time import sleep  # Importa a função sleep da biblioteca time

# Configura o modo de numeração dos pinos como BCM
GPIO.setmode(GPIO.BCM)

# Configura o pino 18 como saída e define seu estado inicial como LOW (desligado)
GPIO.setup(4, GPIO.OUT, initial=0)

while True:
  GPIO.output(4, 1)  # Liga a Ventoinha
  sleep(2) #Aguarda 2 segundos
  GPIO.output(4, 0) #Desliga a Ventoinha
  sleep(2) #Aguarda 2 segundos