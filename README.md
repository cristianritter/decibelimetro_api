# Decibelimetro API

Este repositório contém a implementação de uma API para o decibelimetro modelo INS-1355. Os dados de medições são recebidos por meio do protocolo HID em tempo real.

## Instalação

Certifique-se de estar utilizando a distribuição Raspbian GNU/Linux 11 (bullseye). Verifique as informações do sistema no arquivo `os-release.txt`.

Clone o repositório usando o seguinte comando:

```bash
git clone https://github.com/cristianritter/decibelimetro_api
```

## Configuração no Raspberry Pi
Certifique-se de ter o Python instalado no seu Raspberry Pi. Caso não tenha, você pode instalá-lo utilizando o seguinte comando:
```bash
sudo apt-get update
sudo apt-get install python3
```

## Instalação de Dependências
Instale as bibliotecas necessárias com o seguinte comando:
```bash
pip install -r requirements.txt
```

Execução do Aplicativo
Para executar o aplicativo, utilize o seguinte comando:
```bash
sudo python main.py
```

Isso iniciará a API do decibelimetro. Certifique-se de ter as permissões necessárias para acessar os recursos do hardware.

Observação: O comando utiliza sudo para garantir as permissões necessárias para acessar recursos do sistema.

Agora, você pode acessar a API em http://localhost:5000 para interagir com o decibelimetro.


