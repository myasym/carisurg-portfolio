"""Two sanity checks — not proof of correctness, just tripwires so the
pipeline fails loudly if cleaning or training silently breaks."""
import numpy as np
import pandas as pd

from src.data import clean
from src.features import add_clinical_features
from src.model import build_model

CFG = {
    "data": {
        "target": "esi",
        "valid_esi_labels": [1, 2, 3, 4, 5],
        "vitals": ["triage_vital_hr", "triage_vital_sbp", "triage_vital_dbp",
                   "triage_vital_rr", "triage_vital_o2", "triage_vital_temp",
                   "triage_glucose"],
    }
}


def _fake_raw(n=60):
    rng = np.random.default_rng(42)
    return pd.DataFrame({
        "triage_vital_hr": rng.uniform(60, 140, n),
        "triage_vital_sbp": rng.uniform(90, 180, n),
        "triage_vital_dbp": rng.uniform(50, 110, n),
        "triage_vital_rr": rng.uniform(10, 30, n),
        "triage_vital_o2": rng.uniform(85, 100, n),
        "triage_vital_temp": rng.uniform(96, 103, n),
        "triage_glucose": rng.uniform(70, 200, n),
        "gender": rng.choice(["male", "female"], n),
        "age": rng.uniform(1, 90, n),
        "esi": rng.choice([1, 2, 3, 4, 5], n),
    })


def test_clean_produces_valid_schema():
    """Data contract: valid ESI labels only, no vital gaps, gender encoded."""
    raw = _fake_raw()
    df = clean(raw, CFG)
    assert df["esi"].isin([1, 2, 3, 4, 5]).all()
    assert df["triage_vital_hr"].isna().sum() == 0
    assert set(df["gender"].unique()) <= {0, 1}


def test_smoke_train_predict():
    """Does the pipeline run end-to-end on a tiny slice without crashing?"""
    raw = _fake_raw(60)
    df = clean(raw, CFG)
    X = df.drop(columns=["esi"])
    X = add_clinical_features(X)
    y = df["esi"]

    X_train, y_train = X.iloc[:40], y.iloc[:40]
    X_test, y_test = X.iloc[40:], y.iloc[40:]

    model = build_model("logistic_regression", {"max_iter": 1000}, seed=42)
    model.fit(X_train, y_train)
    preds = model.predict(X_test)

    assert len(preds) == len(y_test)
