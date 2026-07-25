# Model Selection - Audit Trail

Every model trained across Weeks 6–7, evaluated on the identical held-out
test set (N = 11,025, `random_state=42`, stratified 80/20 split). Full
reasoning behind the pinned choice lives in the
[Week 7 Cost-Benefit Memo](docs/4_model_optimisation/cost_benefit_memo.md) — this
table is the "which version gave us what" record Martina Griffith asked for.

★ = pinned final model (config.yaml → `final_model: logistic_regression`)

| Model | Key hyperparameters | Accuracy | Precision (macro) | Recall (macro) | F1 (macro) | Train time (s) | Inference (ms/pred) | ESI-1 PR AUC |
|---|---|---|---|---|---|---|---|---|
| **Logistic Regression (tuned) ★** | C=0.1, max_iter=1000, random_state=42 | **0.670** | **0.573** | **0.453** | **0.481** | **45.61** | **0.004** | **0.230** |
| Logistic Regression (baseline, Week 6) | max_iter=1000, random_state=42 | 0.671 | 0.571 | 0.452 | 0.481 | 14.36 | 0.006 | — |
| Decision Tree (tuned) | max_depth=None, min_samples_leaf=8, random_state=42, class_weight=balanced | 0.512 | 0.356 | 0.462 | 0.371 | 10.58 | 0.001 | 0.079 |
| Decision Tree (baseline, Week 6) | random_state=42, class_weight=balanced | 0.542 | 0.363 | 0.371 | 0.366 | 5.14 | 0.002 | — |
| Random Forest (fixed params) | n_estimators=200, max_depth=None, min_samples_leaf=8, class_weight=balanced | 0.608 | 0.452 | 0.519 | 0.475 | 285.61 | 0.053 | 0.104 |
| Gradient Boosting (scored on f1_macro) | max_iter=150, max_depth=6, learning_rate=0.1, class_weight=balanced | 0.550 | 0.410 | 0.547 | 0.416 | 128.90 | 0.023 | 0.189 |
| Gradient Boosting (scored on recall_macro) | max_iter=150, max_depth=6, learning_rate=0.1, class_weight=balanced | 0.550 | 0.410 | 0.547 | 0.416 | 128.48 | 0.020 | 0.189 |
| Gradient Boosting (scored on esi1_pr_auc) | max_iter=150, max_depth=4, learning_rate=0.05, class_weight=balanced | 0.530 | 0.395 | 0.558 | 0.390 | 137.49 | 0.032 | 0.216 |
| XGBoost (scored on f1_macro) | n_estimators=300, max_depth=7, learning_rate=0.05 | 0.667 | 0.588 | 0.408 | 0.443 | 209.93 | 0.056 | 0.296 |
| XGBoost (scored on recall_macro) | n_estimators=300, max_depth=7, learning_rate=0.05 | 0.667 | 0.588 | 0.408 | 0.443 | 213.22 | 0.034 | 0.296 |
| XGBoost (scored on esi1_pr_auc) | n_estimators=300, max_depth=3, learning_rate=0.05 | 0.643 | 0.612 | 0.398 | 0.443 | 214.23 | 0.018 | 0.303 |

## Why Logistic Regression

**Full clinical transparency and
the best overall macro-F1 (0.481) outweigh the small, hard-to-explain gains
of the complex models** — see the memo for the full argument, including the
honest counterpoints (ESI-1 recall of only 3/16, and XGBoost's stronger
PR-AUC for rare-class ranking).

