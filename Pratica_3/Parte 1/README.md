# 🚀 Projeto de Comunicação I2C

Este projeto demonstra a comunicação entre um dispositivo mestre e um dispositivo escravo usando o protocolo I2C. O arquivo `i2c.py` é um script Python que atua como o mestre, enquanto `sender.ino` é um sketch Arduino que atua como o escravo.

## 📂 Arquivos

### 🐍 i2c.py
Este script Python é responsável por enviar e receber dados via I2C. Ele utiliza a biblioteca `smbus` para comunicação com dispositivos I2C.

### 🔌 sender.ino
Este sketch Arduino configura o dispositivo como um escravo I2C que pode receber comandos do mestre e responder de acordo.

## 🛠️ Instalação

### Python
1. Certifique-se de ter o Python instalado.
2. Instale a biblioteca `smbus`:
    ```sh
    pip install smbus
    ```

### Arduino
1. Abra o Arduino IDE.
2. Carregue o arquivo `sender.ino` no seu Arduino.

## ▶️ Uso

### Python
Execute o script Python:
```sh
python i2c.py