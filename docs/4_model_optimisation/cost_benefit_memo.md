# Cost Benefit Analysis and Model Recommendation for Triage Prediction

**TO:** Executive Board, Clinical Leadership, and IT Governance

**FROM:** Mya Symister, Data Science Lead

**LOCATION:** Mercer General Hospital Emergency Department

**DATE:** 21 July 2026

**SUBJECT:** Final Assessment and Deployment Recommendation for the Emergency Severity Index (ESI) Triage Classifier

---

## 1. Executive Verdict

**VERDICT:** Mercer General Hospital should use the Logistic Regression model for the Emergency Department triage workflow. It is completely transparent and very fast. It also has a better overall Macro F1 score (0.481). These benefits are more important than the small and hard to explain improvements offered by more complex models.

---

## 2. Dataset and Methods Recap

This project tested a computer model for triage using private records from 55,121 patient visits to the Mercer General Hospital Emergency Department. The main goal is to predict the Emergency Severity Index (ESI). This is a five level triage scale from ESI 1 (Immediate Life Support) down to ESI 5 (Non Urgent Care). The old data shows a very uneven spread of patient severity:

* **ESI 1 (Most Urgent):** 77 patients (0.14% of dataset)
* **ESI 2 (Emergent):** 17,924 patients (32.52%)
* **ESI 3 (Urgent):** 27,010 patients (49.00%)
* **ESI 4 (Less Urgent):** 8,896 patients (16.14%)
* **ESI 5 (Non Urgent):** 1,214 patients (2.20%)

**Data Cleaning:** We applied standard cleaning steps to all records. We changed vital signs to numbers. We marked impossible medical readings as missing (for example, a body temperature below 90°F or above 110°F, or oxygen levels over 100%). We filled missing values with the middle value of that column. We left out administrative details and protected personal features (like age, gender, race, ethnicity, and insurance status) to prevent unfair bias. We also removed events that happened after triage (like bed assignment) so the model did not cheat.

**Feature Building:** Blood pressure is often missing or delayed during quick triage. To fix this, we created seven new medical features. These include Shock Index (Heart Rate divided by Systolic BP), Pulse Pressure (Systolic BP minus Diastolic BP), and an oxygen to breathing rate ratio. We also added simple yes or no markers for fast breathing, low oxygen, and fever, along with a total Red Flag Count. The final dataset used 215 features.

**Test Setup:** We split the dataset into an 80% training set (44,096 patients with 61 ESI 1 cases) and a 20% test set (11,025 patients with 16 ESI 1 cases). We used the same random seed (random_state = 42) to ensure fair comparisons with past tests. We tested several models (Logistic Regression, Decision Trees, Random Forests, Gradient Boosting, and XGBoost). We tuned these models using three different scoring goals: Macro F1, Macro Recall, and ESI 1 PR AUC.

---

## 3. Performance Parameters Explanation and Benchmark Table

Evaluating medical machine learning models means balancing clinical risk with real life hospital operations. To make this clear for hospital directors, clinical chiefs, and IT staff, we have defined the scoring metrics below:

### Explanation of Performance Parameters

* **Accuracy:** The total percentage of correct triage predictions. This can be misleading in our uneven data. A simple model predicting only ESI 2 and ESI 3 would get about 81% accuracy, but it would completely miss dying (ESI 1) patients.
* **Precision (Macro):** Out of all the patients the model placed in a specific ESI level, how many truly belonged there? High precision stops nursing staff from getting false alarm fatigue. Macro precision averages the score across all 5 classes equally.
* **Recall (Macro):** Out of all the patients who truly belonged to a specific ESI level, how many did the model find? In an emergency, finding the most urgent patients is vital to prevent severe harm. Macro recall averages the score across all five levels equally.
* **F1 Score (Macro):** This is a combined score of precision and recall, averaged across all five classes. It is the best overall metric because it punishes models that guess one class too often or too rarely.
* **Training Time (seconds):** The time it takes a computer to teach the model using the 44,096 past patient records. This matters for how quickly we can update the model in the future.
* **Inference Time (ms / prediction):** The time it takes the model to guess the ESI level for one new patient. This must be under 100 milliseconds to work smoothly in the computer system.
* **ESI 1 PR AUC (Precision Recall Area Under Curve):** A special score showing how well the model finds the rarest and most critical ESI 1 patients. It looks at all probability levels and is not tricked by the high number of less urgent patients.
* **Interpretability (Under 1 min explanation):** A rating of whether a doctor or nurse can understand the exact medical reason behind a prediction in under 60 seconds without extra software.

### Benchmark Table

**Table 1: Six Axis Quantitative Benchmark and Qualitative Interpretability Assessment** (Evaluated on out of sample test set, N = 11,025)

| Candidate Model | Accuracy | Precision (Macro) | Recall (Macro) | F1 Score (Macro) | Train Time (s) | Inference (ms/pred) | ESI 1 PR AUC | Explainable Under 1 Minute? |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Logistic Regression (tuned) ★** | **0.670** | **0.573** | **0.453** | **0.481** | **45.61** | **0.004** | **0.230** | **YES (Mathematical Weights)** |
| **Decision Tree (tuned)** | 0.512 | 0.356 | 0.462 | 0.371 | 10.58 | 0.001 | 0.079 | **YES (Decision Pathways)** |
| **Random Forest (fixed params)** | 0.608 | 0.452 | 0.519 | 0.475 | 285.61 | 0.053 | 0.104 | **NO (Tree Averaging)** |
| **Gradient Boosting (f1_macro)** | 0.550 | 0.410 | 0.547 | 0.416 | 128.90 | 0.023 | 0.189 | **NO (Requires SHAP)** |
| **Gradient Boosting (recall_macro)** | 0.550 | 0.410 | 0.547 | 0.416 | 128.48 | 0.020 | 0.189 | **NO (Requires SHAP)** |
| **Gradient Boosting (esi1_pr_auc)** | 0.530 | 0.395 | 0.558 | 0.390 | 137.49 | 0.032 | 0.216 | **NO (Requires SHAP)** |
| **XGBoost (f1_macro)** | 0.667 | 0.588 | 0.408 | 0.443 | 209.93 | 0.056 | 0.296 | **NO (Requires SHAP)** |
| **XGBoost (recall_macro)** | 0.667 | 0.588 | 0.408 | 0.443 | 213.22 | 0.034 | 0.296 | **NO (Requires SHAP)** |
| **XGBoost (esi1_pr_auc)** | 0.643 | 0.612 | 0.398 | 0.443 | 214.23 | 0.018 | 0.303 | **NO (Requires SHAP)** |

---

## 4. Arguments for the Recommended Choice

### 1. Total Clinical Transparency and Instant Medical Auditability

The Logistic Regression model is easy to understand. It uses simple maths to make decisions. A triage nurse or doctor can see exactly how much each patient detail changes the final score. If the model gives an unexpected ESI rating, a doctor can check the maths in under 30 seconds to see why (for example, verifying that a high Shock Index increased the risk score). Other complex models act like black boxes and need extra software to explain them.

### 2. Superior Overall Balance

We expected complex models to perform best. However, the Logistic Regression model got the highest overall Macro F1 score (0.481) and highest total accuracy (0.670). Complex models learned too many specific details from the training data and did not generalise well. Logistic Regression gives the most reliable balance across all five ESI levels without causing too many false alarms for less urgent patients.

### 3. Minimal IT Overhead

From an IT view, Logistic Regression is very light. It makes a prediction in just 0.004 milliseconds per patient. This is more than 10 times faster than Random Forest or XGBoost. The maths can be built directly into the hospital's current computer system. It does not need special computer hardware and trains in just 45 seconds. This makes future updates cheap and easy.

---

## 5. Arguments Against the Recommended Choice

1. Lower High Acuity Sensitivity (ESI 1 Case Misses)
The main medical problem with Logistic Regression is that it misses the most urgent patients. Out of 16 true ESI 1 patients in the test data, the model only found 3. It incorrectly labelled 13 critical cases as less urgent. Figure 1 visually highlights this weakness by comparing the missed ESI 1 cases between our recommended model and the alternatives. In a busy emergency department, missing an ESI 1 patient can be fatal.

<img width="1404" height="1339" alt="image" src="https://github.com/user-attachments/assets/6cdfeaac-e2b7-4be6-8f75-bca2a9b969f9" />

Figure 1 - Confusion matrices highlighting the true positive and false negative rates specifically for ESI 1 cases across the Logistic Regression and Gradient Boosting models.

### 2. Inability to Learn Complex Medical Interactions

Logistic Regression models can only add features together in straight lines. In real emergencies, patient health changes in complex ways. For example, a high heart rate combined with low oxygen is much more dangerous for an elderly patient than a young athlete. Complex models map these interactions naturally. Logistic Regression can only do this if doctors manually programme every single combination.

### 3. Suboptimal Precision Recall Area Under Curve

The XGBoost model had a much better ESI 1 PR AUC score (0.303 compared to 0.230 for Logistic Regression). This score measures the quality of the model's rankings for rare events. If hospital leaders want to lower the warning threshold to catch more ESI 1 patients, XGBoost would provide a better mathematical curve. It would catch more true critical cases with fewer false alarms than Logistic Regression.

---

## 6. Operational Risks and Unknowns

* **Risk 1: Automation Bias and Clinical De-skilling:** Using a computer tool creates two risks. Triage nurses might trust the computer too much and ignore physical signs that the vital monitors miss. Alternatively, they might experience alert fatigue if the model is often wrong. We must have strict rules that the computer score is only a helpful second opinion.
* **Risk 2: High Sampling Variance:** ESI 1 cases make up only 0.14% of the past data. This leaves us with just 16 test cases. Small random changes in these test cases cause huge shifts in the scores. If the model gets just two more patients right, the recall jumps by 12.5%. We cannot be totally sure how any model will handle major spikes in trauma cases.
* **Risk 3: Sensor Issues and Missing Data:** The model's special features (like Shock Index) rely on perfect vital sign data. If medical equipment fails or staff are too busy to enter data properly, the computer will guess the missing numbers. This can distort patient risk scores and lead to dangerous triage choices.

---

## 7. Final Recommendation and Operational Boundaries

### Final Recommendation

Mercer General Hospital should deploy the Logistic Regression Model as a real time support tool in the Emergency Department triage system. It is very fast, highly accurate overall, needs no extra software, and is 100% transparent. This makes it the safest choice for hospital management and IT.

### Explicit Acknowledgement of What This Choice Does NOT Solve

Hospital leaders must understand that this tool does not solve the lack of past data for ESI 1 patients. Because we only have 77 total ESI 1 cases in the records, no computer model can act as a standalone safety net for dying patients. The model **must never be permitted to automatically override human nurse decisions**. It is designed only as a silent safety check. It should prompt doctors to look again if the computer disagrees with their human judgement.
