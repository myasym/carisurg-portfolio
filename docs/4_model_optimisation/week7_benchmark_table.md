# Model Benchmark and Interpretability Assessment

The table below evaluates both the baseline and complex classifiers across seven quantitative performance metrics and one qualitative interpretability axis.

| Model | Accuracy | Precision (Macro) | Recall (Macro) | F1 (Macro) | Train Time (s) | Inference (ms/pred) | ESI 1 PR AUC | Interpretability (Under 1 min explanation?) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Logistic Regression (tuned)** | 0.670 | 0.573 | 0.453 | 0.481 | 45.61 | 0.004 | 0.230 | **Yes**, by looking at simple maths. |
| **Decision Tree (tuned)** | 0.512 | 0.356 | 0.462 | 0.371 | 10.58 | 0.001 | 0.079 | **Yes**, by following simple yes or no steps. |
| **Random Forest (fixed)** | 0.608 | 0.452 | 0.519 | 0.475 | 285.61 | 0.053 | 0.104 | **No**, it averages hundreds of rules together. |
| **Gradient Boosting (f1_macro)** | 0.550 | 0.410 | 0.547 | 0.416 | 128.90 | 0.023 | 0.189 | **No**, it needs extra outside software. |
| **Gradient Boosting (recall_macro)** | 0.550 | 0.410 | 0.547 | 0.416 | 128.48 | 0.020 | 0.189 | **No**, it needs extra outside software. |
| **Gradient Boosting (esi1_pr_auc)** | 0.530 | 0.395 | 0.558 | 0.390 | 137.49 | 0.032 | 0.216 | **No**, it needs extra outside software. |
| **XGBoost (f1_macro)** | 0.667 | 0.588 | 0.408 | 0.443 | 209.93 | 0.056 | 0.296 | **No**, it needs extra outside software. |
| **XGBoost (recall_macro)** | 0.667 | 0.588 | 0.408 | 0.443 | 213.22 | 0.034 | 0.296 | **No**, it needs extra outside software. |
| **XGBoost (esi1_pr_auc)** | 0.643 | 0.612 | 0.398 | 0.443 | 214.23 | 0.018 | 0.303 | **No**, it needs extra outside software. |
