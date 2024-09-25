#
# A aplicação escolhida foi um sensor de distância ultrassônico que emite um som de acordo com a distância medida,
# baseado nos "sensores de ré" de um carro.
# O sensor de distância é inicializado e a frequência do buzzer é ajustada de acordo com a distância medida.
#
import RPi.GPIO as GPIO
from gpiozero import DistanceSensor, LED
from time import sleep

# Definição dos pinos GPIO
pinBuz = 24
pinEcho = 17
pinTrig = 4

# Configuração do modo de numeração dos pinos
GPIO.setmode(GPIO.BCM)
# Configuração do pino do buzzer como saída e inicialização em 0
GPIO.setup(pinBuz, GPIO.OUT, initial=0)

# Inicialização do sensor de distância
sensor = DistanceSensor(pinEcho, pinTrig)
# Configuração do PWM no pino do buzzer com frequência inicial de 10Hz
pwm = GPIO.PWM(pinBuz, 10)
pwm.start(50)  # Inicia o PWM com duty cycle de 50%

try:
  while True:
    # Leitura da distância medida pelo sensor
    distancia = sensor.distance
    print(f"Distancia {distancia:.3f}")
    
    freq = 0  # Inicialização da frequência do buzzer
    
    # Condição para distância entre 0.15m e 0.4m
    if distancia < 0.4 and distancia > 0.15:
      # Cálculo da frequência do buzzer baseado na distância
      freq = 50 * (0.003125)**(distancia) - 4
      pwm.ChangeDutyCycle(50)  # Ajusta o duty cycle para 50%
      pwm.ChangeFrequency(freq)  # Ajusta a frequência do PWM
    elif distancia <= 0.15:
      # Se a distância for menor ou igual a 0.15m, buzzer emite som contínuo
      pwm.ChangeDutyCycle(100)  # Ajusta o duty cycle para 100%
      pwm.ChangeFrequency(442)  # Ajusta a frequência para 442Hz
    else:
      # Se a distância for maior que 0.4m, buzzer é desligado
      pwm.ChangeDutyCycle(0)  # Ajusta o duty cycle para 0%
    
    print(f"Frequencia: {freq:.3f}")
except KeyboardInterrupt:
  pass  # Permite a interrupção do loop com Ctrl+C

# Limpeza da configuração dos pinos GPIO
GPIO.cleanup()