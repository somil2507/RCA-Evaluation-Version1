# 🔍 RCA-Evaluation 
An AI-powered Streamlit application that automates **Root Cause Analysis (RCA)** and assigns issues to the correct internal teams using transaction logs, metadata, and error messages in UPI-based systems.

---

### 🚀 Features

- 🔍 Automatically analyzes transaction logs and metadata
- 🧠 Predicts root cause category (e.g., Bank Down, Timeout, Auth Failure)
- 🧭 Assigns issues to the correct team using an escalation matrix
- 📁 Accepts both **CSV uploads** and **manual text input**
- 🧪 Built with a trained ML model (Scikit-learn)
- 🎨 User-friendly Streamlit UI

---

### 🗂️ Project Structure
RCA_Evaluation/
│
├── app.py # Streamlit frontend
├── preprocessing.py # Log preprocessing logic
├── routing.py # Team assignment rules
├── classifier.pkl # Trained ML classifier (joblib)
├── escalation_matrix.yaml # Escalation logic (root cause → team)
├── metadata_sample.csv # Sample input CSV for testing
├── requirements.txt # Python dependencies

---

### ⚙️ Setup Instructions

## 1. Clone the repository
git clone https://github.com/somil2507/RCA-Evaluation.git
cd RCA-Evaluation

## 2. Install dependencies
pip install -r requirements.txt

## 3. ▶️ How to Run
streamlit run app.py

### 📝 Usage Options
## 🔹 Option 1: Upload CSV
Prepare a CSV with the following columns:
timestamp, txn_id, log

Upload the file using the Streamlit UI

Click "Analyze CSV File"

See predicted root cause and assigned team

✅ Sample file: metadata_sample.csv

## 🔹 Option 2: Manual Input
Enter a transaction error/log like: Bank server not responding

Click "Analyze Manual Input"

View the prediction results on screen****

### 🧠 Example Output
| txn\_id | log                        | root\_cause | assigned\_team       |
| ------- | -------------------------- | ----------- | -------------------- |
| TXN123  | Bank server not responding | bank\_down  | Banking Partner Team |
| TXN124  | Gateway timeout occurred   | timeout     | Gateway Ops Team     |


### 🧰 Built With
🐍 Python
🧠 Scikit-learn (ML model)
📊 Pandas
🗃️ YAML (for routing logic)
🎯 Streamlit (UI)
🛠️ Joblib (model serialization)





