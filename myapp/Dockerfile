# Wybór obrazu bazowego
FROM python:3.10-slim

# Ustawienie katalogu roboczego
WORKDIR /app

# Kopiowanie pliku requirements.txt
COPY requirements.txt .

# Instalowanie zależności
RUN pip install --no-cache-dir -r requirements.txt

# Kopiowanie reszty aplikacji
COPY . .

# Eksponowanie portu
EXPOSE 8000

# Uruchamianie aplikacji
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
