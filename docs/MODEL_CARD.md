# InfraRisk AI Model Card

## Model Name
InfraRisk AI Credit Risk Engine

## Model Type
XGBoost Classifier

## Purpose
Predict infrastructure project default risk and estimate expected loss.

## Inputs
- DSCR
- LLCR
- PLCR
- Leverage Ratio
- Sovereign Risk Score
- Construction Risk Score
- Revenue Forecast Metrics
- Macroeconomic Indicators

## Outputs
- Probability of Default (PD)
- Risk Category
- Expected Loss

## Explainability
SHAP Explainability Framework

## Limitations
- Synthetic dataset
- Limited real-world calibration
- Intended for educational and portfolio demonstration purposes

## Monitoring
MLflow experiment tracking enabled.