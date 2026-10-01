# FloodGuard-X Research Notes

## Project Research Overview

FloodGuard-X is a lightweight and explainable flood-risk detection and disaster-management system.

The project investigates whether environmental variables can be combined into a simple Flood Risk Index (FRI) and evaluated using controlled synthetic scenarios without relying on an external historical dataset.

The current research focuses on:

* Flood Risk Index design
* Explainable risk classification
* Sensitivity analysis
* Alternative weighting schemes
* Threshold stability
* Rule-based anomaly detection

---

# Experiment 1: Flood Risk Index Evaluation

## Objective

To evaluate whether a weighted Flood Risk Index (FRI) can classify different environmental flood scenarios using synthetic data without relying on an external dataset.

## Environmental Variables

The model uses four environmental variables:

1. Rainfall
2. Water Level
3. Soil Moisture
4. Temperature

Temperature is currently recorded as contextual information and is not included in the FRI calculation.

## Flood Risk Index

The Flood Risk Index is calculated using:

**FRI = 0.40R + 0.40W + 0.20S**

Where:

* R = normalized rainfall score
* W = normalized water-level score
* S = soil-moisture score

## Normalization

### Rainfall

Rainfall is normalized using a maximum reference value of 150 mm.

**R = (Rainfall / 150) × 100**

Values above 150 mm are capped at 100.

### Water Level

Water level is normalized using a maximum reference value of 5 metres.

**W = (Water Level / 5) × 100**

Values above 5 metres are capped at 100.

### Soil Moisture

Soil moisture is represented as a percentage from 0 to 100.

## Risk Classification

| FRI Range | Risk Level |
| --------- | ---------- |
| 0–39.9    | LOW        |
| 40–69.9   | MEDIUM     |
| 70–100    | HIGH       |

## Dataset

The project uses a synthetic dataset created specifically for controlled experimentation.

The dataset contains environmental scenarios representing different combinations of rainfall, water level, soil moisture, and temperature.

No external dataset is used in this experiment.

## Model Evaluation Results

The evaluation used 10 synthetic scenarios.

| Metric                     | Result |
| -------------------------- | ------ |
| Total scenarios            | 10     |
| Average FRI                | 60.10  |
| Minimum FRI                | 22.93  |
| Maximum FRI                | 100.00 |
| LOW risk scenarios         | 3      |
| MEDIUM risk scenarios      | 3      |
| HIGH risk scenarios        | 4      |
| Classification consistency | PASSED |

The classification consistency check confirmed that all calculated risk classifications matched the predefined FRI thresholds.

## Finding

The initial experiment demonstrates that the proposed FRI can consistently apply its predefined classification rules to the synthetic scenarios.

## Limitation

The experiment does not establish real-world flood prediction accuracy because the scenarios are synthetic and the normalization limits, weights, and thresholds are predefined model assumptions.

---

# Experiment 2: Sensitivity Analysis

## Objective

To investigate how changes in individual environmental variables affect the Flood Risk Index while the other variables remain fixed.

## Baseline Conditions

* Rainfall = 60 mm
* Water Level = 2.0 m
* Soil Moisture = 60%

## Rainfall Sensitivity

| Rainfall (mm) |   FRI |
| ------------- | ----: |
| 0             | 28.00 |
| 30            | 36.00 |
| 60            | 44.00 |
| 90            | 52.00 |
| 120           | 60.00 |
| 150           | 68.00 |

## Water Level Sensitivity

| Water Level (m) |   FRI |
| --------------- | ----: |
| 0               | 28.00 |
| 1               | 36.00 |
| 2               | 44.00 |
| 3               | 52.00 |
| 4               | 60.00 |
| 5               | 68.00 |

## Soil Moisture Sensitivity

| Soil Moisture (%) |   FRI |
| ----------------- | ----: |
| 0                 | 32.00 |
| 20                | 36.00 |
| 40                | 40.00 |
| 60                | 44.00 |
| 80                | 48.00 |
| 100               | 52.00 |

## Finding

Under the tested baseline conditions, rainfall and water level produced equal FRI changes across their tested ranges, while soil moisture produced a smaller FRI change.

This behavior is consistent with the current weighting scheme:

* Rainfall = 40%
* Water Level = 40%
* Soil Moisture = 20%

Therefore, the experiment demonstrates the sensitivity of the model to its input variables and weighting structure.

## Limitation

This result describes the behavior of the proposed mathematical model. It does not establish that rainfall and water level have equal importance in real-world flood prediction.

---

# Experiment 3: Alternative Weighting Analysis

## Objective

To investigate how changing the relative weights of rainfall and water level affects the Flood Risk Index and risk classification.

## Models Tested

### Model A

* Rainfall = 40%
* Water Level = 40%
* Soil Moisture = 20%

### Model B

* Rainfall = 50%
* Water Level = 30%
* Soil Moisture = 20%

### Model C

* Rainfall = 30%
* Water Level = 50%
* Soil Moisture = 20%

## Results

| Scenario      | Model A      | Model B      | Model C      |
| ------------- | ------------ | ------------ | ------------ |
| Normal        | 22.93 LOW    | 21.87 LOW    | 24.00 LOW    |
| Heavy Rain    | 61.93 MEDIUM | 64.87 MEDIUM | 59.00 MEDIUM |
| Rising Water  | 63.67 MEDIUM | 61.33 MEDIUM | 66.00 MEDIUM |
| Extreme Flood | 92.33 HIGH   | 92.67 HIGH   | 92.00 HIGH   |

## Finding

Changing the relative weights of rainfall and water level produced different numerical FRI values.

However, all four tested scenarios retained the same risk classification across the three weighting schemes:

* Normal → LOW
* Heavy Rain → MEDIUM
* Rising Water → MEDIUM
* Extreme Flood → HIGH

The results therefore demonstrate classification stability across the tested weighting configurations.

## Limitation

The experiment does not establish which weighting scheme is more accurate for real-world flood prediction. Such a conclusion would require appropriate real-world observations or another validated reference standard.

---

# Experiment 4: Threshold Stability Analysis

## Objective

To examine how the model behaves around the two Flood Risk Index classification boundaries.

## Classification Thresholds

* FRI below 40 → LOW
* FRI from 40 to below 70 → MEDIUM
* FRI 70 or above → HIGH

## Tested Values

|  FRI | Risk Level |
| ---: | ---------- |
| 39.8 | LOW        |
| 39.9 | LOW        |
| 40.0 | MEDIUM     |
| 40.1 | MEDIUM     |
| 40.2 | MEDIUM     |
| 69.8 | MEDIUM     |
| 69.9 | MEDIUM     |
| 70.0 | HIGH       |
| 70.1 | HIGH       |
| 70.2 | HIGH       |

## Boundary Check

### LOW → MEDIUM

* FRI 39.9 → LOW
* FRI 40.0 → MEDIUM
* FRI 40.1 → MEDIUM

### MEDIUM → HIGH

* FRI 69.9 → MEDIUM
* FRI 70.0 → HIGH
* FRI 70.1 → HIGH

## Finding

The model consistently applies the predefined classification thresholds.

A change of 0.1 FRI around either boundary is sufficient to move the classification into the adjacent risk category.

This demonstrates that the classification logic behaves deterministically at the defined boundaries.

## Limitation

The thresholds are predefined model assumptions and have not been validated against real-world flood observations.

---

# Experiment 5: Anomaly Detection Analysis

## Objective

To evaluate whether the rule-based anomaly detection component can identify unusual environmental conditions and combinations of severe conditions.

## Anomaly Detection Rules

The current anomaly mechanism assigns scores based on environmental conditions.

### Rainfall

* Rainfall ≥ 120 mm → +40
* Rainfall ≥ 90 mm → +20

### Water Level

* Water Level ≥ 4 m → +40
* Water Level ≥ 3 m → +20

### Soil Moisture

* Soil Moisture ≥ 90% → +20

An anomaly is reported when the total anomaly score reaches **40 or higher**.

## Results

| Scenario              | Anomaly Score | Result           |
| --------------------- | ------------: | ---------------- |
| Normal Conditions     |             0 | NORMAL           |
| High Rainfall         |            20 | NORMAL           |
| Extreme Rainfall      |            40 | ANOMALY DETECTED |
| Critical Water Level  |            40 | ANOMALY DETECTED |
| Extreme Soil Moisture |            20 | NORMAL           |
| Multiple Anomalies    |           100 | ANOMALY DETECTED |

## Detected Conditions

### Normal Conditions

No unusual environmental condition was detected.

### High Rainfall

Unusually high rainfall was detected, but the total anomaly score remained below the anomaly threshold.

### Extreme Rainfall

Extremely high rainfall produced an anomaly score of 40, triggering anomaly detection.

### Critical Water Level

Critical water level produced an anomaly score of 40, triggering anomaly detection.

### Extreme Soil Moisture

Extremely high soil moisture produced a score of 20 and did not independently trigger the anomaly state.

### Multiple Anomalies

Extreme rainfall, critical water level, and extremely high soil moisture occurred together.

The combined anomaly score reached 100, resulting in anomaly detection.

## Finding

The anomaly detection mechanism identifies an anomaly when the combined anomaly score reaches 40 or above.

Individual moderate unusual conditions did not trigger the final anomaly state, while severe conditions and combinations of severe conditions triggered detection.

The system also provides an explanation of the detected environmental conditions, making the anomaly result interpretable.

## Limitation

The anomaly thresholds and scores are manually defined rules. The experiment demonstrates the behavior of the proposed system but does not establish real-world anomaly-detection accuracy.

---

# Overall Research Findings

The five experiments provide an initial evaluation of the FloodGuard-X model.

The experiments demonstrate that:

1. The FRI calculation consistently applies the predefined mathematical model.
2. Rainfall and water level have greater influence on FRI than soil moisture under the current weighting scheme.
3. Alternative rainfall and water-level weights change numerical FRI values while the tested scenarios retain their original risk categories.
4. The LOW/MEDIUM and MEDIUM/HIGH classification boundaries operate consistently.
5. The rule-based anomaly mechanism can identify severe or combined unusual environmental conditions.
6. The system provides interpretable explanations for both risk and anomaly results.

---

# Overall Limitations

The current research has several important limitations:

* The dataset is synthetic rather than historical.
* The model weights are manually selected.
* The normalization limits are predefined assumptions.
* The FRI thresholds are manually defined.
* The anomaly thresholds are rule-based.
* No real-world flood observations are currently used for validation.
* The experiments are controlled rather than representative of all real-world flood conditions.
* Temperature is currently recorded but not included in the FRI calculation.

Therefore, the current results demonstrate the behavior, consistency, sensitivity, and interpretability of the proposed model rather than proving real-world predictive accuracy.

---

# Future Research

Future experiments can investigate:

* More extensive synthetic scenario generation
* Variable interaction effects
* Additional weighting schemes
* Threshold optimization
* More detailed anomaly detection
* Statistical analysis
* Machine-learning model comparison
* Explainable machine-learning methods
* Validation against an appropriate real-world dataset if one becomes available
* Comparison of model outputs with established flood-risk indicators

---

# Current Research Question

The current research can be framed around:

**How does the weighting of environmental variables affect the sensitivity and stability of a lightweight, explainable, dataset-free flood-risk model?**

A broader supporting question is:

**How effectively can a lightweight, explainable flood-risk model estimate changing flood risk using controlled synthetic environmental conditions without relying on historical datasets?**
# Experiment 6: Variable Influence Analysis

## Objective

To measure the relative contribution of rainfall, water level, and soil moisture to the final Flood Risk Index (FRI) under selected synthetic flood scenarios.

This experiment helps investigate which variables have the greatest influence on the model output under the current weighting and normalization structure.

## Method

The experiment uses four representative synthetic scenarios:

1. Normal Conditions
2. Heavy Rainfall
3. Rising Water Level
4. Extreme Flood

For each scenario, the individual contribution of each variable to the final FRI is calculated.

The current model uses:

* Rainfall weight = 40%
* Water Level weight = 40%
* Soil Moisture weight = 20%

## Scenario Results

### Normal Conditions

* Rainfall Contribution = 5.33
* Water Level Contribution = 9.60
* Soil Moisture Contribution = 8.00
* Total FRI = 22.93

### Heavy Rainfall

* Rainfall Contribution = 29.33
* Water Level Contribution = 17.60
* Soil Moisture Contribution = 15.00
* Total FRI = 61.93

### Rising Water Level

* Rainfall Contribution = 18.67
* Water Level Contribution = 28.00
* Soil Moisture Contribution = 17.00
* Total FRI = 63.67

### Extreme Flood

* Rainfall Contribution = 37.33
* Water Level Contribution = 36.00
* Soil Moisture Contribution = 19.00
* Total FRI = 92.33

## Average Variable Contribution

Across the four tested scenarios:

| Variable      | Average Contribution |
| ------------- | -------------------: |
| Rainfall      |                22.67 |
| Water Level   |                22.80 |
| Soil Moisture |                14.75 |

## Relative Contribution

The average contributions were converted into relative percentages.

| Variable      | Relative Contribution |
| ------------- | --------------------: |
| Rainfall      |                37.64% |
| Water Level   |                37.86% |
| Soil Moisture |                24.49% |

## Finding

The results show that rainfall and water level produced very similar average contributions to the FRI across the tested scenarios.

Rainfall contributed approximately 37.64% of the combined average contribution, while water level contributed approximately 37.86%.

Soil moisture contributed approximately 24.49%.

The results are consistent with the current model structure, where rainfall and water level each have a 40% weight and soil moisture has a 20% weight.

The experiment also shows that the dominant contributing variable can change between individual scenarios. For example, water level contributed more than rainfall in the Rising Water Level scenario, while rainfall contributed more than water level in the Heavy Rainfall scenario.

## Interpretation

The experiment demonstrates that the FloodGuard-X model responds differently to environmental conditions depending on their normalized values.

A variable with a high normalized value can produce a larger contribution even when another variable has the same model weight.

Therefore, variable influence depends on both:

* The assigned model weight
* The normalized value of the environmental variable

## Limitation

This experiment measures influence within the proposed mathematical model.

It does not establish the actual real-world importance of rainfall, water level, or soil moisture f

