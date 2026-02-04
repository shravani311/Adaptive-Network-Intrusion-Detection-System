from flask import Flask, render_template, request
import pickle
import pandas as pd
import numpy as np
from preprocess import load_data

app = Flask(__name__)

# ---------------- Load trained model, encoders, scaler ----------------
with open("model/rf_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("model/encoders.pkl", "rb") as f:
    encoders = pickle.load(f)

with open("model/scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

# Load training columns to maintain order
X_train, _ = load_data("dataset/KDDTrain+.txt")
columns = X_train.columns

# ---------------- Routes ----------------
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Read input
        data = request.form["features"]
        values = data.split(",")

        if len(values) != len(columns):
            return render_template(
                "index.html",
                prediction_text="Error: Number of features mismatch!",
                confidence="N/A"
            )

        # Convert to DataFrame
        sample_df = pd.DataFrame([values], columns=columns)

        # Numeric conversion
        for col in sample_df.columns:
            if col not in encoders:
                sample_df[col] = sample_df[col].astype(float)

        # Encode categorical safely
        for col, le in encoders.items():
            val = sample_df[col][0]
            if val not in le.classes_:
                val = le.classes_[0]  # fallback
            sample_df[col][0] = val
            sample_df[col] = le.transform(sample_df[col])

        # Scale features
        sample_scaled = scaler.transform(sample_df)

        # Predict probability
        prob = model.predict_proba(sample_scaled)[0][1]  # probability for intrusion
        threshold = 0.60  # calibrated threshold

        if prob >= threshold:
            result = "INTRUSION Detected"
        else:
            result = "NORMAL Traffic"

        return render_template(
            "index.html",
            prediction_text=result,
            confidence=round(prob * 100, 2)
        )

    except Exception as e:
        return render_template(
            "index.html",
            prediction_text=f"Error: {str(e)}",
            confidence="N/A"
        )

if __name__ == "__main__":
    app.run(debug=True)
