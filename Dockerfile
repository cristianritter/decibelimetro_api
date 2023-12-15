# Use uma imagem base, por exemplo, uma imagem do Ubuntu
FROM debian:bullseye
# Use uma imagem base do Python
FROM python:3.8

# Atualize os pacotes e instale as dependências
RUN apt-get update && apt-get install -y \
    software-properties-common \
    && rm -rf /var/lib/apt/lists/*

RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    pip3 install --no-cache-dir -r requirements.txt

# Instale qualquer software adicional que você precise
RUN apt-get update && apt-get install -y \
    curl \
    vim \
    && rm -rf /var/lib/apt/lists/*


# Instale o Git (se não estiver incluído na imagem base)
RUN apt-get update && apt-get install -y git

# Defina o diretório de trabalho padrão
WORKDIR /app

# Clone o repositório do GitHub
RUN git clone https://github.com/cristianritter/decibelimetro_api /caminho/no/container

# Copie os arquivos necessários para dentro do contêiner
COPY ./app /app

# Execute o comando de inicialização do aplicativo
CMD ["python", "main.py"]