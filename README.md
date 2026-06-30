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

## Uygulamaları çalıştırmak

Birinci VS Code terminalinde `main.py` uygulamasını çalıştır:

```bash
source venv/bin/activate
python -m uvicorn main:app --reload --port 8000
```

İkinci VS Code terminalinde `main2.py` uygulamasını çalıştır:

```bash
source venv/bin/activate
python -m uvicorn main2:app --reload --port 8001
```

Uvicorn başlangıç ve istek logları ilgili terminalde görünür. Sunucular çalışırken iki terminal de açık kalmalıdır.

- `main.py`: http://127.0.0.1:8000
- `main.py` API dokümantasyonu: http://127.0.0.1:8000/docs
- `main2.py`: http://127.0.0.1:8001
- `main2.py` kurslar: http://127.0.0.1:8001/courses
- `main2.py` API dokümantasyonu: http://127.0.0.1:8001/docs

Tarayıcıda uygulamayı açınca terminalde aşağıdakine benzer bir istek logu görünür:

```text
127.0.0.1 - "GET / HTTP/1.1" 200 OK
```

`return` ile dönen mesaj terminale yazılmaz; tarayıcıda görünür. İkinci bir terminalden görmek için:

```bash
curl http://127.0.0.1:8000/
```

Tarayıcının istediği `/favicon.ico` için görülen `404 Not Found` geliştirme sırasında normaldir.

Bir sunucuyu durdurmak için çalıştığı terminalde `Control + C` tuşlarına bas.

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
