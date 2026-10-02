# 🌊 FloodGuard-X

### Lightweight • Explainable • Dataset-Free Flood Risk Detection & Disaster Management System

<p align="center">
  <b>Turning environmental conditions into an interpretable Flood Risk Index.</b>
</p>
<p align="center">

  <a href="YOUR-GITHUB-PAGES-LINK">
    <img src="https://img.shields.io/badge/🌊%20LIVE%20DEMO-6f42c1?style=for-the-badge">
  </a>

</p>

<p align="center">
  <img src="https://img.shields.io/badge/Project-FloodGuard--X-6f42c1?style=for-the-badge">
  <img src="https://img.shields.io/badge/Domain-Data%20Science-3776AB?style=for-the-badge">
  <img src="https://img.shields.io/badge/Language-JavaScript-F7DF1E?style=for-the-badge">
  <img src="https://img.shields.io/badge/Cost-Zero%20Cost-2ea44f?style=for-the-badge">
</p>

---

## 📌 Overview

**FloodGuard-X** is a lightweight, explainable flood-risk detection and disaster-management prototype designed to estimate changing flood risk from environmental conditions.

Instead of depending on a historical dataset, the system uses **controlled and synthetic environmental scenarios** to study how a mathematical risk model behaves under different conditions.

The system converts:

* 🌧️ Rainfall
* 🌊 Water level
* 🌱 Soil moisture

into a **Flood Risk Index (FRI)** ranging from **0–100**.

The project focuses on **transparency, interpretability, sensitivity analysis, and reproducibility**.

---

## 🎯 Objectives

* Detect changing flood-risk conditions.
* Produce an interpretable **Flood Risk Index (FRI)**.
* Explain how individual environmental variables contribute to risk.
* Detect unusual environmental conditions using rule-based anomaly detection.
* Study model sensitivity and robustness.
* Test model behavior under extreme conditions.
* Provide a lightweight architecture that can potentially be connected to real sensors in the future.
* Explore how a dataset-free approach can be evaluated using controlled scenarios.

---

## 🧮 Flood Risk Index

FloodGuard-X currently uses the following weighted model:

```text
FRI = 0.40R + 0.40W + 0.20S
```

Where:

| Variable      | Weight |
| ------------- | -----: |
| Rainfall      |    40% |
| Water Level   |    40% |
| Soil Moisture |    20% |

The input variables are normalized to a **0–100 scale** before calculating the FRI.

### Risk Classification

|      FRI | Risk Level |
| -------: | ---------- |
|  0–39.99 | 🟢 LOW     |
| 40–69.99 | 🟡 MEDIUM  |
|   70–100 | 🔴 HIGH    |

> **Important:** These weights, normalization limits, and thresholds are initial model assumptions for this prototype. They are not presented as scientifically validated flood-warning thresholds.

---

## 🔍 Explainability

FloodGuard-X does not only output a risk category.

It also displays the contribution of each variable to the final FRI.

For example:

```text
Rainfall Contribution
Water Level Contribution
Soil Moisture Contribution
        ↓
    Final FRI
        ↓
Risk Classification
```

This makes the model easier to inspect and understand compared with a black-box prediction system.

---

## 🚨 Anomaly Detection

FloodGuard-X includes a lightweight rule-based anomaly detection system.

Examples of monitored conditions include:

* Extremely high rainfall
* Unusually high rainfall
* Critical water level
* Unusually high water level
* Extremely high soil moisture
* Multiple abnormal conditions occurring together

The system generates an **anomaly score** and identifies whether the observed conditions require anomaly attention.

---

## 🖥️ Dashboard Features

The live dashboard provides:

* 🌊 Current flood-risk status
* 📊 Flood Risk Index
* 🎯 Circular FRI gauge
* 🎚️ FRI progress indicator
* 🎛️ Scenario-based simulation
* 📝 Scenario descriptions
* ⚡ Simulation status indicator
* 🌧️ Rainfall monitoring
* 🌊 Water-level monitoring
* 🌱 Soil-moisture monitoring
* 🌡️ Temperature display
* 📈 Variable contribution analysis
* 🔎 Risk explanation
* 🚨 Emergency recommendations
* ⚠️ Anomaly detection
* 📜 Risk history
* 📉 Risk trend visualization
* 🔄 System reset

---

## 🧪 Research & Experiments

FloodGuard-X includes a separate research component for evaluating the behavior of the proposed model.

### Completed Experiments

| Experiment            | Purpose                                        |
| --------------------- | ---------------------------------------------- |
| FRI Evaluation        | Evaluate the model across controlled scenarios |
| Sensitivity Analysis  | Study the effect of individual variables       |
| Alternative Weighting | Compare different weighting configurations     |
| Threshold Stability   | Examine classification boundaries              |
| Anomaly Analysis      | Test rule-based anomaly detection              |
| Variable Influence    | Analyze individual variable contributions      |
| Variable Interaction  | Study combined environmental conditions        |
| Robustness Analysis   | Test response to small input changes           |
| Boundary Sensitivity  | Examine behavior around risk boundaries        |
| Extreme Conditions    | Test normalization and FRI limits              |

### Key Research Question

> **How does the weighting, interaction, and sensitivity of environmental variables affect the stability and interpretability of a lightweight, explainable, dataset-free flood-risk model?**

### Supporting Question

> **How effectively can a lightweight, explainable flood-risk model estimate changing flood risk using controlled synthetic environmental conditions without relying on historical datasets?**

---

## 🧪 Dataset-Free Approach

A major design choice of FloodGuard-X is that the current prototype does **not depend on an external historical dataset**.

Instead, controlled scenarios are used to evaluate model behavior.

Example:

```text
Normal Conditions
        ↓
Heavy Rainfall
        ↓
Rising Water Level
        ↓
Extreme Flood
        ↓
Model Response Analysis
```

This allows the research to focus on:

* Model behavior
* Sensitivity
* Stability
* Explainability
* Boundary behavior
* Extreme-condition handling

rather than claiming predictive accuracy from unavailable real-world labels.

---

## 🧩 System Architecture

```text
              ┌──────────────────────┐
              │ Environmental Inputs  │
              │ Rainfall / Water /    │
              │ Soil Moisture         │
              └──────────┬───────────┘
                         ↓
              ┌──────────────────────┐
              │   Normalization      │
              └──────────┬───────────┘
                         ↓
              ┌──────────────────────┐
              │   FRI Calculation    │
              │    40/40/20 Model    │
              └──────────┬───────────┘
                         ↓
              ┌──────────────────────┐
              │ Risk Classification   │
              │ LOW / MEDIUM / HIGH   │
              └──────────┬───────────┘
                         ↓
        ┌────────────────┴────────────────┐
        ↓                                 ↓
┌──────────────────┐             ┌──────────────────┐
│ Explainability   │             │ Anomaly Detection│
│ Contributions    │             │ Rule-Based Score │
└────────┬─────────┘             └────────┬─────────┘
         ↓                                ↓
         └──────────────┬─────────────────┘
                        ↓
              ┌──────────────────────┐
              │   Web Dashboard      │
              │ History / Trend /    │
              │ Recommendations      │
              └──────────────────────┘
```

---

## 🛠️ Technology Stack

### Frontend

* HTML5
* CSS3
* JavaScript
* Canvas-based visualization

### Research

* Python
* Synthetic scenario generation
* Numerical analysis
* Sensitivity analysis
* Robustness analysis

### Development

* GitHub
* GitHub Pages
* GitHub Codespaces

---

## 📂 Project Structure

```text
FloodGuard-X/
│
├── index.html
│
├── research/
│   ├── scenarios.csv
│   ├── research-notes.md
│   ├── experiments.py
│   ├── evaluation.py
│   ├── sensitivity.py
│   ├── weighting.py
│   ├── threshold.py
│   ├── anomaly_experiment.py
│   ├── influence.py
│   ├── interaction.py
│   ├── robustness.py
│   ├── boundary_sensitivity.py
│   └── extreme_conditions.py
│
└── README.md
```

---

## 🚀 Running the Project

### Option 1 — Live Demo

The project can be deployed using **GitHub Pages**.

### Option 2 — Run Locally

Clone the repository:

```bash
git clone https://github.com/YOUR-USERNAME/FloodGuard-X.git
```

Open:

```text
index.html
```

in a web browser.

No backend server or database is required for the current prototype.

---

## 🎮 Simulation Scenarios

FloodGuard-X currently provides several controlled scenarios:

### Normal Conditions

Represents relatively stable environmental conditions.

### Heavy Rainfall

Simulates increased rainfall accompanied by elevated environmental risk.

### Rising Water Level

Focuses on increasing water-level conditions.

### Extreme Flood

Represents severe environmental conditions across multiple variables.

### Random Scenario

Generates a random combination of environmental conditions within the model's input range.

---

## 📊 Research Findings

The completed experiments indicate that:

* The FRI remains within the intended **0–100 range** under tested extreme inputs.
* Rainfall and water level have equal model weights and therefore produce similar sensitivity under the tested normalization ranges.
* Soil moisture has a smaller model contribution because it has a lower assigned weight.
* Small environmental changes generally produce gradual FRI changes within tested local ranges.
* The LOW/MEDIUM and MEDIUM/HIGH boundaries behave deterministically at FRI 40 and FRI 70.
* Multiple high environmental conditions can produce substantially higher combined FRI values.
* Alternative weighting configurations can change numerical FRI values while leaving classifications unchanged in the tested scenarios.

These findings describe **model behavior**, not real-world flood prediction accuracy.

---

## ⚠️ Limitations

FloodGuard-X is currently a research-oriented prototype.

Important limitations include:

* No historical flood dataset is currently used.
* No real-time sensor hardware is currently connected.
* Risk thresholds have not been validated against real-world flood events.
* The weighting system represents an initial modeling assumption.
* The anomaly detector is rule-based.
* Synthetic scenarios cannot establish real-world predictive accuracy.
* The current system should not be used as an operational emergency-warning system.

---

## 🔮 Future Scope

Possible future development includes:

* 🔌 Integration with physical water-level and environmental sensors
* 🌐 Real-time environmental monitoring
* 📡 IoT-based data transmission
* 🗺️ Geographic flood-risk visualization
* 📱 Mobile notification support
* 🧠 Data-driven model comparison
* 📚 Validation using real-world historical datasets
* 🤖 Machine-learning-based risk prediction
* 📈 Larger-scale experimental evaluation
* 🏘️ Community-level disaster management features

---

## 💡 Research Potential

FloodGuard-X is designed so that the current lightweight mathematical model can serve as a baseline for future research.

A future study could compare:

```text
Rule-Based FRI
       ↓
Statistical Models
       ↓
Machine Learning Models
       ↓
Explainability Comparison
       ↓
Real-World Validation
```

This creates a possible pathway from a **student prototype → experimental study → research paper**.

---

## 💰 Cost

### Current Prototype Cost

**₹0**

The current system uses:

* Open-source technologies
* GitHub
* GitHub Pages
* GitHub Codespaces for research execution
* Synthetic data

No paid API, cloud database, or external dataset is required for the current implementation.

---

## 📜 Project Status

```text
🟢 Core Risk Model             COMPLETE
🟢 Web Dashboard               COMPLETE
🟢 FRI Gauge                   COMPLETE
🟢 Scenario Simulation         COMPLETE
🟢 Explainability              COMPLETE
🟢 Anomaly Detection           COMPLETE
🟢 Risk History                COMPLETE
🟢 Risk Trend                  COMPLETE
🟢 Emergency Recommendations   COMPLETE
🟢 Research Experiments 1–10  COMPLETE
🟡 Real-Time Monitoring        FUTURE
🟡 Sensor Integration          FUTURE
🟡 Real-World Validation       FUTURE
```

---

## 👨‍💻 Project

**FloodGuard-X**

A student-led Data Science project exploring lightweight, explainable, dataset-free flood-risk modeling and disaster-management support.

---

<p align="center">
  <b>🌊 FloodGuard-X</b><br>
  <i>From environmental conditions to explainable flood-risk insights.</i>
</p>
