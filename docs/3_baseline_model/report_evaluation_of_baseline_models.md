## Evaluation of Baseline Triage Models

**Context:** This report outlines the development and evaluation of baseline predictive models for the Mercer General Emergency Department. The objective is to predict a patient's Emergency Severity Index (ESI), a five-level triage scale where level 1 represents the most urgent, critical cases. 

## Metric Justification
When evaluating model performance for clinical triage, we must carefully select how we measure success. Relying solely on **accuracy**, the overall percentage of patients classified correctly, can be dangerously misleading in this context. 

The triage dataset is highly imbalanced, as visualised in Figure 1. ESI-3 patients make up 49% of the volume, whereas critical ESI-1 patients constitute only 0.1%. 

<img width="690" height="390" alt="image" src="https://github.com/user-attachments/assets/d6beec4c-5420-4880-afd3-2d99b6d3ce7c" />

**Figure 1: ESI Class Distribution (Log Scale).** This logarithmic bar chart demonstrates the extreme class imbalance in the triage dataset, highlighting how common ESI-3 cases heavily outnumber rare ESI-1 cases.

Because of this disparity, a model could achieve a reasonably high accuracy score by entirely ignoring ESI-1 patients and only predicting the common classes correctly. 

To safely evaluate these models, our primary metric is **recall**. Recall measures the model's ability to find all the patients who genuinely belong to a specific category. In an emergency setting, missing a critical ESI-1 patient carries a far higher clinical cost than triggering a false alarm. Therefore, demonstrating high ESI-1 recall is essential before any model can be considered for operational use.

## Model Results
We evaluated two standard classification models, Logistic Regression and a Decision Tree, against a **stratified random baseline**. The baseline acts as a 'dummy' model that guesses ESI levels entirely at random, matching the natural proportions of the dataset; real models must clear this hurdle to prove they add any value. 

Additionally, we tested both models in their default state and with **class weighting** applied. Class weighting is a technique that forces the model to treat errors on rare groups (like ESI-1) as more severe during its learning phase, theoretically preventing it from ignoring minority classes. Table 1 and Figure 2 outline the baseline performance results.

*Note: Technical metrics are provided below. **Precision** refers to the proportion of the model's positive predictions that were actually correct.*

**Table 1: Performance Summary of Baseline Triage Models**
| Model Configuration | Overall Accuracy | ESI-1 Recall | ESI-1 Precision |
| :--- | :--- | :--- | :--- |
| **Stratified Random Baseline** | 37.74% | N/A | N/A |
| **Logistic Regression (Default)** | 68.10% | 0.000 | 0.000 |
| **Decision Tree (Default)** | 55.36% | 0.000 | 0.000 |
| **Logistic Regression (Weighted)** | 58.70% | 0.273 | 0.008 |
| **Decision Tree (Weighted)** | 36.60% | 0.091 | 0.003 |

<img width="1086" height="490" alt="image" src="https://github.com/user-attachments/assets/dcf7bef3-fdd8-4e02-9170-00c28437385c" />

**Figure 2: Confusion Matrices for Default Baseline Models.** These matrices illustrate the exact breakdown of correct and incorrect predictions for the default Logistic Regression and Decision Tree models across all five ESI levels.

## Failure Mode Reflection
Neither baseline model, in default or weighted configurations, meets the standard required for clinical deployment. Our analysis highlights three critical failure modes:

*   **The Rare Class Trade-off:** The default models completely failed to identify any ESI-1 patients (recall of 0.000). Applying class weighting successfully forced the models to capture some ESI-1 cases, but this came at a severe cost. Overall accuracy dropped drastically, and precision plummeted. For example, the weighted decision tree experienced such a severe performance penalty that it frequently abandoned predicting majority classes altogether, as demonstrated in Figure 3 and Figure 4. 

<img width="1086" height="490" alt="image" src="https://github.com/user-attachments/assets/81769658-b7a9-4760-848e-8075fbd05711" />

**Figure 3: Normalised Confusion Matrices for Class-Weighted Models.** This visual demonstrates the trade-off effect, showing how forcing the models to find ESI-1 patients caused them to severely misclassify the majority classes.

<img width="790" height="490" alt="image" src="https://github.com/user-attachments/assets/733904b8-bd2d-421a-901e-9650645ef520" />

**Figure 4: Per Class Metrics (Decision Tree, Weighted).** This chart details the precision, recall and F1 scores (a combined metric of precision and recall) for the weighted Decision Tree, further emphasising the poor performance across majority categories when ESI-1 is prioritised.

*   **Mathematical Instability:** Critical decisions must be reliable, but our rare class predictions were not. When testing the weighted decision tree with a different random seed (a computational starting point), ESI-1 recall swung violently from 0.091 to 0.364. Because there are so few true ESI-1 patients in any given test sample, the model's performance on this group is highly unstable and cannot be trusted as a fixed, reliable capability.

*   **Misalignment with Clinical Reality:** From a practical standpoint, ESI-1 patients usually present with obvious physiological signs that clinical staff readily recognise without the need for algorithmic decision support. As illustrated in Figure 5, the model heavily relied on these exact obvious indicators to make its predictions. 

<img width="691" height="490" alt="image" src="https://github.com/user-attachments/assets/cdaf332b-20c9-4011-96a5-26382b781eeb" />

**Figure 5: Top 15 Feature Importances (Weighted Decision Tree).** This chart displays the most influential patient data points used by the model, showing a heavy reliance on clear clinical signals like stroke alerts and ambulance arrival modes.

The bulk of the department's patient volume, and the area where triage judgement is most frequently contested, falls within the ESI-2 to ESI-4 range. By contorting the models to prioritise the ultra-rare ESI-1 cases, we actively sacrificed their ability to discriminate accurately across the ESI-2 to ESI-4 categories, thereby destroying the models' primary avenue for adding operational value.
