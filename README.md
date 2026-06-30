# fastapi-doodle

FastAPI öğrenme ve deneme projesi.

## İlk kurulumda yapılanlar

```bash
# Sanal ortamı oluştur
python3.14 -m venv venv

# Sanal ortamı etkinleştir (macOS / zsh)
source venv/bin/activate

# Paketleri kur
python -m pip install fastapi uvicorn

# Kurulu paketleri sürümleriyle kaydet
python -m pip freeze > requirements.txt
```

## Projeyi daha sonra tekrar kurmak

```bash
python3.14 -m venv venv
source venv/bin/activate
python -m pip install -r requirements.txt
```

Sanal ortamdan çıkmak için:

```bash
deactivate
```
