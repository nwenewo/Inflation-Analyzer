# app.py

import streamlit as st
from data import SIMULATED_COSTS, INFLATION_SCENARIOS, calculate_adjusted_expenses
from advice_data import ADVICE
import time

st.set_page_config(page_title="Inflation Analyzer 🇳🇬", layout="centered")
st.title("🧾 Inflation Impact Analyzer for Nigeria")

# Sidebar
with st.sidebar:
    st.header("Your Info")
    income = st.number_input("Monthly Income (₦)", min_value=10000, step=5000, value=150000)
    location = st.selectbox("Location", ["Lagos", "Abuja", "Kano", "Others"])
    lifestyle = st.selectbox("Lifestyle", list(SIMULATED_COSTS.keys()))
    inflation_label = st.selectbox("Inflation Level", list(INFLATION_SCENARIOS.keys()))

# Calculation
inflation_rate = INFLATION_SCENARIOS[inflation_label]
adjusted, total, balance = calculate_adjusted_expenses(income, lifestyle, inflation_rate)

st.subheader("📊 Monthly Cost Breakdown")
st.write(f"**Lifestyle:** {lifestyle.title()} | **Inflation:** {inflation_label}")
for k, v in adjusted.items():
    st.write(f"• {k.title()}: ₦{v:,}")

st.markdown(f"### 💰 Total: ₦{total:,}")
if balance >= 0:
    st.success(f"Surplus: ₦{balance:,}")
else:
    st.error(f"Deficit: ₦{-balance:,}")

# Advice Section (No AI)
if st.button("💡 Get Smart Advice"):
    tips = ADVICE.get(lifestyle.lower(), [])
    with st.spinner("Thinking like a financial advisor..."):
        time.sleep(2)
        st.markdown("### 🤖 Smart Budgeting Tips")
        for tip in tips:
            st.write(f"👉 {tip}")
