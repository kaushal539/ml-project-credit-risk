import streamlit as st
from predict_helper import predict

# Set page title
st.title("Loan Application Input Form")

# Organizing controls with 4 per line
col1, col2, col3, col4 = st.columns(4)

# First row of inputs
with col1:
    age = st.number_input("Age", min_value=18, max_value=100, value=30, step=1)

with col2:
    income = st.number_input("Income", min_value=0, value=50000, step=1000, help="Enter your monthly income")

with col3:
    loan_amount = st.number_input("Loan Amount", min_value=0, value=100000, step=1000)

with col4:
    dpd = st.number_input("Days Past Due (DPD)", min_value=0, value=0, step=1)

# Second row of inputs
col5, col6, col7, col8 = st.columns(4)

with col5:
    loan_tenure_months = st.number_input("Loan Tenure (months)", min_value=1, max_value=360, value=12, step=1)

with col6:
    credit_utilization_ratio = st.slider("Credit Utilization Ratio", min_value=0.0, max_value=1.0, value=0.3, step=0.01)

with col7:
    residence_type = st.selectbox("Residence Type", ["Owned", "Mortgage", "Rented"])

with col8:
    loan_purpose = st.selectbox("Loan Purpose", ["Education", "Home", "Auto", "Personal"])

# Third row of inputs (loan type)
col9, _ , _ , _ = st.columns(4)  # Only one input in this row, the rest are empty
with col9:
    loan_type = st.selectbox("Loan Type", ["Secured", "Unsecured"])

# Display submitted values
st.write("## Submitted Information")
st.write(f"**Age:** {age}")
st.write(f"**Income:** {income}")
st.write(f"**Loan Amount:** {loan_amount}")
st.write(f"**Days Past Due:** {dpd}")
st.write(f"**Loan Tenure:** {loan_tenure_months} months")
st.write(f"**Credit Utilization Ratio:** {credit_utilization_ratio}")
st.write(f"**Residence Type:** {residence_type}")
st.write(f"**Loan Purpose:** {loan_purpose}")
st.write(f"**Loan Type:** {loan_type}")

# Button to trigger the risk calculation
if st.button("Calculate Risk"):
    # Dummy data for missing parameters
    avg_dpd_per_delinquency = dpd  # Assuming dpd represents avg_dpd_per_delinquency
    delinquency_ratio = 0.1  # Placeholder, replace with actual logic
    num_open_accounts = 5  # Placeholder, replace with actual logic

    # Call the predict function
    probability, credit_score, rating = predict(
        age, income, loan_amount, loan_tenure_months, avg_dpd_per_delinquency,
        delinquency_ratio, credit_utilization_ratio, num_open_accounts,
        residence_type, loan_purpose, loan_type
    )

    # Display the prediction results
    st.write(f"**Default Probability:** {probability:.2%}")
    st.write(f"**Credit Score:** {credit_score}")
    st.write(f"**Rating:** {rating}")
