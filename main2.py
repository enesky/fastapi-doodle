from fastapi import FastAPI, HTTPException

app = FastAPI(
    title="FastAPI Eğitim Platformu",
    description="Bu API, FastAPI ile eğitim platformu için örnek bir uygulamadır.",
    version="1.0.0"
)

tags_metadata = [
    {
        "name": "Genel",
        "description": "Genel işlemler ve bilgiler"
    },
    {
        "name": "Eğitimler",
        "description": "Eğitim platformundaki kurslarla ilgili işlemler"
    },
    {
        "name": "Kullanıcılar",
        "description": "Kullanıcılarla ilgili işlemler"
    }
]

courses = [
    {
        "id": 1,
        "title": "Yapay Zeka için Python",
        "description": "Yapay zeka ve veri bilimi için Python temelleri",
        "level": "beginner",
        "price": 250
    },
    {
        "id": 2,
        "title": "Veri Bilimi",
        "description": "Pandas, NumPy, veri analizi ve görselleştirme",
        "level": "intermediate",
        "price": 350
    },
    {
        "id": 3,
        "title": "Makine Öğrenmesi",
        "description": "Scikit-learn ile makine öğrenmesi modelleri",
        "level": "intermediate",
        "price": 400
    }
]

@app.get(
        "/",
        tags=["Genel"],
        summary="Ana Sayfa",
        description="API'nin ana sayfasına yönlendirme yapar ve hoş geldiniz mesajını döndürür."
    )
def home():
    return {"message": "FastApi Eğitim Platformuna Hoşgeldiniz!"}

@app.get(
        "/courses",
        tags=["Eğitimler"],
        summary="Eğitimleri Listele",
        description="Tüm eğitimleri listeler."
    )
def list_courses():
    return courses

@app.get(
        "/courses/{course_id}",
        tags=["Eğitimler"],
        summary="Eğitim Detaylarını Getir",
        description="Belirtilen ID'ye sahip eğitimi detaylarıyla döndürür."
    )
def get_course(course_id: int):
    for course in courses:
        if course["id"] == course_id:
            return course
    raise HTTPException(status_code=404, detail="Course not found")

"""
200: başarılı
201: oluşturuldu
400: hatalı istek
401: giriş yapılmamış
403: yeti hatası
404: kayıt bulunamadı
422: validation hatası
500: sunucu hatası
"""
