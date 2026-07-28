# CariSurg Portfolio

## Overview

This repository documents my work throughout the **CariSurg MedTech Pathways Programme**, tracking the development of an AI-assisted Emergency Severity Index (ESI) prediction model for emergency department triage.

The project progresses from foundational clinical data cleaning and exploratory analysis through feasibility assessment, baseline model development, and model optimisation. As the programme continues, this repository will be updated with additional modelling, evaluation, and deployment work.

**Current project handover (implementation notes, data governance, known limitations, and outstanding work):** see [`docs/HANDOVER.md`](docs/HANDOVER.md).

**Complete audit trail of model development and selection:** see [`docs/model_selection.md`](docs/model_selection.md).

---

## Before You Start: System Requirements

**Python version: 3.10, 3.11, or 3.12.**

Do not use Python 3.13 or 3.14. Several of the pinned packages in `requirements.txt` (particularly `numpy`) do not yet have ready-built installers for these newer Python versions. Pip will instead try to *compile* numpy from source on your machine, which frequently fails with a wall of C++ compiler errors — this is a known issue with the package, not a mistake in this repository's code.

To check what Python version you currently have:

```bash
python3 --version
```

If it reports 3.13 or higher, install an older version before continuing (macOS, using Homebrew):

```bash
brew install python@3.12
```

You will use `python3.12` specifically (instead of `python3`) in the setup steps below, to make sure the virtual environment is built with the right version.

**Also required:** `git`, and `pip` (comes bundled with Python).

---

## Installation

**1. Clone the repository:**

```bash
git clone https://github.com/myasymi/carisurg-portfolio.git
cd carisurg-portfolio
```

**2. Create and activate a virtual environment**, specifying the Python version explicitly:

```bash
python3.12 -m venv .venv
source .venv/bin/activate
```

(On Windows, activate with `.venv\Scripts\activate` instead of the line above.)

Your terminal prompt should now show `(.venv)` at the start of the line, confirming the environment is active.

**3. Install the pinned dependencies:**

```bash
pip install -r requirements.txt
```

This should complete by downloading pre-built packages, without any compiler output. If you see long blocks of C/C++ compiler warnings or errors here, you are very likely on an unsupported Python version — revisit the section above.

---

## Data

The emergency department dataset is **not included** in this repository, and must never be committed to it. It contains confidential patient information and is excluded from version control via `.gitignore`.

To run the pipeline, you need to place a copy of the dataset file on your own computer, in the exact location the pipeline expects:

1. Obtain the dataset file (`yaleemmlc_admissionprediction_triage.csv`) through the governed access process described in `docs/HANDOVER.md`.
2. Copy that file into the `data/` folder inside your local clone of this repository, so the path reads:
   ```
   carisurg-portfolio/data/yaleemmlc_admissionprediction_triage.csv
   ```
3. Check the filename matches **exactly** — same spelling, same capitalisation — as this exact string is what `config.yaml` looks for.

See the diagram below for exactly where this file goes:

<img width="654" height="343" alt="image" src="https://github.com/user-attachments/assets/56c92613-fbbc-4faf-bdf1-0a41f94c61d2" />


A `data/README.md` file is also included in the `data/` folder itself, explaining the same thing at the point where you'll actually be looking for it.

**A safety note:** placing the file in `data/` will not cause it to be committed to GitHub — `.gitignore` excludes this folder's contents automatically. You can confirm this at any time by running `git status` after adding the file; it should not appear as a change ready to be committed.

---

## Running the Pipeline

Once your environment is set up and the data file is in place, train the pinned model with:

```bash
python scripts/train.py --config config.yaml
```

This will:
1. Load and clean the raw dataset.
2. Engineer the clinical features (shock index, red-flag counts, etc.).
3. Train the pinned Logistic Regression model.
4. Print a six-axis benchmark (accuracy, precision, recall, F1, training time, inference time) to your terminal.
5. Save the trained model to `artifacts/logistic_regression.joblib`.

**Verify the pipeline is working correctly** by running the automated sanity checks:

```bash
PYTHONPATH=. pytest tests/ -v
```

You should see `2 passed`. If either test fails, something in your setup or environment needs attention before the model output can be trusted.

---

## Repository Progress

The repository is organised to reflect the progression of the CariSurg programme.

### Orientation
Foundational exercises introducing clinical datasets, data quality, and exploratory analysis.
- `docs/0_orientation/`
- `notebooks/0_orientation/`

### Research
Background research, project planning, and workflow design.
- `docs/1_research/`
- `notebooks/1_research/`

### Model Development
Exploratory data analysis and feasibility assessment of the emergency department dataset.
- `docs/2_model_development/`
- `notebooks/2_model_development/`

### Baseline Model
Development and evaluation of baseline machine learning models.
- `docs/3_baseline_model/`
- `notebooks/3_baseline_model/`

### Model Optimisation
Benchmarking, optimisation, model comparison, and clinical evaluation.
- `docs/4_model_optimisation/`
- `notebooks/4_model_optimisation/`

---

## Current Project Status

At the current stage of the programme, the repository includes:

- Clinical data cleaning pipelines
- Exploratory data analysis
- Feature engineering
- Baseline model development
- Model benchmarking and optimisation
- A reproducible, config-driven training pipeline
- Automated pipeline testing
- Clinical documentation and decision records

The project is still in active development and will continue to evolve over the remaining weeks of the programme.

---

## Repository Structure

```
carisurg-portfolio/
├── config.yaml
├── LICENSE
├── README.md
├── requirements.txt
├── scripts/
│   └── train.py
├── src/
│   ├── data.py
│   ├── features.py
│   ├── model.py
│   └── utils.py
├── tests/
│   └── test_pipeline.py
├── data/
│   └── README.md   
├── notebooks/
│   ├── 0_orientation/
│   ├── 1_research/
│   ├── 2_model_development/
│   ├── 3_baseline_model/
│   └── 4_model_optimisation/
└── docs/
    ├── 0_orientation/
    ├── 1_research/
    ├── 2_model_development/
    ├── 3_baseline_model/
    ├── 4_model_optimisation/
    ├── decisions/
    ├── figs/
    │   └── data-placement-diagram.svg
    ├── HANDOVER.md
    └── model_selection.md
```

---

## Current Best Model

At the current stage of the programme, **Logistic Regression** has been selected as the leading model following comparative evaluation of multiple baseline and optimised algorithms.

**In one sentence:** Logistic Regression is used because it achieves the best overall macro-F1 score across all five ESI levels while remaining fully transparent — a clinician can trace exactly how each vital sign influenced a prediction, which matters as much as raw accuracy in a clinical setting.

The decision is based on predictive performance, interpretability, robustness, and suitability for clinical deployment. Full reasoning, including the trade-offs against more complex models, is documented in:

- `docs/model_selection.md`
- `docs/decisions/week7_model_choice.md`
- `docs/4_model_optimisation/cost_benefit_memo.md`
- `docs/HANDOVER.md`

This recommendation may change as further modelling and evaluation are completed during the remaining weeks of the programme.

---

## Contributing

Contributions should prioritise:

- Clinical clarity
- Reproducibility
- Readability
- Well-documented code
- Transparent reporting of model decisions

---

## Licence

This project is released under the MIT Licence.
