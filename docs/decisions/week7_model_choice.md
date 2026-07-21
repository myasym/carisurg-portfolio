# Decision Journal: Week 7 Model Choice

**Context:**
* We needed to select a final machine learning classifier to predict patient ESI triage levels based on vital signs and engineered medical features.
* The historical dataset is heavily imbalanced (ESI 1 patients make up only 0.14% of the data), meaning standard accuracy is misleading and we must heavily weigh performance on the rarest patients.

**Alternatives considered:**
* Tuned Logistic Regression, acting as our easily explainable and linear baseline model.
* Gradient Boosting (HistGradientBoosting), tuned specifically to optimise for the ESI 1 Precision Recall Area Under the Curve and macro recall.
* XGBoost, tuned under three different scoring goals to test the absolute performance limits of complex tree models.

**Decision:** 
We will deploy the tuned Logistic Regression model because its mathematical transparency and strong overall balance outweigh the minor performance gains of the complex ensemble classifiers.

**Reasoning:**
* The Logistic Regression model achieved the highest Macro F1 score (0.481) and overall accuracy (0.670), proving it generalises better across all five ESI levels than the overfitting complex models.
* It makes a prediction in just 0.004 milliseconds, which provides zero delay when we integrate it with our current electronic health records.
* It offers complete interpretability in under a minute, allowing doctors to read direct mathematical weights rather than relying on opaque software tools like SHAP to explain a prediction.

**Things not yet known:**
* We do not yet know how the model will perform over time across different seasons, as the current data does not capture changes like wet season viral outbreaks or hurricane season trauma spikes.
* We do not yet know how nurses will react in real time when the computer model disagrees with their own human judgement on borderline triage cases.
