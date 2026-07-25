"""Loading and cleaning — identical logic to the Week 5/6/7 notebooks,
only moved into functions."""
import numpy as np
import pandas as pd


def load_raw(path: str) -> pd.DataFrame:
    """Read the raw triage export."""
    return pd.read_csv(path)


def clean(df: pd.DataFrame, cfg: dict) -> pd.DataFrame:
    """Coerce vitals to numeric, drop invalid-ESI rows, null out
    physiologically impossible readings, encode gender, impute remaining
    gaps with the column median. Logic unchanged from Weeks 5-7 — only
    restructured into a callable function.
    """
    vitals = cfg["data"]["vitals"]
    valid_esi = cfg["data"]["valid_esi_labels"]

    out = df.copy()
    out = out.drop(columns=[c for c in out.columns if c.startswith("Unnamed")],
                    errors="ignore")

    for col in vitals:
        out[col] = pd.to_numeric(out[col], errors="coerce")
    out["esi"] = pd.to_numeric(out["esi"], errors="coerce")
    out = out[out["esi"].isin(valid_esi)].copy()

    out.loc[(out["triage_vital_temp"] < 90) | (out["triage_vital_temp"] > 110),
            "triage_vital_temp"] = np.nan
    out.loc[out["triage_vital_o2"] > 100, "triage_vital_o2"] = np.nan

    out["gender"] = (out["gender"].astype(str).str.strip().str.lower()
                      .map({"male": 0, "m": 0, "female": 1, "f": 1}))

    for col in vitals + ["age", "gender"]:
        out[col] = out[col].fillna(out[col].median())

    out["esi"] = out["esi"].astype(int)
    return out
