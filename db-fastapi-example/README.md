# FastAPI SQLite CRUD

## Kurulum ve çalıştırma

Ana repo klasöründeki sanal ortamı kullanır:

```bash
source ../venv/bin/activate
python -m pip install -r requirements.txt
python create_db.py
python -m uvicorn main:app --reload --port 8007
```

Swagger: http://127.0.0.1:8007/docs

## Test

```bash
python -m pytest -q
```

Testler geçici SQLite veritabanı kullanır; gerçek `courses.db` dosyasını değiştirmez.
