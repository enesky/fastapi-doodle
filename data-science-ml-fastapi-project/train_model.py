from pathlib import Path

import joblib
import pandas as pd
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier


BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "data.json"
MODEL_DIR = BASE_DIR / "models"
MODEL_PATH = MODEL_DIR / "iris_decision_tree_model.joblib"


def load_dataset():
    return pd.read_json(DATA_PATH)


def train_model():
    """Iris veri seti ile karar ağacı modeli eğitir."""
    df = load_dataset()

    feature_columns = [
        "sepal_length",
        "sepal_width",
        "petal_length",
        "petal_width",
    ]
    target_column = "species"

    X = df[feature_columns]
    y = df[target_column]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y,
    )

    model = DecisionTreeClassifier(random_state=42)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)

    print("Accuracy:", accuracy)
    print(classification_report(y_test, y_pred, zero_division=0))

    MODEL_DIR.mkdir(exist_ok=True)
    model_artifact = {
        "model": model,
        "feature_columns": feature_columns,
        "target_column": target_column,
        "classes": sorted(y.unique().tolist()),
    }
    joblib.dump(model_artifact, MODEL_PATH)
    print("Model saved:", MODEL_PATH)


if __name__ == "__main__":
    train_model()
