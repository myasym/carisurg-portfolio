"""Model construction and evaluation."""
from sklearn.ensemble import HistGradientBoostingClassifier, RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (accuracy_score, classification_report,
                              confusion_matrix, precision_recall_fscore_support)
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier


def build_model(name: str, params: dict, seed: int):
    """Construct a model from its config block. Supports every model
    family trialled across Weeks 6-7; `name` must match a key under
    `models:` in config.yaml."""
    params = dict(params or {})
    params.setdefault("random_state", seed)

    if name == "logistic_regression":
        return make_pipeline(StandardScaler(), LogisticRegression(**params))
    if name == "decision_tree":
        return DecisionTreeClassifier(**params)
    if name == "random_forest":
        return RandomForestClassifier(n_jobs=-1, **params)
    if name == "gradient_boosting":
        return HistGradientBoostingClassifier(**params)
    raise ValueError(f"Unknown model name in config: {name!r}")


def evaluate(model, X_test, y_test, train_time: float, infer_time_ms: float) -> dict:
    """Six-axis benchmark: accuracy, macro precision/recall/F1, train
    time, inference time — matching the Week 7 benchmark table."""
    preds = model.predict(X_test)
    acc = accuracy_score(y_test, preds)
    prec, rec, f1, _ = precision_recall_fscore_support(
        y_test, preds, average="macro", zero_division=0)

    return {
        "accuracy": round(acc, 3),
        "precision_macro": round(prec, 3),
        "recall_macro": round(rec, 3),
        "f1_macro": round(f1, 3),
        "train_time_s": round(train_time, 2),
        "inference_ms_per_pred": round(infer_time_ms, 3),
        "confusion_matrix": confusion_matrix(y_test, preds).tolist(),
        "classification_report": classification_report(y_test, preds, digits=3),
    }
