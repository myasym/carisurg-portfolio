## Six-axis benchmark

The table below compares all four models on accuracy, macro precision, macro recall, macro F1, training time, and inference time per prediction. This is the quantitative basis for the cost-benefit memo.

| Model                          |   Accuracy |   Precision (macro) |   Recall (macro) |   F1 (macro) |   Train time (s) |   Inference (ms/pred) |
|:-------------------------------|-----------:|--------------------:|-----------------:|-------------:|-----------------:|----------------------:|
| Logistic Regression (baseline) |      0.671 |               0.571 |            0.452 |        0.481 |            14.36 |                 0.006 |
| Decision Tree (baseline)       |      0.542 |               0.363 |            0.371 |        0.366 |             5.14 |                 0.002 |
| Random Forest (tuned)          |      0.608 |               0.452 |            0.519 |        0.475 |          1724.88 |                 0.06  |
| Gradient Boosting              |      0.55  |               0.41  |            0.547 |        0.416 |            12.79 |                 0.019 |
