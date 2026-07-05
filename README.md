# CariSurg Portfolio

## Headline

Clinical triage data cleaning and feasibility assessment for emergency decision-support modelling.

## Purpose

This repository demonstrates how emergency triage data can be cleaned, analysed, and communicated in a clinically interpretable way, building toward an AI-assisted Emergency Severity Index (ESI) triage model.

## Installation

### Prerequisites

Ensure you have **Python 3.8+** installed.

### Local Setup

Clone the repository:

```bash
git clone [https://github.com/myasymi/carisurg-portfolio.git](https://github.com/myasymi/carisurg-portfolio.git)
cd carisurg-portfolio

```

Install required dependencies:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn missingno

```

### Cloud Setup (Google Colab)

You can run the notebooks directly in Google Colab without local installation.

* Upload the repository files to Google Drive, or
* Open notebooks directly from GitHub in Colab

---

## Usage

### Repository Structure & Workflow

This project is structured as a progressing clinical data pipeline, moving from foundational cleaning to predictive feasibility.

#### Phase 1: Foundational Data Skills (Week 0)

* **`day_1_gender_cleaning.ipynb`**
Standardises inconsistent gender coding in triage data.
* **`day_2_rr_data_cleaning.ipynb`**
Cleans and validates respiratory rate values using clinical thresholds.
* **`day_3_data_visualisation.ipynb`**
Visualises physiological patterns for triage interpretation.

#### Phase 2: Data Exploration & Feasibility (Week 5)

Assesses whether the Yale EMMLC triage extract (`yaleemmlc_admissionprediction_triage.csv`, 55,121 encounters, 225 features) is a viable basis for a baseline ESI triage model.

* **`notebooks/week5_exploration.ipynb`**
Full profiling, outlier detection, distribution analysis, cleaning pipeline, and correlation analysis against the triage target (`esi`).
* **`docs/week5-feasibility-final.md`**
Feasibility memo for the ED Board, including the top-10 feature shortlist and cleaning log.
* **`docs/figs/`**
Data-quality dashboard figures (missingness, ESI/age distribution, demographics, chief complaints, vitals-by-ESI, correlation heatmap).
* **`triage_cleaned_v1.csv`**
Cleaned dataset generated from the pipeline.

**⚠️ Data Governance Note:** The raw and cleaned datasets are excluded from version control via `.gitignore` due to file size and the strict sensitivity of clinical data, even though this extract is de-identified.

### How to Run

To execute any notebook:

1. Place the required raw dataset in your working directory (if running locally) or mount it via Google Drive (if running on Colab).
2. Open the notebook file.
3. Click **Runtime → Run all** (Google Colab) or run all cells in order (Jupyter Notebook).

---

## Contributing

Contributions should focus on clinical clarity, reproducible analysis, and readability for non-technical healthcare audiences.

1. Fork the repository
2. Create a feature branch:
```bash
git checkout -b feature/AmazingFeature

```


3. Commit changes:
```bash
git commit -m "Add some AmazingFeature"

```


4. Push to the branch:
```bash
git push origin feature/AmazingFeature

```


5. Open a Pull Request

## Licence

This project is released under the MIT License. You are free to use, modify, and distribute this work for educational and non-commercial purposes, provided attribution is maintained.

```

```
