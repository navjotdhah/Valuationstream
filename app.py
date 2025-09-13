import streamlit as st

st.set_page_config(page_title="Company Valuation Tool", page_icon="💰", layout="centered")

st.title("📊 Public Company Valuation Tool")
st.write("Enter financials to estimate intrinsic value per share (DCF model).")

# Inputs
company_name = st.text_input("Company Name")
fcf = st.number_input("Free Cash Flow (most recent year, $)", min_value=0.0, value=1000000000.0, step=1000000.0, format="%.2f")
growth_rate = st.number_input("Growth Rate (next 5 years, %)", value=5.0, step=0.5, format="%.2f")
discount_rate = st.number_input("Discount Rate (%)", value=10.0, step=0.5, format="%.2f")
terminal_growth = st.number_input("Terminal Growth Rate (%)", value=2.0, step=0.5, format="%.2f")
shares = st.number_input("Shares Outstanding", min_value=1.0, value=1000000000.0, step=1000000.0, format="%.0f")

if st.button("Calculate Valuation"):
    # Convert to decimals
    g = growth_rate / 100
    d = discount_rate / 100
    tg = terminal_growth / 100

    # DCF projection (5 years)
    present_value = 0
    for i in range(1, 6):
        projected_fcf = fcf * (1 + g)**i
        discounted_fcf = projected_fcf / (1 + d)**i
        present_value += discounted_fcf

    # Terminal value
    terminal_value = (fcf * (1 + g)**5 * (1 + tg)) / (d - tg)
    discounted_terminal = terminal_value / (1 + d)**5

    # Total value
    intrinsic_value = present_value + discounted_terminal
    value_per_share = intrinsic_value / shares

    st.success(f"💡 Estimated intrinsic value per share: **${value_per_share:,.2f}**")
