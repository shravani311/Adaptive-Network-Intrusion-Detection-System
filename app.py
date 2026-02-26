from flask import Flask, render_template, request
import pickle
import pandas as pd
from preprocess import load_data

app = Flask(__name__)

# ---------------- Load trained model ----------------
with open("model/xgb_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("model/encoders.pkl", "rb") as f:
    encoders = pickle.load(f)

with open("model/scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

# Load feature column order
X_train, _ = load_data("dataset/KDDTrain+.txt")
columns = X_train.columns


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    try:
        # ---------------- Read Input ----------------
        data = request.form["features"]
        values = [v.strip() for v in data.split(",")]

        # ---------------- Feature Count Check ----------------
        if len(values) != len(columns):
            return render_template(
                "index.html",
                prediction_text="Error: Exactly 41 features required (label & difficulty NOT allowed).",
                confidence="N/A"
            )

        # ---------------- Create DataFrame ----------------
        sample_df = pd.DataFrame([values], columns=columns)

        # ---------------- Convert Numeric Columns ----------------
        for col in sample_df.columns:
            if col not in encoders:
                sample_df[col] = sample_df[col].astype(float)

        # ---------------- Encode Categorical Columns (SAFE) ----------------
        for col, le in encoders.items():
            value = sample_df[col][0]

            # Strict validation (no silent replacement)
            if value not in le.classes_:
                return render_template(
                    "index.html",
                    prediction_text=f"Error: Unknown category '{value}' in column '{col}'",
                    confidence="N/A"
                )

            sample_df[col] = le.transform(sample_df[col])

        # ---------------- Scaling ----------------
        sample_scaled = scaler.transform(sample_df)

        # ---------------- Probability Prediction ----------------
        prob = model.predict_proba(sample_scaled)[0][1]  # intrusion probability

        threshold = 0.25  # tuned threshold

        if prob >= threshold:
            result = "INTRUSION Detected"
        else:
            result = "NORMAL Traffic"

        return render_template(
            "index.html",
            prediction_text=result,
            confidence=f"Attack Probability: {round(prob * 100, 2)}%"
        )

    except Exception as e:
        return render_template(
            "index.html",
            prediction_text=f"Error: {str(e)}",
            confidence="N/A"
        )


if __name__ == "__main__":
    app.run(debug=True)