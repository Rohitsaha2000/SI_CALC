import streamlit as st

# Title
st.title("💰 Simple Interest Calculator")

# User Inputs
principal = st.number_input("Enter the Principal (₹)", min_value=0.0, format="%.2f")
rate_of_interest = st.number_input("Enter the Rate of Interest (% per year)", min_value=0.0, format="%.2f")
ty = st.number_input("Enter Time (Years)", min_value=0.0, format="%.2f")
tm = st.number_input("Enter Time (Months)", min_value=0.0, max_value=11.0, step=1.0)

# Calculate Button
if st.button("Calculate"):
    time = ty + (tm / 12)
    simple_interest = (principal * rate_of_interest * time) / 100
    maturity_amount = principal + simple_interest

    st.success(f"Simple Interest: ₹{simple_interest:.2f}")
    st.info(f"Maturity Amount: ₹{maturity_amount:.2f}")