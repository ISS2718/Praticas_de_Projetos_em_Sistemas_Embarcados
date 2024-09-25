# Prática 3: Protocolos de Comunicação em Sistemas Embarcados 🚀

## Descrição 📚
Nesta prática, foram explorados protocolos de comunicação em sistemas embarcados, especificamente I2C e SPI. Utilizando a Raspberry Pi e um microcontrolador Arduino, foram implementadas comunicações seriais para leitura de dados analógicos e controle de acesso via tags RFID.

## Objetivos 🎯
- Implementar comunicação serial I2C entre a Raspberry Pi e o Arduino.
- Realizar leituras analógicas no Arduino e enviá-las para a Raspberry Pi via I2C.
- Utilizar o protocolo SPI para controle de acesso com RFID.
- Gravar e ler dados de uma tag RFID e implementar um sistema de controle de acesso básico.

## Parte 1: Comunicação I2C entre Raspberry Pi e Arduino 🔄
- Programar o Arduino para ler valores analógicos de um potenciômetro.
- Estabelecer uma comunicação I2C entre a Raspberry Pi e o Arduino utilizando um level-shifter para adequar os níveis lógicos de tensão.
- Implementar um script em Python para a Raspberry Pi solicitar dados ao Arduino via I2C e exibir o valor no terminal.

### Comandos Utilizados 💻
- `smbus.SMBus(1)` para acessar o barramento I2C na Raspberry Pi.
- `Wire.begin()` no Arduino para inicializar o I2C.
- `Bus.read_i2c_block_data()` para ler os dados enviados pelo Arduino.

## Parte 2: Controle de Acesso com RFID via SPI 🔐
- Utilizar o módulo RFID-RC522 conectado à Raspberry Pi via SPI para controle de acesso.
- Programar a gravação de dados (número USP) em uma tag RFID.
- Implementar um sistema que libera ou nega o acesso com base na identificação da tag.

### Ferramentas Utilizadas 🛠️
- `mfrc522` biblioteca Python para comunicação com o módulo RFID.
- `RFID.write()` para gravar dados na tag.
- `RFID.read()` para ler a identificação da tag e decidir se o acesso é liberado ou negado.

## Resultados Esperados ✅
- Comunicação funcional entre Raspberry Pi e Arduino via I2C, com leitura de valores analógicos.
- Sistema de controle de acesso por RFID funcional, com gravação e leitura de tags.
- Scripts em Python implementados para gerenciar a comunicação e exibir os resultados no terminal.

## Entregas 📦
- Dois scripts `.py` comentados, um referente à comunicação I2C (Parte 1) e outro referente ao controle de acesso RFID via SPI (Parte 2).
- Documentação em PDF ou README.md contendo explicações dos conceitos e fotos da montagem prática.
- Prints dos terminais confirmando o funcionamento da comunicação I2C e do sistema de controle de acesso.

## Bibliografia 📖
- [I2C Communication Between Arduino & Raspberry Pi](https://dronebotworkshop.com/i2c-arduino-raspberry-pi/)
- [mfrc522 Python Library](https://pypi.org/project/mfrc522-python/)
- [SMBus Documentation](https://buildmedia.readthedocs.org/media/pdf/smbus2/latest/smbus2.pdf)