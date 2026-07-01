import requests

BASE_URL = "http://127.0.0.1:8002"

# Ana sayfayı kontrol et
response = requests.get(f"{BASE_URL}/", timeout=5)
print("Ana Sayfa:", response.json())
print("Status Code:", response.status_code)

# yeni eğitim ekle
new_course = {
    "title": "Derin Öğrenme",
    "description": "TensorFlow ve Keras ile derin öğrenme modelleri",
    "level": "advanced",
    "price": 500
}
response = requests.post(f"{BASE_URL}/courses", json=new_course, timeout=5)
print("Yeni Eğitim Ekle:", response.json())
print("Status Code:", response.status_code)

# Eğitimleri listele
response = requests.get(f"{BASE_URL}/courses", timeout=5)
print("Eğitimleri Listele:", response.json())
print("Status Code:", response.status_code)

# Belirli bir eğitimi getir
course_id = 1
response = requests.get(f"{BASE_URL}/courses/{course_id}", timeout=5)
print(f"Eğitim ID {course_id} Getir:", response.json())
print("Status Code:", response.status_code)
