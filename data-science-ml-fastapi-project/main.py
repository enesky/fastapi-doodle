from pathlib import Path

import joblib
import pandas as pd
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field


app = FastAPI(title="Iris Veri Analizi API")

BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "data.json"
MODEL_PATH = BASE_DIR / "models" / "iris_decision_tree_model.joblib"


class IrisInput(BaseModel):
    sepal_length: float = Field(gt=0, description="Sepal uzunluğu")
    sepal_width: float = Field(gt=0, description="Sepal genişliği")
    petal_length: float = Field(gt=0, description="Petal uzunluğu")
    petal_width: float = Field(gt=0, description="Petal genişliği")


def load_dataset():
    """data.json dosyasını okur ve pandas DataFrame'e çevirir."""
    return pd.read_json(DATA_PATH)


def load_model():
    if not MODEL_PATH.exists():
        raise HTTPException(
            status_code=503,
            detail="Model bulunamadı. Önce train_model.py dosyasını çalıştırın.",
        )
    return joblib.load(MODEL_PATH)


@app.get("/")
def home():
    return {"message": "Iris veri analizi API çalışıyor."}


@app.get("/data")
def read_data():
    """Veri setinin yapısını ve ilk beş satırını döndürür."""
    df = load_dataset()
    return {
        "row_count": len(df),
        "column_count": len(df.columns),
        "columns": list(df.columns),
        "first_5_rows": df.head().to_dict(orient="records"),
    }


@app.get("/analysis")
def analyze_dataset():
    """Veri setinin temel istatistiklerini döndürür."""
    df = load_dataset()
    numeric_columns = df.select_dtypes(include="number").columns.tolist()
    categorical_columns = df.select_dtypes(include="object").columns.tolist()

    return {
        "row_count": len(df),
        "column_count": len(df.columns),
        "numeric_columns": numeric_columns,
        "categorical_columns": categorical_columns,
        "missing_values": df.isnull().sum().to_dict(),
        "species_distribution": df["species"].value_counts().to_dict(),
        "numeric_summary": df[numeric_columns].describe().to_dict(),
    }


@app.post("/predict")
def predict_species(input_data: IrisInput):
    """Eğitilmiş karar ağacı modeli ile Iris türünü tahmin eder."""
    artifact = load_model()
    input_df = pd.DataFrame([input_data.model_dump()])
    input_df = input_df[artifact["feature_columns"]]
    prediction = artifact["model"].predict(input_df)[0]

    return {"prediction": prediction}
