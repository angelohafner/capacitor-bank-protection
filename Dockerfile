# Usa imagem Python leve
FROM python:3-slim

# Instala compiladores, LaTeX, pacotes de idioma, bibliografia e fontes
RUN apt-get update && apt-get install -y \
    build-essential \
    g++ \
    make \
    perl \
    wget \
    python3-dev \
    fonts-liberation \
    texlive-xetex \
    texlive-latex-recommended \
    texlive-latex-extra \
    texlive-bibtex-extra \
    texlive-pictures \
    texlive-fonts-recommended \
    texlive-fonts-extra \
    texlive-lang-portuguese \
    texlive-humanities \
    latexmk \
    biber \
    && rm -rf /var/lib/apt/lists/*

# Faz com que o Python exiba logs imediatamente
ENV PYTHONUNBUFFERED True

# Define o diretório de trabalho no contêiner
WORKDIR /app

# Copia o código da aplicação para o contêiner
COPY . ./

# Instala dependências Python, se houver
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Expõe a porta padrão do Streamlit
EXPOSE 8080

# Comando padrão ao iniciar o contêiner
CMD ["streamlit", "run", "--server.port", "8080", "--server.enableCORS", "false", "main.py"]
