# Data Science ML FastAPI Project

## Yapılacaklar

1. [x] JSON formatında bir veri seti oluştur.
2. [x] Veri setini oku.
3. [x] Veri setinin temel analizlerini yapan bir endpoint tanımla.
4. [x] Veri setini kullanarak bir karar ağacı modeli eğit.
5. [x] Eğitilen model ile endpoint üzerinden tahmin yapılmasını sağla.

## Veri seti

`data.json`, Iris veri setindeki 150 ölçümü ve üç çiçek sınıfını içerir:

- `setosa`
- `versicolor`
- `virginica`

Ölçümler santimetre cinsindedir.

`iris.json` ilk denemede kullanılan 15 satırlık küçük örnek olarak korunmuştur; uygulama ve model `data.json` kullanır.

## Kurulum

Ana repo klasöründeki sanal ortamı kullanmak için:

```bash
source ../venv/bin/activate
python -m pip install -r requirements.txt
```

## Modeli eğitmek

```bash
python train_model.py
```

Model `models/iris_decision_tree_model.joblib` dosyasına yazılır.

## API'yi çalıştırmak

```bash
python -m uvicorn main:app --reload --port 8003
```

Endpoint'ler:

- `GET /`: sağlık mesajı
- `GET /data`: satır, sütun ve ilk beş kayıt
- `GET /analysis`: eksik değerler, sınıf dağılımı ve sayısal özet
- `POST /predict`: eğitilmiş model ile tür tahmini

Örnek tahmin isteği:

```bash
curl -X POST http://127.0.0.1:8003/predict \
  -H "Content-Type: application/json" \
  -d '{"sepal_length":5.1,"sepal_width":3.5,"petal_length":1.4,"petal_width":0.2}'
```
