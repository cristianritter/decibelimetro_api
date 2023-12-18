# Use uma imagem base, por exemplo, uma imagem do Debian Bullseye
FROM debian:bullseye

# Atualize os pacotes e instale as dependências
RUN apt-get update && \
    apt-get install -y \
    software-properties-common \
    python3=3.9.* \
    python3-pip=18.* \
    curl \
    vim \
    git \
    && rm -rf /var/lib/apt/lists/*

# Defina o diretório de trabalho padrão
WORKDIR /app

# Clone o repositório do GitHub
RUN git clone https://github.com/cristianritter/decibelimetro_api /caminho/no/container

# Copie os arquivos necessários para dentro do contêiner
COPY ./app /app

# Instale as dependências do aplicativo
RUN pip3 install --no-cache-dir -r /app/requirements.txt

# Execute o comando de inicialização do aplicativo
CMD ["python3", "main.py"]
