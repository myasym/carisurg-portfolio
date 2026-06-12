# CariSurg Portfolio

## Headline

Clinical triage data cleaning for emergency decision-support exploration.

## Purpose

This repository demonstrates how emergency triage data can be cleaned, analysed, and communicated in a clinically interpretable way.

## Installation

### Prerequisites

Ensure you have **Python 3.8+** installed.

### Local Setup

Clone the repository:

```bash
git clone https://github.com/myasymi/carisurg-portfolio.git
cd carisurg-portfolio
```

Install required dependencies:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn
```

### Cloud Setup (Google Colab)

You can run the notebooks directly in Google Colab without local installation.

- Upload the repository files to Google Drive, or
- Open notebooks directly from GitHub in Colab

## Usage

### Notebook Workflow

This project is structured as a 3-step clinical data pipeline:

- **`day_1_gender_cleaning.ipynb`**
  Standardises inconsistent gender coding in triage data.

- **`day_2_rr_data_cleaning.ipynb`**
  Cleans and validates respiratory rate values using clinical thresholds.

- **`day_3_data_visualisation.ipynb`**
  Visualises physiological patterns for triage interpretation.

### How to Run

To execute any notebook:

1. Open the notebook file
2. Click **Runtime → Run all** (Google Colab) or run all cells in order (Jupyter Notebook)

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
