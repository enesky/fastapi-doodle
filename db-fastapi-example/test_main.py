import main
import pytest
from fastapi.testclient import TestClient


@pytest.fixture()
def client(tmp_path, monkeypatch):
    test_db_path = tmp_path / "test_courses.db"
    monkeypatch.setattr(main, "DB_PATH", test_db_path)

    conn = main.get_connection()
    conn.execute(
        """
        CREATE TABLE courses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT NOT NULL,
            level TEXT NOT NULL,
            price REAL NOT NULL,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP,
            updated_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
        """
    )
    conn.execute(
        """
        INSERT INTO courses (title, description, level, price)
        VALUES (?, ?, ?, ?)
        """,
        (
            "Python Eğitimi",
            "Python temellerini anlatan eğitim",
            "beginner",
            100.0,
        ),
    )
    conn.commit()
    conn.close()
    return TestClient(main.app)


def test_crud_flow(client):
    response = client.get("/courses")
    assert response.status_code == 200
    assert len(response.json()) == 1

    response = client.post(
        "/courses",
        json={
            "title": "FastAPI Eğitimi",
            "description": "FastAPI ile backend geliştirme eğitimi",
            "level": "intermediate",
            "price": 250,
        },
    )
    assert response.status_code == 201
    course_id = response.json()["id"]

    response = client.put(
        f"/courses/{course_id}",
        json={
            "title": "Güncel FastAPI Eğitimi",
            "description": "Güncel FastAPI backend geliştirme eğitimi",
            "level": "advanced",
            "price": 300,
        },
    )
    assert response.status_code == 200
    assert response.json()["price"] == 300

    response = client.patch(f"/courses/{course_id}", json={"price": 325})
    assert response.status_code == 200
    assert response.json()["price"] == 325

    response = client.delete(f"/courses/{course_id}")
    assert response.status_code == 200
    assert response.json()["deleted_course"]["id"] == course_id

    assert client.get(f"/courses/{course_id}").status_code == 404


@pytest.mark.parametrize(
    "payload",
    [
        {
            "title": "Py",
            "description": "Python temellerini anlatan eğitim",
            "level": "beginner",
            "price": 100,
        },
        {
            "title": "Python Eğitimi",
            "description": "Python temellerini anlatan eğitim",
            "level": "easy",
            "price": 100,
        },
        {
            "title": "Python Eğitimi",
            "description": "Python temellerini anlatan eğitim",
            "level": "beginner",
            "price": -10,
        },
    ],
)
def test_create_validation(client, payload):
    assert client.post("/courses", json=payload).status_code == 422


def test_missing_course(client):
    assert client.get("/courses/999").status_code == 404
    assert client.delete("/courses/999").status_code == 404
