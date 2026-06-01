import random


EVENTS = {
    "Construction Delay": {
        "impact": 15,
        "recommendation": "Negotiate EPC liquidated damages and increase contingency reserve."
    },
    "Inflation Shock": {
        "impact": 12,
        "recommendation": "Review tariff escalation clause and hedge input cost exposure."
    },
    "Sovereign Downgrade": {
        "impact": 18,
        "recommendation": "Activate political risk monitoring and reduce country concentration."
    },
    "Traffic Demand Collapse": {
        "impact": 20,
        "recommendation": "Reforecast demand, draw DSRA if needed, and negotiate covenant waiver."
    },
    "Interest Rate Spike": {
        "impact": 10,
        "recommendation": "Refinance fixed-rate tranche or use interest-rate swap."
    },
    "Regulatory Change": {
        "impact": 14,
        "recommendation": "Review concession agreement and trigger change-in-law protection."
    },
}


PROJECT_BASE_RISK = {
    "Toll Road": 45,
    "Airport": 50,
    "Solar Plant": 35,
    "Port": 42,
    "Telecom Tower": 30,
}


def calculate_initial_risk(project_type: str, leverage: float) -> float:
    base_risk = PROJECT_BASE_RISK.get(project_type, 45)
    leverage_penalty = max(0, (leverage - 70) * 0.8)
    return min(base_risk + leverage_penalty, 100)


def assign_rating(risk_score: float) -> str:
    if risk_score < 35:
        return "A / Low Risk"
    if risk_score < 55:
        return "BBB / Moderate Risk"
    if risk_score < 75:
        return "BB / High Risk"
    return "B / Distressed"


def simulate_event(project_type: str, leverage: float) -> dict:
    initial_risk = calculate_initial_risk(project_type, leverage)

    event_name = random.choice(list(EVENTS.keys()))
    event = EVENTS[event_name]

    stressed_risk = min(initial_risk + event["impact"], 100)

    result = {
        "project_type": project_type,
        "leverage": leverage,
        "event": event_name,
        "initial_risk_score": round(initial_risk, 2),
        "stressed_risk_score": round(stressed_risk, 2),
        "initial_rating": assign_rating(initial_risk),
        "stressed_rating": assign_rating(stressed_risk),
        "recommendation": event["recommendation"],
    }

    return result


def main() -> None:
    print("InfraRisk Lab Simulation")
    print("-" * 40)

    project_type = "Toll Road"
    leverage = 80

    result = simulate_event(project_type, leverage)

    for key, value in result.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()