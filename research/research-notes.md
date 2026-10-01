# FloodGuard-X Research Notes

## Experiment 1: Flood Risk Index Evaluation

### Objective

To evaluate whether a weighted Flood Risk Index (FRI) can classify different environmental flood scenarios using synthetic data without relying on an external dataset.

---

## Environmental Variables

The model uses four environmental variables:

1. Rainfall
2. Water Level
3. Soil Moisture
4. Temperature

Temperature is currently recorded as contextual information and is not included in the FRI calculation.

---

## Flood Risk Index

The Flood Risk Index is calculated using:

FRI = 0.40R + 0.40W + 0.20S

Where:

- R = normalized rainfall score
- W = normalized water-level score
- S = soil-moisture score

---

## Normalization

### Rainfall

Rainfall is normalized using a maximum reference value of 150 mm.

R = (Rainfall / 150) × 100

Values above 150 mm are capped at 100.

### Water Level

Water level is normalized using a maximum reference value of 5 metres.

W = (Water Level / 5) × 100

Values above 5 metres are capped at 100.

### Soil Moisture

Soil moisture is already represented as a percentage from 0 to 100.

---

## Risk Classification

| FRI Range | Risk Level |
|-----------|------------|
| 0–39.9 | LOW |
| 40–69.9 | MEDIUM |
| 70–100 | HIGH |

---

## Dataset

The project uses a synthetic dataset created specifically for controlled experimentation.

The dataset contains environmental scenarios representing different combinations of rainfall, water level, soil moisture, and temperature.

No external dataset is used in this experiment.

---

## Research Direction

The initial experiment investigates whether the proposed weighted FRI provides consistent and interpretable risk classifications under different environmental conditions.

Future experiments will investigate:

- Sensitivity to rainfall
- Sensitivity to water level
- Sensitivity to soil moisture
- Alternative weighting schemes
- Risk classification stability
- Anomaly detection
- Comparison with machine-learning models
