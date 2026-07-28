# Data Directory

This directory intentionally contains no data files.

## Rationale

The dataset underpinning this project (`yaleemmlc_admissionprediction_triage.csv`,
comprising 55,121 emergency department patient records) constitutes confidential
clinical data and is therefore excluded from version control via `.gitignore`.
It must never be committed to this repository, including in de-identified or
reduced form.

## Data Provenance and Access

The dataset resides in a governed storage location (Google Drive, access-
controlled) and is not distributed alongside this repository. Access requires
clearance through Mercer General IT Governance — contact Martina Griffith
(Clinical IT Lead) to initiate this process.

## Running the Pipeline

Prior to executing `scripts/train.py`, place the dataset at the path specified
under `config.yaml → data.raw_path`. Full instructions are documented in
`docs/HANDOVER.md`.
