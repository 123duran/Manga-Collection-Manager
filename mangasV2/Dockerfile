# Use an official Python runtime
FROM python:3.11

# Set environment vars
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /mangasV2

# Install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy project files
COPY . .

# Copia o entrypoint e dá permissão
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Expõe a porta esperada pelo Fly.io
EXPOSE 8080

# Usa o script como ponto de entrada
ENTRYPOINT ["/entrypoint.sh"]
