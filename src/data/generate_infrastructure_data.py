import pandas as pd
import numpy as np

np.random.seed(42)

n_projects = 10000

project_types = [
    "Transportation",
    "Renewable Energy",
    "Airport",
    "Port",
    "Telecom"
]

df = pd.DataFrame({
    "project_id": range(1, n_projects + 1),
    "project_type": np.random.choice(project_types, n_projects),

    "project_cost_musd": np.random.uniform(50, 5000, n_projects),

    "debt_ratio": np.random.uniform(0.5, 0.9, n_projects),

    "interest_rate": np.random.uniform(3, 12, n_projects),

    "construction_delay_months": np.random.randint(0, 24, n_projects),

    "cost_overrun_pct": np.random.uniform(0, 50, n_projects),

    "gdp_growth": np.random.uniform(-5, 10, n_projects),

    "inflation_rate": np.random.uniform(1, 15, n_projects),

    "sovereign_risk_score": np.random.uniform(0, 100, n_projects),

    "traffic_demand_index": np.random.uniform(50, 150, n_projects)
})
df["dscr"] = (
    2
    - df["debt_ratio"]
    - (df["construction_delay_months"] * 0.02)
    - (df["cost_overrun_pct"] * 0.01)
    + (df["gdp_growth"] * 0.03)
)

df["dscr"] = df["dscr"].clip(0.3, 3.0)
df["llcr"] = (
    df["dscr"]
    + np.random.normal(0.5, 0.2, n_projects)
)

df["llcr"] = df["llcr"].clip(0.5, 5)
df["plcr"] = (
    df["llcr"]
    + np.random.normal(0.3, 0.1, n_projects)
)

df["plcr"] = df["plcr"].clip(0.5, 6)
conditions = [
    df["dscr"] < 1.0,
    (df["dscr"] >= 1.0) & (df["dscr"] < 1.5),
    df["dscr"] >= 1.5
]

labels = [
    "High Risk",
    "Medium Risk",
    "Low Risk"
]

df["risk_category"] = np.select(
    conditions,
    labels,
    default="Medium Risk"
)
df.to_csv(
    "data/processed/infrastructure_projects.csv",
    index=False
)

print(df.head())
print(df.shape)
