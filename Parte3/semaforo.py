import RPi.GPIO as GPIO
import threading
from gpiozero import DistanceSensor, RGBLED
from time import sleep

# Inicializa semáforo e mutex para controle de concorrência
sem = threading.Semaphore(1)
mutex = threading.Lock()

# Definição dos pinos dos LEDs
pinLed1 = [14, 17, 23]
pinLed2 = [15, 27, 24]
pinLed3 = [18, 22, 25]

# Declaração dos LEDs RGB
led1 = RGBLED(red=pinLed1[0], green=pinLed1[1], blue=pinLed1[2])
led2 = RGBLED(red=pinLed2[0], green=pinLed2[1], blue=pinLed2[2])
led3 = RGBLED(red=pinLed3[0], green=pinLed3[1], blue=pinLed3[2])

# Inicializa LEDs na cor vermelha
led1.red = 1
led2.red = 1
led3.red = 1

# Função que controla o ciclo do semáforo
def semaforo(led):
    sem.acquire()
    while True:
        try:
            with mutex:
                led.color = (0, 1, 0)  # Verde
                print(f"{led}: Verde...")
                sleep(3)
                led.color = (1, 0.3, 0)  # Amarelo
                print(f"{led}: Amarelo")
                sleep(3)
                led.color = (1, 0, 0)  # Vermelho
                print(f"{led}: Vermelho")
            sleep(1)
        finally:
            sem.release()
            sleep(1)

# Execução principal
if __name__ == '__main__':
    try:
        # Cria e inicia threads para cada LED
        thread1 = threading.Thread(target=semaforo, args=(led1,))
        thread2 = threading.Thread(target=semaforo, args=(led2,))
        thread3 = threading.Thread(target=semaforo, args=(led3,))

        thread1.start()
        thread2.start()
        thread3.start()

        # Aguarda a conclusão das threads
        thread1.join()
        thread2.join()
        thread3.join()
    except KeyboardInterrupt:
        # Desliga os LEDs em caso de interrupção
        led1.color(0, 0, 0)
        led2.color(0, 0, 0)
        led3.color(0, 0, 0)