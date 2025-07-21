import streamlit as st
import pandas as pd
import yaml
from preprocessing import preprocess_log
from routing import assign_team
import joblib

st.title("🔍 UPI RCA & Team Assignment Agent (Enhanced)")

# Upload or input manually
option = st.radio("Choose input method:", ("Upload CSV", "Manual Input"))

model = joblib.load("classifier.pkl")

# Load escalation matrix
with open("escalation_matrix.yaml", "r") as f:
    escalation_matrix = yaml.safe_load(f)

if option == "Upload CSV":
    uploaded_file = st.file_uploader("Upload transaction metadata (CSV)", type="csv")
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        st.write("Sample Input:", df.head())

        if st.button("Analyze CSV File"):
            df['processed_log'] = df['log'].apply(preprocess_log)
            df['root_cause'] = model.predict(df['processed_log'])
            df['assigned_team'] = df['root_cause'].apply(lambda rc: assign_team(rc, escalation_matrix))

            st.write("Results:", df[['timestamp', 'txn_id', 'log', 'root_cause', 'assigned_team']])

elif option == "Manual Input":
    log_input = st.text_area("Describe the issue (log or message):")

    if st.button("Analyze Manual Input"):
        processed = preprocess_log(log_input)
        root_cause = model.predict([processed])[0]
        assigned_team = assign_team(root_cause, escalation_matrix)

        st.markdown("### Prediction")
        st.write(f"**Root Cause:** {root_cause}")
        st.write(f"**Assigned Team:** {assigned_team}")