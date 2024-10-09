# Parte 2: Controle de Acesso com RFID via SPI 🔐

Esta parte do projeto utiliza o módulo RFID-RC522 conectado à Raspberry Pi via SPI para implementar um sistema de controle de acesso.

## 📂 Arquivos

### 📜 rfid_access_control.py
Este script Python é responsável por interagir com o módulo RFID-RC522 para ler e gravar dados em tags RFID. Ele também implementa a lógica de controle de acesso.

## 🛠️ Instalação

1. Certifique-se de ter o Python instalado na Raspberry Pi.
2. Instale as bibliotecas necessárias:
    ```sh
    pip install mfrc522 spidev RPi.GPIO
    ```
    
## ▶️ Uso

1. Conecte o módulo RFID-RC522 à Raspberry Pi via SPI.
2. Execute o script Python:
    ```sh
    python rfid_access_control.py
    ```

## 📋 Funcionalidades

- **Gravação de Dados**: Permite identificar ID de uma tag RFID.
- **Controle de Acesso**: Libera ou nega o acesso com base na identificação da tag.

## 🎥 Demonstração de Funcionamento

<div align="center">
    <img src="./img/video-parte2.gif" width="400" />
</div>