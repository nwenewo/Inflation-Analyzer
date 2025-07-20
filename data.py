# data.py

# Sample cost data by lifestyle
SIMULATED_COSTS = {
    "Basic": {
        "food": 30000,
        "transport": 15000,
        "housing": 20000,
        "utilities": 10000,
        "misc": 5000,
    },
    "Moderate": {
        "food": 50000,
        "transport": 25000,
        "housing": 40000,
        "utilities": 15000,
        "misc": 10000,
    },
    "Luxury": {
        "food": 80000,
        "transport": 40000,
        "housing": 80000,
        "utilities": 25000,
        "misc": 30000,
    },
}

# Simulated inflation levels
INFLATION_SCENARIOS = {
    "Low (5%)": 0.05,
    "Medium (15%)": 0.15,
    "High (30%)": 0.30,
    "Extreme (50%)": 0.50,
}

def calculate_adjusted_expenses(income, lifestyle, inflation_rate):
    base = SIMULATED_COSTS[lifestyle]
    adjusted = {k: int(v * (1 + inflation_rate)) for k, v in base.items()}
    total = sum(adjusted.values())
    balance = income - total
    return adjusted, total, balance