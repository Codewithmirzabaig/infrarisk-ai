# InfraRisk AI API Reference

## Feature Engineering

### build_features()

Generates infrastructure finance features from raw project data.

---

## Credit Risk

### train_credit_model()

Trains XGBoost credit risk model.

Returns:
- Trained model
- Risk predictions

---

## Monte Carlo

### monte_carlo_engine()

Runs stress testing simulations.

Returns:
- Simulated DSCR
- Default probability

---

## Forecasting

### revenue_forecasting()

Generates revenue forecasts.

Returns:
- Forecast
- Confidence intervals

---

## InfraRisk Lab

### simulate_event()

Parameters:
- project_type
- leverage
- mode

Returns:
- Risk score
- Ratings
- Recommendation