from fastapi import FastAPI

app = FastAPI() # FastAPI application instance

@app.get("/") # endpoint for the root URL. Kullanıcı / adresine get isteği yaptığında home fonksiyonu çalıştırılır.
def home():
    return {"message": "Welcome to the FastAPI application!"}