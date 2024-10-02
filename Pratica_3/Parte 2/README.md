# Parte 2: Controle de Acesso com RFID via SPI 🔐

Esta parte do projeto utiliza o módulo RFID-RC522 conectado à Raspberry Pi via SPI para implementar um sistema de controle de acesso.

## 📂 Arquivos

### 📜 rfid_access_control.py
Este script Python é responsável por interagir com o módulo RFID-RC522 para ler e gravar dados em tags RFID. Ele também implementa a lógica de controle de acesso.

## 🛠️ Instalação

1. Certifique-se de ter o Python instalado na Raspberry Pi.
2. Instale as bibliotecas necessárias:
    ```sh
    pip install mfrc522 spidev
    ```

## ▶️ Uso

1. Conecte o módulo RFID-RC522 à Raspberry Pi via SPI.
2. Execute o script Python:
    ```sh
    python rfid_access_control.py
    ```

## 📋 Funcionalidades

- **Gravação de Dados**: Permite gravar o número USP em uma tag RFID.
- **Controle de Acesso**: Libera ou nega o acesso com base na identificação da tag.

## 🤝 Contribuição

1. Faça um fork do repositório.
2. Crie uma nova branch: `git checkout -b minha-nova-feature`.
3. Faça suas alterações e commit: `git commit -am 'Adiciona nova feature'`.
4. Envie para o branch original: `git push origin minha-nova-feature`.
5. Crie um novo Pull Request.