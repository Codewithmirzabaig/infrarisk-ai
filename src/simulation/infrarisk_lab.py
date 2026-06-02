import random


GAME_MODES = [
    "Single Deal",
    "Portfolio Manager",
    "Crisis Manager",
    "Deal Structurer",
]


EVENTS = {
    "Construction Delay": {
        "impact": 15,
        "recommendation": "Negotiate EPC liquidated damages and increase contingency reserve.",
    },
    "Inflation Shock": {
        "impact": 12,
        "recommendation": "Review tariff escalation clause and hedge input cost exposure.",
    },
    "Sovereign Downgrade": {
        "impact": 18,
        "recommendation": "Activate political risk monitoring and reduce country concentration.",
    },
    "Traffic Demand Collapse": {
        "impact": 20,
        "recommendation": "Reforecast demand, draw DSRA if needed, and negotiate covenant waiver.",
    },
    "Interest Rate Spike": {
        "impact": 10,
        "recommendation": "Refinance fixed-rate tranche or use interest-rate swap.",
    },
    "Regulatory Change": {
        "impact": 14,
        "recommendation": "Review concession agreement and trigger change-in-law protection.",
    },
    "FX Depreciation": {
        "impact": 16,
        "recommendation": "Use FX hedging or restructure debt into local currency.",
    },
    "Commodity Price Shock": {
        "impact": 13,
        "recommendation": "Renegotiate supply contracts and hedge commodity exposure.",
    },
    "Pandemic Demand Shock": {
        "impact": 25,
        "recommendation": "Seek covenant waivers and preserve liquidity through DSRA drawdown.",
    },
    "Climate Event": {
        "impact": 22,
        "recommendation": "Activate insurance claims and update climate resilience assumptions.",
    },
    "Contractor Default": {
        "impact": 24,
        "recommendation": "Trigger performance bond and replace EPC contractor.",
    },
    "Land Acquisition Delay": {
        "impact": 17,
        "recommendation": "Escalate government approvals and revise construction schedule.",
    },
    "Tariff Freeze": {
        "impact": 19,
        "recommendation": "Invoke concession protections and renegotiate tariff indexation.",
    },
    "Debt Refinancing Failure": {
        "impact": 21,
        "recommendation": "Extend tenor, reduce leverage, and negotiate lender support.",
    },
    "Port Congestion": {
        "impact": 11,
        "recommendation": "Increase operational capacity and optimize logistics scheduling.",
    },
    "Power Offtaker Weakness": {
        "impact": 18,
        "recommendation": "Seek sovereign guarantee or diversify offtaker exposure.",
    },
    "Technology Failure": {
        "impact": 15,
        "recommendation": "Increase maintenance reserve and validate technology readiness.",
    },
    "Political Protest": {
        "impact": 14,
        "recommendation": "Strengthen stakeholder engagement and monitor political risk.",
    },
    "Liquidity Shortfall": {
        "impact": 20,
        "recommendation": "Draw reserve accounts and request sponsor support.",
    },
    "Sponsor Credit Deterioration": {
        "impact": 16,
        "recommendation": "Require additional guarantees and enhanced reporting covenants.",
    },
}


PROJECT_BASE_RISK = {
    "Toll Road": 45,
    "Airport": 50,
    "Solar Plant": 35,
    "Port": 42,
    "Telecom Tower": 30,
}


MODE_RISK_MULTIPLIER = {
    "Single Deal": 1.00,
    "Portfolio Manager": 1.10,
    "Crisis Manager": 1.25,
    "Deal Structurer": 0.95,
}


def calculate_initial_risk(project_type: str, leverage: float, mode: str = "Single Deal") -> float:
    base_risk = PROJECT_BASE_RISK.get(project_type, 45)
    leverage_penalty = max(0, (leverage - 70) * 0.8)
    mode_multiplier = MODE_RISK_MULTIPLIER.get(mode, 1.0)
    return min((base_risk + leverage_penalty) * mode_multiplier, 100)


def assign_rating(risk_score: float) -> str:
    if risk_score < 35:
        return "A / Low Risk"
    if risk_score < 55:
        return "BBB / Moderate Risk"
    if risk_score < 75:
        return "BB / High Risk"
    return "B / Distressed"


def calculate_game_score(initial_risk: float, stressed_risk: float, leverage: float) -> int:
    risk_penalty = stressed_risk * 6
    leverage_bonus = max(0, 90 - leverage) * 3
    score = 1000 - risk_penalty + leverage_bonus
    return int(max(min(score, 1000), 0))


def simulate_event(project_type: str, leverage: float, mode: str = "Single Deal") -> dict:
    initial_risk = calculate_initial_risk(project_type, leverage, mode)

    event_name = random.choice(list(EVENTS.keys()))
    event = EVENTS[event_name]

    stressed_risk = min(initial_risk + event["impact"], 100)
    score = calculate_game_score(initial_risk, stressed_risk, leverage)

    return {
        "mode": mode,
        "project_type": project_type,
        "leverage": leverage,
        "event": event_name,
        "initial_risk_score": round(initial_risk, 2),
        "stressed_risk_score": round(stressed_risk, 2),
        "initial_rating": assign_rating(initial_risk),
        "stressed_rating": assign_rating(stressed_risk),
        "game_score": score,
        "recommendation": event["recommendation"],
    }


def list_scenarios() -> list:
    return list(EVENTS.keys())


def main() -> None:
    result = simulate_event("Toll Road", 80, "Portfolio Manager")

    print("InfraRisk Lab Simulation")
    print("-" * 40)

    for key, value in result.items():
        print(f"{key}: {value}")

    print(f"\nTotal Scenarios Available: {len(EVENTS)}")


if __name__ == "__main__":
    main()