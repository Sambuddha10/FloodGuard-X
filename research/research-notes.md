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
# Experiment 7: Variable Interaction Analysis

## Objective

To investigate how combinations of environmental variables affect the Flood Risk Index (FRI).

The experiment examines whether multiple elevated environmental conditions produce a different risk level compared with elevated conditions occurring individually.

## Method

The current FRI model uses:

* Rainfall = 40%
* Water Level = 40%
* Soil Moisture = 20%

Several controlled combinations of environmental conditions were tested while using the same normalization and weighting structure.

## Interaction Scenarios

| Scenario                           |   FRI |
| ---------------------------------- | ----: |
| High Rainfall + Low Water          | 50.00 |
| Low Rainfall + High Water          | 50.00 |
| High Rainfall + High Water         | 74.00 |
| High Rainfall + High Soil Moisture | 67.00 |
| High Water + High Soil Moisture    | 67.00 |
| All High Conditions                | 92.33 |

## Interaction Comparison

The first three scenarios provide a direct comparison:

| Condition                  |   FRI |
| -------------------------- | ----: |
| High Rainfall + Low Water  | 50.00 |
| Low Rainfall + High Water  | 50.00 |
| High Rainfall + High Water | 74.00 |

When either rainfall or water level was elevated while the other remained relatively low, the FRI was 50.00.

When both rainfall and water level were elevated, the FRI increased to 74.00.

This shows that simultaneous high values from strongly weighted variables can substantially increase the overall FRI.

## Multi-Variable Interaction

Additional combinations were tested:

| Combination                        |   FRI |
| ---------------------------------- | ----: |
| High Rainfall + High Soil Moisture | 67.00 |
| High Water + High Soil Moisture    | 67.00 |
| All High Conditions                | 92.33 |

The combination of all three elevated environmental variables produced an FRI of 92.33, which is substantially higher than the scenarios containing only two elevated variables.

## Finding

The experiment demonstrates that combinations of elevated environmental variables can produce substantially higher FRI values than conditions where only one major variable is elevated.

In particular, combining high rainfall and high water level increased the FRI from 50.00 for either individual high-condition scenario to 74.00 when both conditions were high.

When rainfall, water level, and soil moisture were all elevated, the FRI reached 92.33.

This indicates that the current weighted model responds strongly to simultaneous increases in multiple environmental variables.

## Interpretation

The result demonstrates an important property of the additive FRI model.

Because the contributions from rainfall, water level, and soil moisture are combined, simultaneous increases in multiple variables accumulate in the final FRI.

The experiment therefore provides evidence that the model can represent increasing risk associated with multiple elevated environmental conditions.

However, the current model does not contain an explicit nonlinear interaction term. The observed combined effect is therefore the result of adding the weighted contributions of the variables.

## Limitation

This experiment demonstrates mathematical interaction within the proposed FRI model.

It does not prove that the tested combinations accurately represent real-world flood interactions.

Real-world environmental variables may interact in nonlinear ways that are not captured by the current additive model.

Validation using appropriate observational data would be required to investigate real-world interaction effects.

---

# Updated Overall Research Findings

The seven experiments provide an initial evaluation of the FloodGuard-X model.

The experiments demonstrate that:

1. The FRI calculation consistently applies the predefined mathematical model.
2. Rainfall and water level have greater model influence than soil moisture under the current weighting structure.
3. Rainfall and water level show similar relative contributions across the tested scenarios.
4. Alternative rainfall and water-level weights change numerical FRI values while the tested scenarios retain their original risk categories.
5. The LOW/MEDIUM and MEDIUM/HIGH classification boundaries operate consistently.
6. The rule-based anomaly mechanism can identify severe or combined unusual environmental conditions.
7. The model provides interpretable explanations for risk, anomaly detection, and variable contributions.
8. Variable influence depends on both the assigned weight and the normalized environmental value.
9. Simultaneously elevated environmental variables can substantially increase the final FRI.
10. The current additive model represents combined conditions through the accumulation of weighted variable contributions.

These findings describe the behavior of the proposed model under controlled synthetic conditions and should not be interpreted as evidence of real-world predictive accuracy.

---

# Updated Research Question

Based on the completed experiments, the research can be framed around:

**How does the weighting and interaction of environmental variables affect the sensitivity and stability of a lightweight, explainable, dataset-free flood-risk model?**

A supporting question is:

**How effectively can a lightweight, explainable flood-risk model estimate changing flood risk using controlled synthetic environmental conditions without relying on historical datasets?**
# Experiment 8: Robustness Analysis

## Objective

To evaluate whether small changes in environmental input values produce gradual and consistent changes in the Flood Risk Index (FRI).

This experiment examines the local robustness of the model around a predefined baseline condition.

## Baseline Conditions

* Rainfall = 60 mm
* Water Level = 2.0 m
* Soil Moisture = 60%
* Baseline FRI = 44.00

## Method

Each environmental variable was independently perturbed around the baseline while the other variables were kept constant.

The following ranges were tested:

* Rainfall: 50–70 mm
* Water Level: 1.8–2.2 m
* Soil Moisture: 50–70%

The resulting FRI values were compared with the baseline FRI.

## Rainfall Perturbation

| Rainfall (mm) |   FRI | Change from Baseline |
| ------------: | ----: | -------------------: |
|            50 | 41.33 |                -2.67 |
|            55 | 42.67 |                -1.33 |
|            60 | 44.00 |                +0.00 |
|            65 | 45.33 |                +1.33 |
|            70 | 46.67 |                +2.67 |

The FRI increased gradually as rainfall increased and decreased gradually as rainfall decreased.

## Water Level Perturbation

| Water Level (m) |   FRI | Change from Baseline |
| --------------: | ----: | -------------------: |
|             1.8 | 42.40 |                -1.60 |
|             1.9 | 43.20 |                -0.80 |
|             2.0 | 44.00 |                +0.00 |
|             2.1 | 44.80 |                +0.80 |
|             2.2 | 45.60 |                +1.60 |

The FRI changed gradually as the water level was varied around the baseline.

## Soil Moisture Perturbation

| Soil Moisture (%) |   FRI | Change from Baseline |
| ----------------: | ----: | -------------------: |
|                50 | 42.00 |                -2.00 |
|                55 | 43.00 |                -1.00 |
|                60 | 44.00 |                +0.00 |
|                65 | 45.00 |                +1.00 |
|                70 | 46.00 |                +2.00 |

The FRI also changed gradually with changes in soil moisture.

## Finding

The experiment showed that small changes in the environmental inputs produced gradual changes in the FRI within the tested ranges.

For a rainfall change of ±5 mm, the FRI changed by approximately ±1.33.

For a water-level change of ±0.1 m, the FRI changed by approximately ±0.80.

For a soil-moisture change of ±5%, the FRI changed by approximately ±1.00.

No unexpected discontinuities were observed in the tested ranges.

This indicates that the current FRI calculation behaves smoothly around the selected baseline condition.

## Interpretation

The robustness behavior is consistent with the additive mathematical structure of the model.

Because the normalized inputs are combined using fixed weights, small changes in an individual input produce proportional changes in its contribution to the FRI, provided the input remains within the normal operating range and does not encounter a normalization boundary.

## Limitation

This experiment evaluates local robustness around only one baseline condition and within limited input ranges.

It does not establish robustness across the entire possible environmental input space.

Additional testing would be required near normalization limits, classification boundaries, and extreme environmental conditions.

---

# Updated Overall Research Findings

The eight experiments provide an initial evaluation of the FloodGuard-X model.

The experiments demonstrate that:

1. The FRI calculation consistently applies the predefined mathematical model.
2. Rainfall and water level have greater model influence than soil moisture under the current weighting structure.
3. Rainfall and water level show similar relative contributions across the tested scenarios.
4. Alternative rainfall and water-level weights change numerical FRI values while the tested scenarios retain their original risk categories.
5. The LOW/MEDIUM and MEDIUM/HIGH classification boundaries operate consistently.
6. The rule-based anomaly mechanism can identify severe or combined unusual environmental conditions.
7. The model provides interpretable explanations for risk, anomaly detection, and variable contributions.
8. Variable influence depends on both the assigned weight and the normalized environmental value.
9. Simultaneously elevated environmental variables can substantially increase the final FRI.
10. The current additive model represents combined conditions through the accumulation of weighted variable contributions.
11. Small changes in environmental inputs produce gradual FRI changes within the tested local ranges.
12. No unexpected discontinuities were observed during the robustness experiment.

These findings describe the behavior of the proposed model under controlled synthetic conditions and should not be interpreted as evidence of real-world predictive accuracy.

---

# Updated Research Question

Based on the completed experiments, the research can be framed around:

**How does the weighting, interaction, and sensitivity of environmental variables affect the stability and interpretability of a lightweight, explainable, dataset-free flood-risk model?**

A supporting question is:

**How effectively can a lightweight, explainable flood-risk model estimate changing flood risk using controlled synthetic environmental conditions without relying on historical datasets?**
## Experiment 9: Boundary Sensitivity Analysis

### Objective

This experiment evaluates how the FloodGuard-X classification behaves around the predefined FRI boundaries of 40 and 70. It also examines whether small changes in environmental variables produce abrupt changes in the calculated Flood Risk Index (FRI).

### Classification Boundary Test

The LOW/MEDIUM boundary was tested using FRI values from 39.0 to 41.0.

Results:

| FRI | Classification |
|---:|---|
| 39.0 | LOW |
| 39.5 | LOW |
| 39.9 | LOW |
| 40.0 | MEDIUM |
| 40.1 | MEDIUM |
| 40.5 | MEDIUM |
| 41.0 | MEDIUM |

The MEDIUM/HIGH boundary was tested using FRI values from 69.0 to 71.0.

Results:

| FRI | Classification |
|---:|---|
| 69.0 | MEDIUM |
| 69.5 | MEDIUM |
| 69.9 | MEDIUM |
| 70.0 | HIGH |
| 70.1 | HIGH |
| 70.5 | HIGH |
| 71.0 | HIGH |

The results confirm that the classification rules operate deterministically at the predefined boundaries. A small change around a boundary can change the category because the model uses discrete threshold-based classification.

### Environmental Sensitivity Near the Lower Boundary

Baseline conditions:

- Rainfall = 60 mm
- Water Level = 2.0 m
- Soil Moisture = 60%
- Baseline FRI = 44.00
- Classification = MEDIUM

Small environmental changes produced the following results:

| Change | FRI | Classification |
|---|---:|---|
| Rainfall -5 mm | 42.67 | MEDIUM |
| Rainfall +5 mm | 45.33 | MEDIUM |
| Water -0.1 m | 43.20 | MEDIUM |
| Water +0.1 m | 44.80 | MEDIUM |
| Soil -5% | 43.00 | MEDIUM |
| Soil +5% | 45.00 | MEDIUM |

The tested small perturbations changed the numerical FRI gradually while maintaining the same MEDIUM classification.

### Environmental Sensitivity Near the Upper Boundary

Baseline conditions:

- Rainfall = 100 mm
- Water Level = 3.0 m
- Soil Moisture = 70%
- Baseline FRI = 64.67
- Classification = MEDIUM

Small environmental changes produced the following results:

| Change | FRI | Classification |
|---|---:|---|
| Rainfall -5 mm | 63.33 | MEDIUM |
| Rainfall +5 mm | 66.00 | MEDIUM |
| Water -0.1 m | 63.87 | MEDIUM |
| Water +0.1 m | 65.47 | MEDIUM |
| Soil -5% | 63.67 | MEDIUM |
| Soil +5% | 65.67 | MEDIUM |

The tested perturbations again produced gradual FRI changes without classification changes. The baseline was below the HIGH threshold, so these tests examine behavior near the upper boundary rather than directly crossing FRI = 70.

### Finding

The boundary sensitivity experiment demonstrates that FloodGuard-X follows deterministic threshold behavior. The FRI changes gradually under small environmental perturbations in the tested ranges, while classification remains stable when the resulting FRI stays within the same threshold interval.

However, values very close to the thresholds may change classification after a small perturbation. Therefore, threshold-based classification provides clear interpretability but can introduce categorical sensitivity near boundary values.

This experiment evaluates mathematical behavior of the proposed model and does not establish whether the selected thresholds correspond to real-world flood warning levels.

---

## Updated Overall Research Findings

The experiments conducted so far indicate that:

1. The FRI calculation is mathematically consistent across the tested synthetic scenarios.
2. Rainfall and water level have greater model influence than soil moisture under the selected 40/40/20 weighting scheme.
3. Rainfall and water level produce similar relative contributions under the current normalization and weighting.
4. Alternative weighting configurations change numerical FRI values while maintaining classifications for the tested scenarios.
5. The threshold mechanism produces consistent LOW, MEDIUM, and HIGH classifications at the predefined boundaries.
6. The rule-based anomaly mechanism identifies severe and combined abnormal environmental conditions in the tested scenarios.
7. The model provides interpretable risk explanations through variable contributions.
8. Variable influence depends on both the assigned weight and the normalized environmental value.
9. Simultaneously elevated environmental variables substantially increase the resulting FRI.
10. The additive model represents combined environmental conditions through accumulation of weighted contributions rather than explicit nonlinear interaction terms.
11. Small input changes produce gradual FRI changes within the tested local ranges.
12. No unexpected discontinuities were observed during the local robustness tests.
13. Boundary analysis confirms that classification changes occur exactly at the predefined FRI thresholds.
14. Small environmental perturbations generally preserve classification when the resulting FRI remains sufficiently away from a threshold.
15. The model can become categorically sensitive when FRI values are very close to the predefined thresholds.
16. Overall, the experiments support the mathematical consistency, interpretability, and controlled behavior of the proposed lightweight model, while emphasizing that its weights, thresholds, anomaly rules, and synthetic scenarios require real-world validation before operational deployment.

### Updated Research Question

**How does the weighting, interaction, and sensitivity of environmental variables affect the stability and interpretability of a lightweight, explainable, dataset-free flood-risk model?**

### Supporting Research Question

**How effectively can a lightweight, explainable flood-risk model estimate changing flood risk using controlled synthetic environmental conditions without relying on historical datasets?**



