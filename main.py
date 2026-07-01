from fastapi import FastAPI

app = FastAPI() # FastAPI application instance

@app.get("/") # endpoint for the root URL. Kullanıcı / adresine get isteği yaptığında home fonksiyonu çalıştırılır.
def home():
    return {"message": "Welcome to the FastAPI application!"}


@app.get("/eky")
def bu_test_fonksiyonu():
    return {
        "deneme": "bu test fonksiyonu çalıştı",
        "deneme2": "bu test fonksiyonu çalıştı 2",
        "sonuc": "200",
        "bir de array": ["deneme1", "deneme2", "deneme3"]
    }

# Path paremeter: Kullanıcının url içerisinde değer göndermesi için path parameter kullanılır. Örnek: /items/5 gibi bir url ile 5 değerini alabiliriz.
@app.get("/courses/{course_id}")
def get_course(course_id: int): # course_id parametresi int tipinde olmalı. Eğer kullanıcı string bir değer gönderirse hata alır.
    return {
        "course_id": course_id,
        "message": f"Course ID is {course_id}",
        "title": "FastAPI Course",
    }

# Query parameter: Kullanıcı url içerisinde ? ile başlayan parametreleri gönderebilir. Örnek: /items/?name=FastAPI gibi bir url ile name parametresini alabiliriz.
@app.get("/courses")
def list_courses(level: str | None = None, limit: int = 10): # level parametresi str tipinde olmalı ve opsiyonel. Eğer kullanıcı level parametresini göndermezse None değeri alır. limit parametresi int tipinde olmalı ve default değeri 10.
    return {
        "level": level,
        "limit": limit,
        "courses": [
            {"id": 1, "title": "FastAPI Course", "level": "beginner"},
            {"id": 2, "title": "Django Course", "level": "intermediate"},
            {"id": 3, "title": "Flask Course", "level": "advanced"},
        ],
    }
