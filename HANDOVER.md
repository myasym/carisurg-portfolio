# Handover — Mercer General ED Triage Classifier

*Standard this page is held to: could a new hire, arriving Monday morning,
clone this repo, read this page, and be running the model by end of day —
without asking a single question?*

## 1. Project summary

This project predicts the Emergency Severity Index (ESI 1–5) for patients
arriving at the Mercer General Hospital Emergency Department, from vitals
and a small set of engineered clinical features (shock index, pulse
pressure, red-flag counts). It's built as a decision-support second opinion
for triage nurses and doctors — not a replacement for clinical judgement —
trained and evaluated on 55,121 historical ED visits.

## 2. Final-model decision

**We ship Logistic Regression** for its combination of full clinical
transparency, the best overall macro-F1 (0.481) across all five ESI levels,
and near-zero inference cost (0.004ms/prediction). Full reasoning, including
the honest trade-off on ESI-1 recall (3/16 caught) against alternatives, is
in [`reports/week7-cost-benefit-memo.md`](reports/week7-cost-benefit-memo.md)
and the audit trail of every model tried is in
[`docs/model-selection.md`](docs/model-selection.md).

## 3. How to run

```bash
git clone <repo-url>
cd carisurg-triage
python3 -m venv .venv && source .venv/bin/activate   # macOS/Linux
pip install -r requirements.txt
python scripts/train.py --config config.yaml
```

Expect console output confirming the cleaned patient count, then the
six-axis benchmark (accuracy, macro precision/recall/F1, train time,
inference time) for the pinned model, and a saved model at
`artifacts/logistic_regression.joblib`.

Run the sanity checks before trusting any of the above:

```bash
pip install pytest
PYTHONPATH=. pytest tests/ -v
```

Both tests must pass (2 passed) before this is considered working.

## 4. Where the data lives

The raw triage export (`yaleemmlc_admissionprediction_triage.csv`) is
**confidential patient data and is git-ignored** — it is not, and must
never be, committed to this repository. Access requires clearance through
Mercer General IT Governance; contact Martina Griffith (Clinical IT Lead)
for access, and place the file at the path set in `config.yaml` →
`data.raw_path` before running anything.

## 5. Known limitations

- **ESI-1 recall is still modest (3/16 in testing)** — the model is a
  support tool, not a substitute for clinical judgement, and must never be
  permitted to auto-override a nurse's triage decision.
- **Single-site data** — trained only on Mercer General's historical
  records; performance on another hospital's population or workflow is
  unverified and likely to shift.
- **Demographics excluded by design** (age, gender, ethnicity, insurance
  status, etc.) — a deliberate Week 4 fairness decision, not an oversight.
  This means the model cannot be audited for demographic bias without a
  separate, explicit sensitivity analysis (see `src/features.py:encode_demographics`).

## 6. Who to ask

- **Model / methodology questions:** Mya Symister (Data Science Lead)
- **Data access / governance:** Martina Griffith (Clinical IT Lead)
- **Clinical validity questions:** Dr. De Freitas / Dr. Reyes

---
*This content also seeds the repo `README.md` install-and-run section.*
