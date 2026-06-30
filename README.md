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

## İlk FastAPI uygulaması

`main.py` dosyasını oluştur ve aşağıdaki kodu ekle:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to the FastAPI application!"}
```

## Uygulamayı çalıştırmak

```bash
python -m uvicorn main:app --reload
```

Bu komutu VS Code terminalinde çalıştır. Uvicorn başlangıç ve istek logları aynı terminalde görünür. Sunucu çalışırken terminal açık kalmalıdır.

- Uygulama: http://127.0.0.1:8000
- API dokümantasyonu: http://127.0.0.1:8000/docs

Tarayıcıda uygulamayı açınca terminalde aşağıdakine benzer bir istek logu görünür:

```text
127.0.0.1 - "GET / HTTP/1.1" 200 OK
```

`return` ile dönen mesaj terminale yazılmaz; tarayıcıda görünür. İkinci bir terminalden görmek için:

```bash
curl http://127.0.0.1:8000/
```

Tarayıcının istediği `/favicon.ico` için görülen `404 Not Found` geliştirme sırasında normaldir.

Sunucuyu durdurmak için terminalde `Control + C` tuşlarına bas.

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
