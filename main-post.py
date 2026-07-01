"""
POST: Veri ekleme

Kullanıcıdan JSON Body almamız lazım ve bunu almak için Pydantic model kullanırız
    {
        "title": ...,
        "description": ...
    }
"""

from enum import Enum

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field

app = FastAPI()

class CourseLevel(str, Enum):
    BEGINNER = "beginner"
    INTERMEDIATE = "intermediate"
    ADVANCED = "advanced"

class CourseCreate(BaseModel):
    title: str = Field(..., min_length=5, max_length=100, description="Eğitimin başlığı")
    description: str = Field(..., min_length=10, max_length=500, description="Eğitimin açıklaması")
    level: CourseLevel = Field(..., description="Eğitimin seviyesi")
    price: float = Field(..., ge=0, description="Eğitimin fiyatı")


class CourseResponse(CourseCreate):
    id: int

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
    }
]

@app.get("/")
def home():
    return {"message": "FastAPI eğitim platformu"}


@app.get("/courses", response_model=list[CourseResponse])
def list_courses():
    return courses


@app.get("/courses/{course_id}", response_model=CourseResponse)
def get_course(course_id: int):
    for course in courses:
        if course["id"] == course_id:
            return course
    raise HTTPException(status_code=404, detail="Eğitim bulunamadı")


@app.post(
    "/courses",
    response_model=CourseResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_course(course: CourseCreate):
    new_course = {
        "id": max(item["id"] for item in courses) + 1,
        **course.model_dump(),
    }
    courses.append(new_course)
    return new_course
