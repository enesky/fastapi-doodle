# fastapi-doodle

FastAPI öğrenme ve deneme projesi.

## İlk kurulumda yapılanlar

```bash
# Sanal ortamı oluştur
python3.14 -m venv venv

# Sanal ortamı etkinleştir (macOS / zsh)
source venv/bin/activate

# Paketleri kur
python -m pip install -r requirements.txt

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

POST örneğini üçüncü terminalde çalıştır:

```bash
source venv/bin/activate
python -m uvicorn main-post:app --reload --port 8002
```

POST isteklerini başka bir terminalden test et:

```bash
source venv/bin/activate
python main-post-test.py
```

PUT, PATCH ve DELETE ders örneklerini ayrı portlarda çalıştırabilirsin:

```bash
python -m uvicorn main-put:app --reload --port 8004
python -m uvicorn main-put-patch:app --reload --port 8005
python -m uvicorn main-put-patch-delete:app --reload --port 8006
```

Her komutu ayrı terminalde çalıştır. Swagger adresleri sırasıyla `/docs` eklenmiş 8004, 8005 ve 8006 portlarıdır.

Uvicorn başlangıç ve istek logları ilgili terminalde görünür. Sunucular çalışırken iki terminal de açık kalmalıdır.

- `main.py`: http://127.0.0.1:8000
- `main.py` API dokümantasyonu: http://127.0.0.1:8000/docs
- `main2.py`: http://127.0.0.1:8001
- `main2.py` kurslar: http://127.0.0.1:8001/courses
- `main2.py` API dokümantasyonu: http://127.0.0.1:8001/docs
- `main-post.py`: http://127.0.0.1:8002/docs

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

## Iris veri analizi ve makine öğrenmesi

Alt proje tam Iris veri setini analiz eder, karar ağacı modelini eğitir ve FastAPI üzerinden tahmin sunar.

```bash
cd data-science-ml-fastapi-project
source ../venv/bin/activate
python -m pip install -r requirements.txt
python train_model.py
python -m uvicorn main:app --reload --port 8003
```

- API dokümantasyonu: http://127.0.0.1:8003/docs
- Veri özeti: http://127.0.0.1:8003/data
- Temel analiz: http://127.0.0.1:8003/analysis
- Tahmin: `POST http://127.0.0.1:8003/predict`

## SQLite CRUD API

SQLite kullanan kalıcı GET, POST, PUT, PATCH ve DELETE örneği:

```bash
cd db-fastapi-example
source ../venv/bin/activate
python -m pip install -r requirements.txt
python create_db.py
python -m uvicorn main:app --reload --port 8007
```

- API dokümantasyonu: http://127.0.0.1:8007/docs
- Testler: `python -m pytest -q`

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
