import RPi.GPIO as GPIO  # Importa a biblioteca para controle dos pinos GPIO do Raspberry Pi
from time import sleep  # Importa a função sleep para pausas no código

GPIO.setmode(GPIO.BCM)  # Configura o modo de numeração dos pinos GPIO
GPIO.setup(18, GPIO.OUT, initial=0)  # Configura o pino 18 como saída e inicializa em 0

pwm = GPIO.PWM(18, 100)  # Configura PWM no pino 18 com frequência de 100 Hz
pwm.start(0)  # Inicia o PWM com duty cycle de 0%

try:
  while True:  # Loop infinito
    print("Ligando...")
    for dc in range(101):  # Aumenta o duty cycle de 0 a 100%
      pwm.ChangeDutyCycle(dc)  # Altera o duty cycle
      sleep(0.01)  # Pausa de 10 ms
    print("Desligando...")
    for dc in range(100, -1, -1):  # Diminui o duty cycle de 100 a 0%
      pwm.ChangeDutyCycle(dc)  # Altera o duty cycle
      sleep(0.01)  # Pausa de 10 ms

except KeyboardInterrupt:
  pass  # Interrompe o loop ao pressionar Ctrl+C

GPIO.cleanup()  # Limpa a configuração dos pinos GPIO