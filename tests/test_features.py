import pandas as pd

from src.features.build_features import build_features
from src.simulation.infrarisk_lab import simulate_event
from src.models.monte_carlo.monte_carlo_engine import run_monte_carlo


def test_feature_engineering_output():
    df = pd.read_csv("data/processed/infrastructure_projects.csv")
    features_df = build_features(df)

    assert "risk_score" in features_df.columns
    assert "expected_loss" in features_df.columns
    assert "default_flag" in features_df.columns
    assert features_df.shape[0] == 10000


def test_risk_score_range():
    df = pd.read_csv("data/processed/infrastructure_projects.csv")
    features_df = build_features(df)

    assert features_df["risk_score"].between(0, 100).all()


def test_expected_loss_non_negative():
    df = pd.read_csv("data/processed/infrastructure_projects.csv")
    features_df = build_features(df)

    assert (features_df["expected_loss"] >= 0).all()


def test_monte_carlo_engine():
    results = run_monte_carlo(n_simulations=1000)

    assert results.shape[0] == 1000
    assert "simulated_dscr" in results.columns
    assert "default_flag" in results.columns


def test_simulation_engine():
    result = simulate_event("Toll Road", 80)

    assert "initial_risk_score" in result
    assert "stressed_risk_score" in result
    assert "recommendation" in result
    assert result["stressed_risk_score"] >= result["initial_risk_score"]