import sys
from pathlib import Path

import pandas as pd
import streamlit as st
from PIL import Image

ROOT_DIR = Path(__file__).resolve().parents[2]
sys.path.append(str(ROOT_DIR))

from src.simulation.infrarisk_lab import simulate_event


st.set_page_config(
    page_title="InfraRisk AI",
    page_icon="🏗️",
    layout="wide"
)

st.title("InfraRisk AI: Infrastructure Credit Risk Intelligence Platform")

features_path = ROOT_DIR / "data" / "processed" / "infrastructure_features.csv"
mc_path = ROOT_DIR / "data" / "processed" / "monte_carlo_results.csv"
forecast_path = ROOT_DIR / "data" / "processed" / "revenue_forecast.csv"

shap_img = ROOT_DIR / "reports" / "figures" / "shap_summary.png"
mc_img = ROOT_DIR / "reports" / "figures" / "monte_carlo_dscr_distribution.png"
forecast_img = ROOT_DIR / "reports" / "figures" / "revenue_forecast.png"

df = pd.read_csv(features_path)
mc = pd.read_csv(mc_path)
forecast = pd.read_csv(forecast_path)

tabs = st.tabs([
    "Executive Overview",
    "Credit Risk",
    "SHAP Explainability",
    "Monte Carlo",
    "Revenue Forecasting",
    "InfraRisk Lab"
])

with tabs[0]:
    st.header("Executive Overview")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Projects Analyzed", f"{len(df):,}")
    col2.metric("Average Risk Score", f"{df['risk_score'].mean():.2f}")
    col3.metric("Average DSCR", f"{df['dscr'].mean():.2f}")
    col4.metric("Default Rate", f"{df['default_flag'].mean():.2%}")

    st.subheader("Project Portfolio Sample")
    st.dataframe(df.head(20), use_container_width=True)

with tabs[1]:
    st.header("Credit Risk Analytics")

    st.subheader("Risk Category Distribution")
    st.bar_chart(df["risk_category"].value_counts())

    st.subheader("Average Risk Score by Project Type")
    risk_by_type = df.groupby("project_type")["risk_score"].mean().sort_values()
    st.bar_chart(risk_by_type)

    st.subheader("Expected Loss by Project Type")
    loss_by_type = df.groupby("project_type")["expected_loss"].mean().sort_values()
    st.bar_chart(loss_by_type)

with tabs[2]:
    st.header("SHAP Explainability")

    st.write(
        "SHAP explains which variables contribute most to infrastructure credit default predictions."
    )

    if shap_img.exists():
        st.image(Image.open(shap_img), caption="SHAP Summary Plot", use_container_width=True)
    else:
        st.warning("SHAP image not found. Run shap_analysis.py first.")

with tabs[3]:
    st.header("Monte Carlo Stress Testing")

    probability_default = mc["default_flag"].mean()
    avg_dscr = mc["simulated_dscr"].mean()
    min_dscr = mc["simulated_dscr"].min()

    col1, col2, col3 = st.columns(3)

    col1.metric("Simulated PD", f"{probability_default:.2%}")
    col2.metric("Average Simulated DSCR", f"{avg_dscr:.2f}")
    col3.metric("Minimum Simulated DSCR", f"{min_dscr:.2f}")

    if mc_img.exists():
        st.image(Image.open(mc_img), caption="Monte Carlo DSCR Distribution", use_container_width=True)
    else:
        st.warning("Monte Carlo chart not found. Run monte_carlo_engine.py first.")

    st.subheader("Simulation Results Sample")
    st.dataframe(mc.head(20), use_container_width=True)

with tabs[4]:
    st.header("Revenue Forecasting")

    if forecast_img.exists():
        st.image(Image.open(forecast_img), caption="Prophet Revenue Forecast", use_container_width=True)
    else:
        st.warning("Revenue forecast chart not found. Run revenue_forecasting.py first.")

    st.subheader("Forecast Data")
    st.dataframe(
        forecast[["ds", "yhat", "yhat_lower", "yhat_upper"]].tail(12),
        use_container_width=True
    )

with tabs[5]:
    st.header("InfraRisk Lab Simulation")

    project_type = st.selectbox(
        "Select Project Type",
        ["Toll Road", "Airport", "Solar Plant", "Port", "Telecom Tower"]
    )

    leverage = st.slider(
        "Select Debt Leverage (%)",
        min_value=50,
        max_value=90,
        value=75,
        step=5
    )

    if st.button("Run Simulation"):
        result = simulate_event(project_type, leverage)

        col1, col2 = st.columns(2)

        col1.metric(
            "Initial Risk Score",
            result["initial_risk_score"]
        )

        col2.metric(
            "Stressed Risk Score",
            result["stressed_risk_score"]
        )

        st.write(f"Event: {result['event']}")
        st.write(f"Initial Rating: {result['initial_rating']}")
        st.write(f"Stressed Rating: {result['stressed_rating']}")
        st.success(f"AI Recommendation: {result['recommendation']}")