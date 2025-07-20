import streamlit as st
from data import SIMULATED_COSTS, INFLATION_SCENARIOS, calculate_adjusted_expenses
from utils import build_ai_prompt, get_ai_suggestions

st.set_page_config(page_title="Inflation Impact Analyzer", layout="centered")
st.title("🧾 Inflation Impact Analyzer for Nigeria")

# Sidebar Inputs
with st.sidebar:
    st.header("User Info")
    income = st.number_input("Monthly Income (₦)", min_value=10000, step=5000, value=150000)
    location = st.selectbox("Your Location", ["Lagos", "Abuja", "Kano", "Others"])
    lifestyle = st.selectbox("Lifestyle", list(SIMULATED_COSTS.keys()))
    inflation_label = st.selectbox("Inflation Level", list(INFLATION_SCENARIOS.keys()))

# Calculate inflation-adjusted expenses
inflation_rate = INFLATION_SCENARIOS[inflation_label]
adjusted, total, balance = calculate_adjusted_expenses(income, lifestyle, inflation_rate)

# Show Output
st.subheader("📊 Monthly Cost Breakdown")
st.write(f"**Lifestyle:** {lifestyle} | **Inflation:** {inflation_label}")
for k, v in adjusted.items():
    st.write(f"• {k.title()}: ₦{v:,}")

st.markdown(f"### 💰 Total: ₦{total:,}")
if balance >= 0:
    st.success(f"Surplus: ₦{balance:,}")
else:
    st.error(f"Deficit: ₦{-balance:,}")

# AI Financial Advice
prompt = build_ai_prompt(adjusted, income)
if st.button("💡 Get AI Advice"):
    suggestion = get_ai_suggestions(prompt)
    st.markdown("### 🤖 AI Financial Tips")
    st.info(suggestion)