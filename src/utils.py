"""Shared helpers: config loading, seeding, timing."""
import random
import time
from pathlib import Path

import numpy as np
import yaml


def load_config(path: str) -> dict:
    """Load the YAML config file that drives the whole pipeline."""
    with open(path, "r") as f:
        return yaml.safe_load(f)


def set_seed(seed: int) -> None:
    """Fix every random source we touch so runs are reproducible."""
    random.seed(seed)
    np.random.seed(seed)


def time_fit_predict(model, X_train, y_train, X_test):
    """Fit + predict, returning predictions, train time (s), and inference
    time (ms per prediction) — the timing half of the six-axis benchmark."""
    t0 = time.perf_counter()
    model.fit(X_train, y_train)
    train_time = time.perf_counter() - t0

    t0 = time.perf_counter()
    preds = model.predict(X_test)
    infer_ms_per_pred = (time.perf_counter() - t0) / len(X_test) * 1000

    return preds, train_time, infer_ms_per_pred


def ensure_dir(path: str) -> Path:
    p = Path(path)
    p.mkdir(parents=True, exist_ok=True)
    return p
