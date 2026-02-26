🚀 Adaptive Network Intrusion Detection System (Adaptive-IDS)

A Machine Learning-based Intrusion Detection System (IDS) built using the NSL-KDD dataset, trained with XGBoost, enhanced using SMOTE for class balancing, and deployed using Flask.

This system classifies network traffic as:

✅ NORMAL Traffic

🚨 INTRUSION Detected

It also provides attack probability with adaptive threshold detection.

📌 Project Overview

This project implements a supervised ML-based Network Intrusion Detection System that:

Performs data preprocessing

Handles class imbalance using SMOTE

Trains an XGBoost classifier

Uses probability-based adaptive thresholding

Deploys the model via Flask web interface

The system allows users to input 41 network features and get real-time intrusion predictions.

🧠 Dataset Used

Dataset: NSL-KDD

The NSL-KDD dataset is an improved version of the KDD Cup 1999 dataset and is widely used for intrusion detection research.

Key Features:

41 network traffic features

Multiple attack categories

Converted to Binary Classification:

0 → Normal

1 → Intrusion

We removed the difficulty column to prevent data leakage since it is not available in real-world network traffic.

⚙️ Tech Stack

Python

Pandas

NumPy

Scikit-learn

XGBoost

SMOTE (Imbalanced-learn)

Flask

HTML/CSS

🔄 Machine Learning Pipeline
1️⃣ Data Preprocessing

Label conversion (multi-class → binary)

Encoding categorical features (protocol_type, service, flag)

Feature scaling using StandardScaler

Train-test split

Important:

fit_transform() on training data

transform() on test data

2️⃣ Class Imbalance Handling

Used SMOTE (Synthetic Minority Oversampling Technique) to balance attack and normal samples.

Before SMOTE:

[67343 58630]

After SMOTE:

[67343 67343]
3️⃣ Model Used: XGBoost

Why XGBoost?

Handles non-linearity

High performance on structured/tabular data

Robust against overfitting

Supports probability prediction

Model tuned using:

max_depth

n_estimators

scale_pos_weight

Adaptive threshold (0.25)

4️⃣ Evaluation Metrics

Example Output:

Accuracy: 0.82

Precision (Attack): 0.97
Recall (Attack): 0.71
F1-score: 0.82

Most important metric in IDS:
👉 Recall (to reduce False Negatives)

False Negative = Attack missed (dangerous)

🎯 Adaptive Threshold Detection

Instead of using default 0.5 threshold:

prob = model.predict_proba(sample)[0][1]
threshold = 0.25

If:

prob ≥ 0.25 → INTRUSION
else → NORMAL

This improves attack sensitivity.

🌐 Deployment (Flask)

Flow:

User Input
↓
Preprocessing (Encoding + Scaling)
↓
Probability Prediction
↓
Threshold Check
↓
Result Display

The UI provides:

Clear classification result

Attack probability percentage

Clean readable layout

📂 Project Structure
adaptive_ids/
│
├── app.py
├── train_model.py
├── preprocess.py
├── dataset/
├── model/
│   ├── xgb_model.pkl
│   ├── scaler.pkl
│   └── encoders.pkl
├── templates/
│   └── index.html
├── requirements.txt
└── README.md
▶️ How to Run
1️⃣ Clone Repository
git clone https://github.com/shravani311/Adaptive-Network-Intrusion-Detection-System.git
cd Adaptive-Network-Intrusion-Detection-System
2️⃣ Install Dependencies
pip install -r requirements.txt
3️⃣ Train Model (Optional)
python train_model.py
4️⃣ Run Flask App
python app.py

Open browser:

http://127.0.0.1:5000/
🔥 Key Interview Highlights

Binary classification from multi-class dataset

Data leakage prevention

SMOTE-based class balancing

XGBoost ensemble learning

Probability-based adaptive threshold

End-to-end deployment using Flask

🏆 Author

Shravani Sakhalkar
Computer Engineering Undergraduate
Machine Learning & Cybersecurity Enthusiast
