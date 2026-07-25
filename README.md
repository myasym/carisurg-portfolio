# CariSurg Portfolio

## Overview

This repository documents my work throughout the **CariSurg MedTech Pathways Programme**, following the development of an AI-assisted Emergency Severity Index (ESI) prediction model for emergency department triage.

The project progresses from foundational clinical data cleaning and exploratory analysis through feasibility assessment, baseline model development, and model optimisation. As the programme continues, this repository will be updated with additional modelling, evaluation, and deployment work.

**Current project handover (implementation notes, data governance, known limitations, and outstanding work): see [`docs/HANDOVER.md`](docs/HANDOVER.md).**

**Complete audit trail of model development and selection: see [`docs/model_selection.md`](docs/model_selection.md).**

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
- A reproducible training pipeline
- Automated pipeline testing
- Clinical documentation and decision records

The project is still in active development and will continue to evolve over the remaining weeks of the programme.

---

## Requirements

- Python 3.10+
- Git
- pip

---

## Installation

Clone the repository:

```bash
git clone https://github.com/myasymi/carisurg-portfolio.git
cd carisurg-portfolio
```

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

---

## Data

The emergency department dataset is **not included** in this repository due to clinical governance requirements.

Place the confidential patient CSV at the location specified in:

```
config.yaml → data.raw_path
```

The dataset is excluded from version control via `.gitignore` and must never be committed.

Further guidance is available in `HANDOVER.md`.

---

## Running the Pipeline

Train the current model using:

```bash
python scripts/train.py --config config.yaml
```

Verify that the pipeline is functioning correctly:

```bash
PYTHONPATH=. pytest tests/ -v
```

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
    ├── HANDOVER.md
    └── model-selection.md
```

---

## Current Best Model

At the current stage of the programme, **Logistic Regression** has been selected as the leading model following comparative evaluation of multiple baseline and optimised algorithms.

The decision is based on predictive performance, interpretability, robustness, and suitability for clinical deployment.

Supporting documentation:

- `docs/model-selection.md`
- `docs/decisions/week7_model_choice.md`
- `docs/4_model_optimisation/cost_benefit_memo.md`
- `HANDOVER.md`

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

This project is released under the MIT License.
