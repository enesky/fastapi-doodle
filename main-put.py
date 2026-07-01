"""
PUT mevcut bir kaynağı güncellemek için kullanılır.

{
    "id": 1,
    "price": 250
}

{
    "id": 1,
    "price": 500
}
"""

from enum import Enum

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field


app = FastAPI(
    title="FastAPI Eğitim Platformu API - PUT",
    description="FastAPI ile modern backend geliştirme",
    version="1.2.3",
)


class CourseLevel(str, Enum):
    beginner = "beginner"
    intermediate = "intermediate"
    advanced = "advanced"


class CourseCreate(BaseModel):
    title: str = Field(..., min_length=5, max_length=50)
    description: str = Field(..., min_length=5, max_length=50)
    level: CourseLevel
    price: float = Field(..., ge=0)


class CourseResponse(BaseModel):
    id: int
    title: str
    description: str
    level: CourseLevel
    price: float


courses = [
    {
        "id": 1,
        "title": "Yapay Zeka için Python",
        "description": "Yapay zeka ve veri bilimi için Python temelleri",
        "level": "beginner",
        "price": 250,
    },
    {
        "id": 2,
        "title": "Veri Bilimi",
        "description": "Pandas, NumPy, veri analizi ve görselleştirme",
        "level": "intermediate",
        "price": 350,
    },
    {
        "id": 3,
        "title": "Makine Öğrenmesi",
        "description": "Scikit-learn ile makine öğrenmesi modelleri",
        "level": "intermediate",
        "price": 400,
    },
]


@app.put("/courses/{course_id}", response_model=CourseResponse)
def update_course(course_id: int, updated_course: CourseCreate):
    for index, course in enumerate(courses):
        if course["id"] == course_id:
            course_data = {
                "id": course_id,
                "title": updated_course.title,
                "description": updated_course.description,
                "level": updated_course.level,
                "price": updated_course.price,
            }

            courses[index] = course_data
            return course_data

    raise HTTPException(status_code=404, detail="Eğitim bulunamadı.")
