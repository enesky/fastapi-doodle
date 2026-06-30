from fastapi import FastAPI

app = FastAPI()

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

@app.get("/")
def home():
    return {"message": "FastApi Eğitim Platformuna Hoşgeldiniz!"}

@app.get("/courses")
def list_courses():
    return courses

@app.get("/courses/{course_id}")
def get_course(course_id: int):
    for course in courses:
        if course["id"] == course_id:
            return course
    return {"error": "Course not found"}