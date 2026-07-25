"""Feature selection and clinical feature engineering — Weeks 5-7 logic,
moved into functions, logic unchanged."""
import pandas as pd


def select_features(df: pd.DataFrame, cfg: dict):
    """Choose columns; exclude leakage, admin, and demographic fields.
    Demographics are excluded from the base feature set by design — the
    Week 4 fairness decision — not because they lack predictive value."""
    target = cfg["data"]["target"]
    excluded = (cfg["data"]["leakage_excluded"]
                + cfg["data"]["admin_excluded"]
                + cfg["data"]["demographics_excluded"])

    feature_cols = [c for c in df.columns if c != target and c not in excluded]
    return df[feature_cols], df[target]


def add_clinical_features(X: pd.DataFrame) -> pd.DataFrame:
    """Shock index, pulse pressure, SpO2/RR ratio, and three red-flag
    binary markers, plus a summed red-flag count. Built to carry signal
    from vitals other than blood pressure, which is frequently missing
    or unreliable at triage."""
    out = X.copy()
    out["shock_index"] = out["triage_vital_hr"] / out["triage_vital_sbp"]
    out["pulse_pressure"] = out["triage_vital_sbp"] - out["triage_vital_dbp"]
    out["spo2_rr_ratio"] = out["triage_vital_o2"] / out["triage_vital_rr"]
    out["is_tachypneic"] = (out["triage_vital_rr"] > 20).astype(int)
    out["is_hypoxic"] = (out["triage_vital_o2"] < 92).astype(int)
    out["is_febrile"] = (out["triage_vital_temp"] >= 100.4).astype(int)
    out["red_flag_count"] = out[["is_tachypneic", "is_hypoxic", "is_febrile"]].sum(axis=1)
    return out


def encode_demographics(X: pd.DataFrame, df: pd.DataFrame) -> pd.DataFrame:
    """Optional one-hot encoding of demographic fields — OFF by default,
    per the Week 4 fairness decision to exclude demographics from the
    pinned model's base feature set. Provided only as a hook for an
    explicit fairness sensitivity analysis, not for production training.
    """
    raise NotImplementedError(
        "Demographics are excluded from the pinned model by design. "
        "Only wire this in for a deliberate fairness sensitivity "
        "analysis, never for the default training path."
    )
