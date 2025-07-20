import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
import joblib

# Updated and more specific training data
training_data = {
    "log": [
        "Bank server not responding",
        "Unable to reach core banking system",
        "Gateway timeout while sending request",
        "Request timed out at gateway",
        "User authentication failed",
        "Incorrect pin entered multiple times",
        "Malformed JSON in payload",
        "Unexpected payload format",
        "Third-party service failed",
        "External service call failed"
    ],
    "label": [
        "bank_down",
        "bank_down",
        "timeout",
        "timeout",
        "auth_failure",
        "auth_failure",
        "invalid_payload",
        "invalid_payload",
        "dependency_error",
        "dependency_error"
    ]
}

# Create a DataFrame
df = pd.DataFrame(training_data)

# Build pipeline using TF-IDF and Logistic Regression
model = make_pipeline(TfidfVectorizer(lowercase=True, stop_words='english'), LogisticRegression())

# Train the model
model.fit(df['log'], df['label'])

# Save the model
joblib.dump(model, "classifier.pkl")
print("✅ Model saved as classifier.pkl")
