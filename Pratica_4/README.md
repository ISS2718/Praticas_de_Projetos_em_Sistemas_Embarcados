# Prática 4: Configuração do SystemD para Gerenciar Serviços Personalizados em Sistemas Embarcados 🚀

## Descrição 📄
Esta prática tem como objetivo configurar uma unidade de serviço personalizada (`systemd service unit`) para gerenciar a inicialização automática de uma aplicação em sistemas embarcados com o sistema operacional Linux. A prática foi realizada em uma Raspberry Pi, onde um script para piscar um LED (blink) é configurado para iniciar automaticamente no boot do sistema.

## Objetivos 🎯
- Compreender o processo de inicialização de sistemas embarcados com Linux.
- Criar e configurar uma unidade de serviço no `systemd`.
- Automatizar a inicialização de um script de controle de GPIO em um sistema embarcado.

## Requisitos 📋
- Raspberry Pi com Raspberry Pi OS instalado.
- Circuito com LED conectado à GPIO 18 da Raspberry Pi.
- Acesso ao terminal da Raspberry Pi.

## Passos Realizados 🛠️

1. **Atualização do sistema**  
   Atualizamos o sistema e garantimos compatibilidade de bibliotecas:
   ```bash
   sudo rpi-update
   ```

2. **Criação do Script Bash**  
   Criamos o script `blink.sh` para controlar o piscar do LED:
   ```bash
   #!/bin/bash

   echo 18 > /sys/class/gpio/export
   echo out > /sys/class/gpio/gpio18/direction

   while [ 1 ]
   do
      echo 1 > /sys/class/gpio/gpio18/value
      sleep 0.2s
      echo 0 > /sys/class/gpio/gpio18/value
      sleep 0.2s
   done
   ```

3. **Permissão de Execução**  
   Alteramos as permissões do script:
   ```bash
   chmod +x blink.sh
   ```

4. **Teste do Script**  
   Testamos o script para garantir que o LED pisque corretamente:
   ```bash
   ./blink.sh
   ```

5. **Criação da Unidade de Serviço SystemD**  
   Criamos o arquivo `blink.service` para configurar o serviço no systemd:
   ```ini
   [Unit]
   Description=Blink LED
   After=multi-user.target

   [Service]
   ExecStart=/home/pi/blink.sh
   User=pi

   [Install]
   WantedBy=multi-user.target
   ```

6. **Registro do Serviço no SystemD**  
   Copiamos o arquivo de serviço para o diretório do `systemd`:
   ```bash
   sudo cp blink.service /lib/systemd/system/
   ```

7. **Inicialização do Serviço**  
   Inicializamos o serviço e verificamos seu funcionamento:
   ```bash
   sudo systemctl start blink
   ```

8. **Configuração de Inicialização Automática**  
   Configuramos o serviço para iniciar automaticamente no boot:
   ```bash
   sudo systemctl enable blink
   ```

9. **Reinicialização e Teste**  
   Reiniciamos a Raspberry Pi para verificar se o serviço é inicializado corretamente durante o boot:
   ```bash
   sudo reboot
   ```
 
## Resultados ✅
Se configurado corretamente, o LED deve começar a piscar automaticamente após o boot da Raspberry Pi. Para solucionar problemas, o status do serviço pode ser verificado com:
```bash
sudo systemctl status blink
```

## Utilizando Python 📌

Utilizando o arquivo [`blinkLED.py`](blinkLED.py), criamos o arquivo [`blinkLED.service`](blinkLED.service) para configurar o serviço no systemd:
   ```ini
   [Unit]
   Description=Blink LED
   After=multi-user.target

   [Service]
   ExecStart=python /home/sel/ghi/blinkLED.py
   User=pi

   [Install]
   WantedBy=multi-user.target
   ```
Enfim copiamos esse arquivo para a pasta `/lib/systemd/system/` e habilitamos o serviço para iniciar durante o boot do sistema.

### 🎥 Demonstração de Funcionamento


![Vídeo de demonstração](./img/video_demonstracao.gif)



## Referências 📚
- [Systemd - freedesktop.org](https://www.freedesktop.org/wiki/Software/systemd/)
- [DigitalOcean: How to Use Systemctl](https://www.digitalocean.com/community/tutorials/how-to-use-systemctl-to-manage-systemd-services-and-units-pt)