# Prática 1: Introdução à Instalação de Sistemas Operacionais em Sistemas Embarcados 🚀

## Descrição 📄
Nesta prática, foi realizada a instalação do sistema operacional Raspberry Pi OS em uma placa Raspberry Pi, utilizando o instalador oficial "Raspberry Pi Imager". Além da instalação, foram configuradas funções essenciais, como o SSH, drivers de câmera e conexão Wi-Fi, visando garantir a segurança e o uso básico da placa em futuras atividades.

## Objetivos 🎯
- Familiarizar-se com o processo de instalação de sistemas embarcados baseados em distribuições Linux, como o Raspberry Pi OS.
- Configurar o usuário root e assegurar a proteção contra acessos não autorizados.
- Habilitar funcionalidades para uso futuro, como SSH, VNC e suporte a câmera.
- Conectar a placa à rede Wi-Fi do laboratório e configurar o acesso remoto via VNC e SSH.

## Passos 🛠️
1. Instalar o Raspberry Pi OS 64-bit com interface gráfica no cartão SD usando o "Raspberry Pi Imager".
2. Alterar a senha do root antes de conectar à internet para garantir a segurança.
3. Configurar a conexão Wi-Fi e habilitar os drivers de câmera e serviços como SSH e VNC.
4. Realizar a conexão remota à placa via SSH e VNC.
5. Executar comandos de diagnóstico, como `neofetch` e `pinout`, para verificar o hardware e o sistema.
6. Atualizar os pacotes e configurar a conexão automática ao Wi-Fi durante o boot.
7. Desligar e armazenar corretamente os equipamentos ao final da prática.

## Comandos Utilizados 💻
- `sudo passwd root`
- `sudo raspi-config`
- `sudo apt update && upgrade`
- `ifconfig`
- `neofetch`
- `pinout`

## Resultados Esperados ✅
- Sistema operacional instalado e configurado corretamente.
- Acesso remoto seguro e funcional via SSH e VNC.
- Placa Raspberry Pi pronta para futuras práticas de laboratório.

## Bibliografia 📚
- [Raspberry Pi Documentation](https://www.raspberrypi.com/documentation/computers/getting-started.html#installing-the-operating-system)
- [RealVNC Viewer Installation](https://linuxhint.com/install-realvnc-vnc-viewer-linux/)