# InfraRisk AI: Infrastructure Credit Risk Intelligence Platform
![CI](https://img.shields.io/badge/CI-GitHub%20Actions-success)
![Python](https://img.shields.io/badge/Python-3.12-blue)
![Docker](https://img.shields.io/badge/Docker-Enabled-blue)
![Tests](https://img.shields.io/badge/Tests-Passing-success)

## Overview

InfraRisk AI is an end-to-end infrastructure finance risk intelligence platform designed to assess, forecast, and simulate risks associated with large-scale infrastructure projects. The platform combines machine learning, explainable AI, quantitative risk analytics, forecasting, and simulation to support data-driven decision-making for project finance stakeholders.

The system evaluates infrastructure projects across multiple sectors, including transportation, energy, telecommunications, airports, and ports. It provides project-level risk assessment, probability of default estimation, expected loss calculations, revenue forecasting, and stress-testing capabilities through an interactive dashboard.

---

## Problem Statement

Infrastructure projects involve significant capital investment and are exposed to various risks including:

* Construction delays
* Cost overruns
* Sovereign and political risks
* Demand uncertainty
* Inflation and interest rate fluctuations
* Regulatory changes

Traditional project finance assessments rely heavily on spreadsheets and static assumptions. InfraRisk AI introduces an AI-driven approach to improve risk evaluation and portfolio monitoring.

---

## Key Features

### Infrastructure Credit Risk Modeling

* XGBoost-based credit risk classification
* Project risk categorization
* Probability of Default (PD) estimation
* Expected Loss (EL) calculation

### Explainable AI

* SHAP explainability framework
* Feature contribution analysis
* Transparent risk assessment

### Monte Carlo Stress Testing

* 10,000 scenario simulations
* DSCR distribution analysis
* Default probability estimation
* Expected loss calculation

### Revenue Forecasting

* Prophet forecasting model
* Infrastructure revenue projections
* Confidence interval generation
* Future demand analysis

### InfraRisk Lab Simulation

Interactive infrastructure finance simulation environment:

Supported Assets:

* Toll Roads
* Airports
* Solar Plants
* Ports
* Telecom Towers

Simulated Events:

* Construction Delays
* Inflation Shocks
* Sovereign Downgrades
* Traffic Demand Collapse
* Regulatory Changes

AI-generated mitigation recommendations are provided for each scenario.

### Streamlit Dashboard

Integrated dashboard modules:

* Executive Overview
* Credit Risk Analytics
* SHAP Explainability
* Monte Carlo Analysis
* Revenue Forecasting
* InfraRisk Lab Simulation

---

## Project Architecture

```text
infrarisk-ai/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── src/
│   ├── data/
│   ├── features/
│   ├── models/
│   │   ├── credit_risk/
│   │   ├── forecasting/
│   │   ├── monte_carlo/
│   │   ├── shap_explainability/
│   │   └── sovereign_risk/
│   │
│   ├── simulation/
│   ├── dashboard/
│   └── utils/
│
├── tests/
├── reports/
│   └── figures/
│
├── docker/
├── docs/
├── configs/
│
├── requirements.txt
├── docker-compose.yml
└── README.md
```

---

## Dataset

Synthetic infrastructure finance dataset containing:

* 10,000 infrastructure projects
* Transportation projects
* Airports
* Ports
* Renewable energy projects
* Telecom infrastructure

Core Variables:

* Project Cost
* Debt Ratio
* Interest Rate
* Construction Delay
* Cost Overrun
* GDP Growth
* Inflation
* Sovereign Risk Score
* Traffic Demand Index
* DSCR
* LLCR
* PLCR

---

## Feature Engineering

Engineered Features:

* Leverage Risk
* Construction Risk Score
* Macroeconomic Risk Score
* Financial Strength
* Probability of Default (PD)
* Loss Given Default (LGD)
* Exposure at Default (EAD)
* Expected Loss (EL)
* Debt Burden Index
* Revenue Vulnerability
* Composite Risk Score

---

## Machine Learning Model

### XGBoost Credit Risk Model

Objective:
Predict infrastructure project default risk.

Performance:

* Accuracy: 98.25%
* ROC-AUC: 0.989

Evaluation Metrics:

* Accuracy
* ROC-AUC
* Classification Report
* Confusion Matrix

---

## Explainable AI

SHAP (SHapley Additive Explanations) was used to explain model predictions and identify the most influential drivers of infrastructure project risk.

Generated Outputs:

* SHAP Summary Plot
* Feature Importance Analysis

---

## Monte Carlo Risk Engine

The platform performs large-scale scenario simulations to estimate project risk under uncertainty.

Simulation Inputs:

* GDP Growth Shock
* Inflation Shock
* Interest Rate Shock
* Traffic Demand Shock
* Cost Overrun Shock

Outputs:

* Probability of Default
* Expected Loss
* DSCR Distribution
* Stress-Test Results

---

## Revenue Forecasting

Prophet forecasting model used for infrastructure revenue prediction.

Forecast Outputs:

* Future Revenue Estimates
* Confidence Intervals
* Trend Analysis

---

## InfraRisk Lab

A gamified infrastructure finance simulation platform where users evaluate projects under various stress scenarios and receive AI-driven recommendations.

Example Events:

* Construction Delay
* Sovereign Downgrade
* Inflation Shock
* Regulatory Change

Outputs:

* Initial Risk Score
* Stressed Risk Score
* Credit Rating Change
* Mitigation Recommendations

---

## Testing

Framework:

* Pytest

Test Coverage:

* Feature Engineering
* Expected Loss Calculation
* Risk Score Validation
* Monte Carlo Engine
* InfraRisk Lab Simulation

Results:

```text
5 Passed
```

---

## Docker Deployment

Build:

```bash
docker compose build
```

Run:

```bash
docker compose up
```

Access Dashboard:

```text
http://localhost:8501
```

---

## Dashboard Screenshots

Add screenshots for:

1. Executive Overview
2. Credit Risk Analytics
3. SHAP Explainability
4. Monte Carlo Stress Testing
5. Revenue Forecasting
6. InfraRisk Lab

---

## Future Enhancements

* Graph Neural Networks (GNN)
* Temporal Fusion Transformers (TFT)
* Satellite Imagery Analysis
* Reinforcement Learning Debt Optimization
* NLP Contract Intelligence
* Sovereign Risk API Integration
* Portfolio-Level Risk Analytics
* Real-Time Infrastructure Monitoring

---

## Technologies Used

* Python
* Pandas
* NumPy
* XGBoost
* SHAP
* Prophet
* Streamlit
* Matplotlib
* Scikit-Learn
* Pytest
* Docker

---

## Author

Mirza Sharif Baig

Data Scientist | Machine Learning | Risk Analytics | Infrastructure Intelligence

---

## License

This project was developed as part of the InfraRisk AI Data Science Assessment and is intended for educational and research purposes.
