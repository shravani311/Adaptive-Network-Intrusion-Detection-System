🚀 Adaptive Network Intrusion Detection System (Adaptive-IDS)

A Machine Learning-based Network Intrusion Detection System (IDS) built using the NSL-KDD dataset, trained with XGBoost, enhanced using SMOTE for class balancing, and deployed using Flask.

The system classifies network traffic as:

✅ NORMAL Traffic

🚨 INTRUSION Detected
It also displays the Attack Probability (%) using adaptive threshold logic.

📌 Project Overview

This project implements an end-to-end supervised machine learning pipeline for detecting malicious network activity.
The system:
Preprocesses raw network traffic features
Handles class imbalance using SMOTE
Trains an XGBoost classifier
Uses probability-based adaptive thresholding
Deploys the trained model via Flask web interface
Users can input 41 network features and receive real-time intrusion predictions.

🧠 Dataset
Dataset Used: NSL-KDD
The NSL-KDD dataset is an improved version of the KDD Cup 1999 dataset and is widely used in intrusion detection research.

Key Characteristics
41 network traffic features
Multiple attack categories
Converted to binary classification:
  0 → Normal
  1 → Intrusion
The difficulty column was removed to avoid data leakage, as it is not available in real-world network traffic.

🛠 Tech Stack
Python
Pandas
NumPy
Scikit-learn
XGBoost
SMOTE (Imbalanced-learn)
Flask
HTML 

⚙️ Machine Learning Pipeline
1️⃣ Data Preprocessing
Multi-class attacks converted to binary labels
Categorical features encoded:
protocol_type
service
flag
Feature scaling using StandardScaler
Proper train-test separation
Important rule followed:
  fit_transform() on training data
  transform() on test data

2️⃣ Class Imbalance Handling
The dataset contains unequal numbers of normal and attack samples.
To address this:
Applied SMOTE (Synthetic Minority Oversampling Technique)
Balanced the training dataset before model training
This improves attack detection capability.

3️⃣ Model Used – XGBoost
Why XGBoost?
Excellent performance on structured/tabular data
Handles non-linearity
Reduces overfitting via boosting
Provides probability predictions
Model Tuning
Increased max_depth
Increased n_estimators
Adjusted scale_pos_weight
Applied custom probability threshold (0.25)
Final accuracy achieved: ~82%

📊 Evaluation Metrics
The model was evaluated using:
Accuracy
Precision
Recall
F1-Score
Confusion Matrix
Most Important Metric in IDS

👉 Recall
Because:
False Negative = Attack missed
Missing an attack is more dangerous than a false alarm

🎯 Adaptive Threshold Logic
Instead of using default threshold (0.5), the system uses:
threshold = 0.25
Prediction logic:
If Attack Probability ≥ 0.25 → INTRUSION
Else → NORMAL
This improves sensitivity to attacks and reduces missed intrusions.

🌐 Deployment – Flask
Application Flow
User Input
↓
Encoding
↓
Scaling
↓
Probability Prediction
↓
Threshold Check
↓
Result Display

The web interface displays:
Clear classification result
Attack probability (%)
Clean, user-friendly layout

📂 Project Structure
adaptive_ids/
│
├── app.py
├── train_model.py
├── preprocess.py
│
├── dataset/
│   ├── KDDTrain+.txt
│   └── KDDTest+.txt
│
├── model/
│   ├── xgb_model.pkl
│   ├── scaler.pkl
│   └── encoders.pkl
│
├── templates/
│   └── index.html
│
├── requirements.txt
└── README.md

▶️ How to Run the Project
1️⃣ Clone the Repository
git clone https://github.com/shravani311/Adaptive-Network-Intrusion-Detection-System.git
cd Adaptive-Network-Intrusion-Detection-System
2️⃣ Install Dependencies
pip install -r requirements.txt
3️⃣ Train the Model (Optional)
python train_model.py
4️⃣ Run the Flask Application
python app.py
Open in browser

🔥 Key Interview Highlights
Binary classification from multi-class dataset
Data leakage prevention
SMOTE-based class balancing
XGBoost ensemble learning
Probability-based adaptive threshold
End-to-end ML deployment using Flask

👩‍💻 Author

Shravani Sakhalkar
Computer Engineering Undergraduate
