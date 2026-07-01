import sqlite3
from enum import Enum
from pathlib import Path

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field


DB_PATH = Path(__file__).with_name("courses.db")

app = FastAPI(
    title="FastAPI SQLite CRUD API",
    description="SQLite ile GET, POST, PUT, PATCH ve DELETE örnekleri",
    version="1.0.0",
)


class CourseLevel(str, Enum):
    beginner = "beginner"
    intermediate = "intermediate"
    advanced = "advanced"


class CourseCreate(BaseModel):
    title: str = Field(..., min_length=3, max_length=100)
    description: str = Field(..., min_length=10)
    level: CourseLevel
    price: float = Field(..., ge=0)


class CourseUpdate(CourseCreate):
    pass


class CoursePatch(BaseModel):
    title: str | None = Field(None, min_length=3, max_length=100)
    description: str | None = Field(None, min_length=10)
    level: CourseLevel | None = None
    price: float | None = Field(None, ge=0)


class CourseResponse(CourseCreate):
    id: int
    created_at: str | None = None
    updated_at: str | None = None


def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def get_course_or_404(course_id: int):
    conn = get_connection()
    row = conn.execute(
        """
        SELECT id, title, description, level, price, created_at, updated_at
        FROM courses
        WHERE id = ?
        """,
        (course_id,),
    ).fetchone()
    conn.close()

    if row is None:
        raise HTTPException(status_code=404, detail="Eğitim bulunamadı")
    return dict(row)


@app.get("/")
def home():
    return {"message": "FastAPI SQLite CRUD API"}


@app.get("/courses", response_model=list[CourseResponse])
def list_courses():
    conn = get_connection()
    rows = conn.execute(
        """
        SELECT id, title, description, level, price, created_at, updated_at
        FROM courses
        ORDER BY id
        """
    ).fetchall()
    conn.close()
    return [dict(row) for row in rows]


@app.get("/courses/{course_id}", response_model=CourseResponse)
def get_course(course_id: int):
    return get_course_or_404(course_id)


@app.post("/courses", response_model=CourseResponse, status_code=201)
def create_course(course: CourseCreate):
    conn = get_connection()
    cursor = conn.execute(
        """
        INSERT INTO courses (title, description, level, price)
        VALUES (?, ?, ?, ?)
        """,
        (course.title, course.description, course.level.value, course.price),
    )
    new_course_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return get_course_or_404(new_course_id)


@app.put("/courses/{course_id}", response_model=CourseResponse)
def update_course(course_id: int, course: CourseUpdate):
    conn = get_connection()
    cursor = conn.execute(
        """
        UPDATE courses
        SET title = ?, description = ?, level = ?, price = ?,
            updated_at = CURRENT_TIMESTAMP
        WHERE id = ?
        """,
        (
            course.title,
            course.description,
            course.level.value,
            course.price,
            course_id,
        ),
    )
    conn.commit()
    conn.close()

    if cursor.rowcount == 0:
        raise HTTPException(status_code=404, detail="Eğitim bulunamadı")
    return get_course_or_404(course_id)


@app.patch("/courses/{course_id}", response_model=CourseResponse)
def patch_course(course_id: int, patch_data: CoursePatch):
    course = get_course_or_404(course_id)
    course.update(patch_data.model_dump(exclude_unset=True))

    level = course["level"]
    if isinstance(level, CourseLevel):
        level = level.value

    conn = get_connection()
    conn.execute(
        """
        UPDATE courses
        SET title = ?, description = ?, level = ?, price = ?,
            updated_at = CURRENT_TIMESTAMP
        WHERE id = ?
        """,
        (
            course["title"],
            course["description"],
            level,
            course["price"],
            course_id,
        ),
    )
    conn.commit()
    conn.close()
    return get_course_or_404(course_id)


@app.delete("/courses/{course_id}")
def delete_course(course_id: int):
    course = get_course_or_404(course_id)
    conn = get_connection()
    conn.execute("DELETE FROM courses WHERE id = ?", (course_id,))
    conn.commit()
    conn.close()
    return {"message": "Eğitim başarıyla silindi", "deleted_course": course}
