# Data Directory

This folder intentionally contains no data files.

## Why

The dataset used in this project (`yaleemmlc_admissionprediction_triage.csv`,
55,121 emergency department patient records) is confidential clinical data
and is excluded from version control via `.gitignore`.

## Obtaining the dataset

The dataset is not included in this repository. In the original project, it
would be obtained through the appropriate data governance process before being
placed in this directory.

For the purposes of this portfolio, the repository assumes you already have
authorised access to the dataset.

## Placing the file

Copy the dataset into this folder so the structure is:

```
carisurg-portfolio/
├── data/
│   └── yaleemmlc_admissionprediction_triage.csv
```

Alternatively, see the diagram below:

<img width="654" height="343" alt="image" src="https://github.com/user-attachments/assets/7f3cefa2-5783-4edc-ae8e-58c71736f677" />

## Running the pipeline

Once the dataset is in place, follow the instructions in the main
[`README.md`](../README.md).
