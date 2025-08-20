# Základní image Python 3.11
FROM python:3.11-slim

# Nastav pracovní složku uvnitř kontejneru
WORKDIR /app

# Zkopíruj requirements a nainstaluj závislosti
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Zkopíruj celý projekt
COPY . .

# Otevři port 5000
EXPOSE 5000

# Spustit Flask aplikaci přes Gunicorn
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]