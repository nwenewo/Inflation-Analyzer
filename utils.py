import openai
import streamlit as st

openai.api_key = st.secrets["OPENAI_API_KEY"]

def build_ai_prompt(adjusted_expenses, income):
    prompt = f"Monthly income: ₦{income:,}\nExpenses:\n"
    for k, v in adjusted_expenses.items():
        prompt += f"- {k}: ₦{v:,}\n"
    prompt += "Suggest money-saving tips for this person in Nigeria to stay within budget."
    return prompt

def get_ai_suggestions(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a financial advisor helping Nigerians manage their budget."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=300
    )
    return response["choices"][0]["message"]["content"]