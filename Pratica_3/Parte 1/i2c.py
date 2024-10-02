from smbus import SMBus
from time import sleep

addr = 0x8
Bus = SMBus(1)

SDA_pin = 2
SDL_pin = 3

while True:
#       data = Bus.read_byte_data(addr,0x01)
#       print(f"{data}")
  data = Bus.read_i2c_block_data(addr, 0, 2)
  value = data[0]*256 + data[1]
  print(f"Potenciometro = {value} - [{data[0]} {data[1]}]")
  sleep(0.5)