# Week 5 Feasibility Memo - AI-Assisted ESI Triage Decision Support

**Prepared for:** Mercer General ED Board
**Prepared by:** Mya Symister · CariSurg MedTech Pathways 2026
**Date:** 4 July 2026

---

## 1 · Verdict

**Proceed to a baseline triage model caution. There should be room for iterative revision of the model in the future.**

---

## 2 · Dataset Summary

The dataset covers 55,121 emergency department encounters, each described by 225 features: 25 structured fields (demographics, arrival details, triage vital signs) and 200 chief-complaint flags. Patients range from 18 to 107 years old (mean 55.3 years); the sample includes no paediatric encounters. The age distribution and overall demographic composition of the cohort are further illustrated in Figure 2. The sample is 57.6% female, 53.4% White/Caucasian, 29.0% Black/African American, and predominantly Non-Hispanic (81.9%). Figure 3 provides a visual summary of the race and ethnicity composition represented in the dataset. Insurance status is dominated by Medicaid and Medicare (70.8% combined). Triage acuity is imbalanced, as expected for an ED population: the great majority of encounters fall in the mid-acuity range (ESI 2–3), with very few at the most urgent level (ESI 1, 0.1%) or least urgent level (ESI 5, 2.2%). Figure 1 summarises the distributions of key vital signs and demonstrates the expected imbalance in ESI categories within the cohort. Temperature is recorded in Fahrenheit throughout.

<img width="1760" height="770" alt="image" src="https://github.com/user-attachments/assets/8e7e3b4c-dacb-46b7-806f-fa8ebdcfbeca" />

*Figure 1 - Vital Sign Distributions and ESI Class Balance*

<img width="1089" height="390" alt="image" src="https://github.com/user-attachments/assets/947edfda-4d15-40cc-b8aa-4fad7c94f0e9" />
 
*Figure 2 - Distribution of Triage Acuity (ESI) and Patient Age*

<img width="1430" height="440" alt="image" src="https://github.com/user-attachments/assets/ac087fe1-a390-4c4b-a28e-c503e46958e4" />

*Figure 3 - Sample Composition by Race and Ethnicity*

---

## 3 · Top Three Quality Concerns

**1. Physiologically implausible values in a small number of vital-sign readings.** Four respiratory-rate readings and 25 glucose readings fell outside physiologically plausible bounds (0.007% and 0.045% of encounters respectively); no implausible values were found in heart rate, blood pressure, oxygen saturation, or temperature. *Mitigation:* implausible values were treated as missing, not corrected or capped, and imputed with the column median — a conservative, documented choice appropriate for a small number of affected records.

**2. A large proportion of near-constant chief-complaint flags.** 149 of the 200 chief-complaint columns (74.5%) occur in fewer than 0.5% of encounters, meaning most complaint flags individually carry little statistical signal. The concentration of presenting complaints is shown in Figure 4, which highlights that only a small number of complaint categories occur frequently enough to contribute substantial signal without further feature processing. *Mitigation:* this is noted explicitly for Week 6, where a minimum-prevalence filter or dimensionality-reduction step should be considered before modelling.

<img width="990" height="660" alt="image" src="https://github.com/user-attachments/assets/a446982e-3058-461b-a8b0-ab7d7f754623" />

*Figure 4 - 15 Most Frequent Presenting Complaints*

**3. Representativeness.** This is a single-country, US academic-hospital sample; case-mix, demographics, and insurance structures may not transfer to a Caribbean ED. *Mitigation:* named as a caveat below; external validation against local data is recommended before any deployment decision.

---

## 4 · Top Three Reasons to Proceed

**1. A complete, genuine triage label.** No encounter lacks an ESI value, and no rows needed to be dropped for a missing target — the model can learn the actual triage decision, not a proxy.

**2. Vital signs that behave as clinically expected.** Oxygen saturation shows the strongest association with acuity among the vitals (r = 0.178, in the expected direction: lower SpO2 associates with higher acuity), and several chief complaints known to be high-acuity red flags — chest pain, shortness of breath, altered mental status — show the strongest associations with acuity in the expected direction. The relationship between vital signs and ESI severity is visualised in Figure 5, while Figure 6 summarises the strength and direction of associations between individual vital-sign measures and triage acuity.

**3. A fully documented and reproducible cleaning pipeline.** Every cleaning decision — what was flagged as implausible, what was imputed, and why — is logged in the exploration notebook and can be independently audited.

---

## 5 · Caveats

* Temperature is recorded in Fahrenheit; any future work must not assume Celsius.
* The majority of chief-complaint flags are near-constant and individually low-signal; feature selection is needed before Week 6 modelling.
* Correlation values reported here are associations only, not evidence of causation or future model performance, and many chief-complaint flags are low-variance, making their correlations unstable. Figures 4 and 5 should therefore be interpreted as exploratory analyses of association patterns rather than evidence of causal relationships or confirmed predictive importance.
* The sample's demographic and insurance-payer composition reflects a single US healthcare system; external validity for a Caribbean ED population and payer structure is untested and should be treated as the primary limitation before any deployment decision.

<img width="1540" height="880" alt="image" src="https://github.com/user-attachments/assets/07ac77dd-77b7-4633-899d-1de0d8948b71" />

*Figure 5 - Vital Signs by ESI Level Box-plots*

<img width="880" height="770" alt="image" src="https://github.com/user-attachments/assets/6ec900fc-c6bb-48a2-83c2-b829033ae7a1" />

*Figure 6 - Association Between Vital Signs and Triage Acuity*

---

## Top-10 Feature Shortlist

Ranked by absolute correlation with ESI, then screened for clinical plausibility; leakage columns (`disposition`, `previousdispo`) were excluded by design. Presented as a hypothesis to test in Week 6, not proven importance.

| Rank | Feature | Correlation with ESI | Clinical justification |
| --- | --- | --- | --- |
| 1 | Oxygen saturation (SpO2) | +0.178 | A triage nurse treats low SpO2 as a danger-zone vital; this is the strongest and most clinically central association in the data. |
| 2 | Chest pain (chief complaint) | −0.164 | Classic high-acuity red flag for cardiac and pulmonary emergencies; the strongest complaint-level association found. |
| 3 | Shortness of breath (chief complaint) | −0.150 | A core ESI-2 trigger reflecting respiratory distress. |
| 4 | Suicidal ideation (chief complaint) | −0.143 | Psychiatric emergencies requiring urgent evaluation are recognised as high-acuity regardless of physiological vitals. |
| 5 | Back pain (chief complaint) | +0.142 | In the absence of red-flag features, back pain is a well-established lower-acuity presentation, consistent with its positive correlation. |
| 6 | Alcohol intoxication (chief complaint) | −0.142 | Intoxication often requires urgent monitoring for airway and safety risk. |
| 7 | Rash (chief complaint) | +0.134 | Isolated rash (without anaphylaxis features) is typically a lower-acuity presentation. |
| 8 | Altered mental status (chief complaint) | −0.132 | A classic acuity red flag spanning neurological, infectious, and metabolic causes. |
| 9 | Dental pain (chief complaint) | +0.127 | Rarely urgent; a routine, lower-resource complaint. |
| 10 | Knee pain (chief complaint) | +0.116 | A routine musculoskeletal complaint typically requiring minimal ED resources. |

*Note: patient age was not included in this ranking, as its correlation with ESI was not computed in the current notebook run. Age is a recognised clinical risk modifier and its omission here should be noted as a gap, not an assessment that it lacks predictive value.*

---

## Assumptions

* Implausible vital-sign values reflect data-entry or sensor error rather than genuine extreme physiology, given their rarity (well under 0.1% of encounters).

## Cleaning Log

Figure 7 provides an overview of missingness patterns across dataset fields and supports the documented cleaning decisions described below.

<img width="2750" height="1100" alt="image" src="https://github.com/user-attachments/assets/743815aa-fb37-4470-a2e0-09d528db16e4" />

*Figure 7 - Missing Data by Field*

| Column(s) | Rule applied | Rationale | Rows/values affected |
| --- | --- | --- | --- |
| `esi` | Drop rows with no label | Cannot learn an unrecorded decision | 0 rows |
| Vitals, `age` | Coerce to numeric | Defensive; reveal hidden dtype issues | 0 new NaNs introduced |
| `triage_vital_rr` | Out-of-range → NaN, then median-fill | 4 values outside plausible bounds (4–60/min) | 4 values |
| `triage_glucose` | Out-of-range → NaN, then median-fill | 25 values outside plausible bounds (20–800 mg/dL) | 25 values |
| Other vitals | Checked, no correction needed | 0 implausible values found | 0 values |
| `triage_vital_o2_device`, `cc_*` | Fill with 0 | Blank means "not recorded" = absent | N/A (no missingness present) |
| Demographics, admin, leakage (text) | Fill with "Unknown" | Explicit missing category, row preserved | N/A (no missingness present) |
| `esi` | Round to nearest whole number | ESI is a discrete 1–5 scale | N/A (already whole numbers) |

## Methodology

See `notebooks/week5_exploration.ipynb` for the full profiling, outlier-detection, cleaning, and correlation pipeline.
