import os
import pandas as pd
import numpy as np


INPUT_PATH = "data/processed/infrastructure_projects.csv"
OUTPUT_PATH = "data/processed/infrastructure_features.csv"


def build_features(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    # 1. Leverage Risk
    df["leverage_risk"] = df["debt_ratio"] * df["project_cost_musd"]

    # 2. Construction Risk Score
    df["construction_risk_score"] = (
        df["construction_delay_months"] * 2
        + df["cost_overrun_pct"]
    ).clip(0, 100)

    # 3. Macroeconomic Risk Score
    df["macro_risk_score"] = (
        df["inflation_rate"] * 3
        - df["gdp_growth"] * 2
    ).clip(0, 100)

    # 4. Financial Strength
    df["financial_strength"] = (
        df["dscr"] * 0.50
        + df["llcr"] * 0.30
        + df["plcr"] * 0.20
    )

    # 5. Probability of Default
    df["pd"] = np.select(
        [
            df["risk_category"] == "High Risk",
            df["risk_category"] == "Medium Risk",
            df["risk_category"] == "Low Risk",
        ],
        [0.15, 0.07, 0.02],
        default=0.07,
    )

    # 6. Loss Given Default
    np.random.seed(42)
    df["lgd"] = np.random.uniform(0.20, 0.50, len(df))

    # 7. Exposure at Default
    df["ead"] = df["project_cost_musd"] * df["debt_ratio"]

    # 8. Expected Loss
    df["expected_loss"] = df["pd"] * df["lgd"] * df["ead"]

    # 9. Debt Burden Index
    df["debt_burden_index"] = (
        df["debt_ratio"] * 100
        + df["interest_rate"] * 2
    ).clip(0, 100)

    # 10. Revenue Vulnerability
    df["revenue_vulnerability"] = (
        100 - df["traffic_demand_index"]
        + df["inflation_rate"] * 2
    ).clip(0, 100)

    # 11. Delay Impact Factor
    df["delay_impact_factor"] = (
        df["construction_delay_months"] / 24
    ).clip(0, 1)

    # 12. Cost Overrun Severity
    df["cost_overrun_severity"] = np.select(
        [
            df["cost_overrun_pct"] < 10,
            (df["cost_overrun_pct"] >= 10) & (df["cost_overrun_pct"] < 25),
            df["cost_overrun_pct"] >= 25,
        ],
        [1, 2, 3],
        default=2,
    )

    # 13. Sovereign Risk Band
    df["sovereign_risk_band"] = pd.cut(
        df["sovereign_risk_score"],
        bins=[-1, 33, 66, 101],
        labels=["Low", "Medium", "High"],
    ).astype(str)

    # 14. DSCR Stress Flag
    df["dscr_stress_flag"] = np.where(df["dscr"] < 1.0, 1, 0)

    # 15. Composite Risk Score
    df["risk_score"] = (
        0.30 * df["construction_risk_score"]
        + 0.25 * df["macro_risk_score"]
        + 0.25 * df["sovereign_risk_score"]
        + 0.20 * (100 - df["financial_strength"] * 20)
    ).clip(0, 100)

    # 16. Model Target
    df["default_flag"] = np.where(
    (
        (df["dscr"] < 1.0)
        |
        (df["construction_risk_score"] > 60)
        |
        (df["sovereign_risk_score"] > 80)
    ),
    1,
    0
)

    return df


def main() -> None:
    if not os.path.exists(INPUT_PATH):
        raise FileNotFoundError(
            f"Input file not found: {INPUT_PATH}. "
            "Run src/data/generate_infrastructure_data.py first."
        )

    df = pd.read_csv(INPUT_PATH)
    features_df = build_features(df)

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    features_df.to_csv(OUTPUT_PATH, index=False)

    print("Feature engineering completed successfully.")
    print(f"Saved file: {OUTPUT_PATH}")
    print(f"Shape: {features_df.shape}")
    print("\nColumns:")
    print(features_df.columns.tolist())

    print("\nPreview:")
    print(features_df.head())


if __name__ == "__main__":
    main()