# data.py

SIMULATED_COSTS = {
    "basic": {
        "rent": 150000,
        "food": 40000,
        "transport": 10000,
        "utilities": 8000,
        "misc": 5000
    },
    "moderate": {
        "rent": 250000,
        "food": 60000,
        "transport": 15000,
        "utilities": 10000,
        "misc": 10000
    },
    "luxury": {
        "rent": 2000000,
        "food": 100000,
        "transport": 25000,
        "utilities": 20000,
        "misc": 20000
    }
}

INFLATION_SCENARIOS = {
    "Low (5%)": 1.05,
    "Medium (15%)": 1.15,
    "High (30%)": 1.30
}

def calculate_adjusted_expenses(income, lifestyle, inflation_rate):
    base_costs = SIMULATED_COSTS[lifestyle]
    adjusted_costs = {k: int(v * inflation_rate) for k, v in base_costs.items()}
    total = sum(adjusted_costs.values())
    balance = income - total
    return adjusted_costs, total, balance
