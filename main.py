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