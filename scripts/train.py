"""Single entry point: python scripts/train.py --config config.yaml"""
import argparse
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

import joblib
from sklearn.model_selection import train_test_split

from src.data import clean, load_raw
from src.features import add_clinical_features, select_features
from src.model import build_model, evaluate
from src.utils import ensure_dir, load_config, set_seed, time_fit_predict


def main(config_path: str):
    cfg = load_config(config_path)
    set_seed(cfg["seed"])

    df_raw = load_raw(cfg["data"]["raw_path"])
    df = clean(df_raw, cfg)
    print(f"Loaded and cleaned {df.shape[0]} patients, {df.shape[1]} columns.")

    X, y = select_features(df, cfg)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=cfg["data"]["test_size"], stratify=y,
        random_state=cfg["seed"])

    X_train_fe = add_clinical_features(X_train)
    X_test_fe = add_clinical_features(X_test)

    model_name = cfg["final_model"]
    model = build_model(model_name, cfg["models"][model_name], cfg["seed"])

    preds, train_time, infer_ms = time_fit_predict(model, X_train_fe, y_train, X_test_fe)
    results = evaluate(model, X_test_fe, y_test, train_time, infer_ms)

    print(f"\nPinned model: {model_name}")
    for k, v in results.items():
        if k not in ("confusion_matrix", "classification_report"):
            print(f"  {k}: {v}")

    out_dir = ensure_dir("artifacts")
    joblib.dump(model, out_dir / f"{model_name}.joblib")
    print(f"\nSaved model to artifacts/{model_name}.joblib")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default="config.yaml")
    args = parser.parse_args()
    main(args.config)
