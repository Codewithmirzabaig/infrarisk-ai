import sys
from pathlib import Path

import pandas as pd
import streamlit as st

ROOT_DIR = Path(__file__).resolve().parents[2]
sys.path.append(str(ROOT_DIR))

from src.simulation.infrarisk_lab import simulate_event, list_scenarios


st.set_page_config(
    page_title="InfraRisk AI",
    page_icon="🏗️",
    layout="wide"
)

st.title("🏗️ InfraRisk AI")
st.subheader("Infrastructure Finance Risk Intelligence Platform")


try:
    df = pd.read_csv(
        ROOT_DIR / "data" / "processed" / "infrastructure_features.csv"
    )
except FileNotFoundError:
    st.error("infrastructure_features.csv not found. Run feature engineering first.")
    st.stop()


st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Select Module",
    [
        "Executive Overview",
        "Credit Risk",
        "Monte Carlo",
        "Revenue Forecasting",
        "InfraRisk Lab"
    ]
)


if page == "Executive Overview":

    st.header("Executive Overview")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Projects", f"{len(df):,}")
    col2.metric("Avg Risk Score", f"{df['risk_score'].mean():.2f}")
    col3.metric("Avg DSCR", f"{df['dscr'].mean():.2f}")
    col4.metric("Default Rate", f"{df['default_flag'].mean():.2%}")

    st.markdown("---")

    st.subheader("Project Portfolio Sample")

    st.dataframe(
        df.head(20),
        use_container_width=True
    )


elif page == "Credit Risk":

    st.header("Credit Risk Analytics")

    st.subheader("Risk Category Distribution")
    st.bar_chart(df["risk_category"].value_counts())

    st.subheader("Average Risk Score by Project Type")

    risk_by_type = (
        df.groupby("project_type")["risk_score"]
        .mean()
        .sort_values()
    )

    st.bar_chart(risk_by_type)

    st.subheader("Expected Loss by Project Type")

    loss_by_type = (
        df.groupby("project_type")["expected_loss"]
        .mean()
        .sort_values()
    )

    st.bar_chart(loss_by_type)


elif page == "Monte Carlo":

    st.header("Monte Carlo Stress Testing")

    mc_file = (
        ROOT_DIR
        / "data"
        / "processed"
        / "monte_carlo_results.csv"
    )

    if mc_file.exists():

        mc = pd.read_csv(mc_file)

        col1, col2, col3 = st.columns(3)

        col1.metric(
            "Probability of Default",
            f"{mc['default_flag'].mean():.2%}"
        )

        col2.metric(
            "Average DSCR",
            f"{mc['simulated_dscr'].mean():.2f}"
        )

        col3.metric(
            "Worst DSCR",
            f"{mc['simulated_dscr'].min():.2f}"
        )

        st.subheader("Simulation Results")
        st.dataframe(mc.head(20), use_container_width=True)

        chart_path = (
            ROOT_DIR
            / "reports"
            / "figures"
            / "monte_carlo_dscr_distribution.png"
        )

        if chart_path.exists():
            st.image(str(chart_path), caption="Monte Carlo DSCR Distribution")

    else:
        st.warning("Run monte_carlo_engine.py first.")


elif page == "Revenue Forecasting":

    st.header("Revenue Forecasting")

    forecast_file = (
        ROOT_DIR
        / "data"
        / "processed"
        / "revenue_forecast.csv"
    )

    if forecast_file.exists():

        forecast = pd.read_csv(forecast_file)

        cols = [
            "ds",
            "yhat",
            "yhat_lower",
            "yhat_upper"
        ]

        available_cols = [
            c for c in cols
            if c in forecast.columns
        ]

        st.dataframe(
            forecast[available_cols].tail(20),
            use_container_width=True
        )

        chart_path = (
            ROOT_DIR
            / "reports"
            / "figures"
            / "revenue_forecast.png"
        )

        if chart_path.exists():
            st.image(str(chart_path), caption="Revenue Forecast")

    else:
        st.warning("Run revenue_forecasting.py first.")


elif page == "InfraRisk Lab":

    st.header("InfraRisk Lab Simulation")

    mode = st.selectbox(
        "Game Mode",
        [
            "Single Deal",
            "Portfolio Manager",
            "Crisis Manager",
            "Deal Structurer"
        ]
    )

    project_type = st.selectbox(
        "Project Type",
        [
            "Toll Road",
            "Airport",
            "Solar Plant",
            "Port",
            "Telecom Tower"
        ]
    )

    leverage = st.slider(
        "Debt Leverage %",
        min_value=50,
        max_value=90,
        value=75,
        step=5
    )

    with st.expander("Available Stress Scenarios"):
        scenarios = list_scenarios()
        st.write(f"Total scenarios available: {len(scenarios)}")
        st.write(scenarios)

    if st.button("Run Simulation"):

        result = simulate_event(
            project_type,
            leverage,
            mode
        )

        col1, col2, col3 = st.columns(3)

        col1.metric(
            "Initial Risk Score",
            result["initial_risk_score"]
        )

        col2.metric(
            "Stressed Risk Score",
            result["stressed_risk_score"]
        )

        col3.metric(
            "Simulation Score",
            result["game_score"]
        )

        st.markdown("---")

        st.write(f"**Game Mode:** {result['mode']}")
        st.write(f"**Event:** {result['event']}")
        st.write(f"**Initial Rating:** {result['initial_rating']}")
        st.write(f"**Stressed Rating:** {result['stressed_rating']}")

        st.success(
            f"AI Recommendation: {result['recommendation']}"
        )


st.markdown("---")
st.caption(
    "InfraRisk AI | Credit Risk | Monte Carlo | Forecasting | Infrastructure Simulation"
)