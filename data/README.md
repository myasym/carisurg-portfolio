# Data Folder

## About Dataset

The dataset (`EmergencyTriageDataset_Reduced_Dirty.csv`) contains anonymised emergency department triage observations used for Week 0 clinical data cleaning and exploratory analysis.

It includes patient-level demographic and physiological measurements recorded at the point of emergency admission. These variables represent routine triage indicators used to assess patient acuity, including cardiovascular, respiratory, and neurological status.

The dataset is intentionally “dirty” (e.g. inconsistent categorical encoding, missing values, and physiologically implausible entries) to support data cleaning, validation, and preprocessing exercises.

---

## Description of the Data

The dataset is stored as a single CSV file in this directory:

```

data/
└── EmergencyTriageDataset_Reduced_Dirty.csv

```

Each row represents a single patient triage record. Each column represents a clinical measurement or demographic attribute collected at admission.

---

### Key Columns (Clinical Meaning)

- `ID` - Unique patient identifier (non-clinical reference key)  
- `Age` - Patient age in years (demographic variable)  
- `Gender` - Categorical sex/gender entry (contains inconsistent encoding requiring standardisation)  
- `GCS` - Glasgow Coma Scale (neurological status; range typically 3–15)  
- `SBP` - Systolic blood pressure (mmHg; cardiovascular function)  
- `DBP` - Diastolic blood pressure (mmHg)  
- `MAP` - Mean arterial pressure (mmHg; perfusion indicator)  
- `pulse` - Heart rate (beats per minute; circulatory status)  
- `Temp` - Body temperature (may include inconsistent formats or units)  
- `RR` - Respiratory rate (breaths per minute; respiratory status indicator)  
- `Fio2` - Fraction of inspired oxygen (%) used in oxygen therapy context  

---

## File Format

- `.csv` (comma-separated values)
- Structured tabular format:
  - Rows = individual patients
  - Columns = clinical or demographic variables
 
(No images or audio files included.)

---

## Notes

- This dataset is used strictly for educational purposes in clinical data preprocessing and exploratory analysis.
- It is designed to demonstrate real-world data quality issues commonly encountered in emergency medicine datasets (e.g. inconsistent encoding, missingness, and outliers).
- All data is anonymised and contains no patient-identifiable information.
```
