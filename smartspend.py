import streamlit as st

# Title and description
st.title("SmartSpend 💸")
st.write("""
Welcome to SmartSpend — a simple app to help you decide whether or not to buy something, 
based on your monthly budget and the value you place on the item.
""")

# User inputs
income = st.number_input("Monthly Income (£)", min_value=0)
rent = st.number_input("Monthly Rent + Bills (£)", min_value=0)
necessities = st.number_input("Monthly Necessities (£)", min_value=0)
item_cost = st.number_input("Cost of the Item (£)", min_value=0)
utility_score = st.slider("Utility Score (1–10)", 1, 10)

# Calculate disposable income
disposable_income = income - rent - necessities

# Output logic
if disposable_income <= 0:
    result = "❌ Your disposable income is £0 or less. You may need to adjust your fixed costs before spending on extras."
else:
    percent_of_disposable = item_cost / disposable_income
    utility_to_cost = utility_score / item_cost if item_cost else 0

    if utility_score >= 7 and percent_of_disposable <= 0.25:
        result = "✅ Yes, buy it — it's within your means and brings good value!"
    elif 0.25 < percent_of_disposable <= 0.5 or 4 <= utility_score < 7:
        result = "⚠️ Think again — this might not be the best use of your disposable income."
    else:
        result = "❌ No — it's either too expensive or not valuable enough."

# Display results
if income and rent and necessities and item_cost:
    st.markdown(f"### Result: {result}")
    st.write(f"**Disposable Income:** £{disposable_income:.2f}")
    st.write(f"**% of Disposable Income Spent:** {percent_of_disposable*100:.1f}%")
    st.write(f"**Utility/Cost Ratio:** {utility_to_cost:.2f}")
