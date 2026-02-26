import pickle
import numpy as np
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from xgboost import XGBClassifier
from imblearn.over_sampling import SMOTE
from preprocess import load_data, preprocess_features

# ---------------- Load data ----------------
X_train, y_train = load_data("dataset/KDDTrain+.txt")
X_test, y_test = load_data("dataset/KDDTest+.txt")

# ---------------- Preprocess ----------------
X_train_scaled, X_test_scaled, encoders, scaler = preprocess_features(X_train, X_test)

# ---------------- Apply SMOTE ----------------
sm = SMOTE(random_state=42)
X_train_res, y_train_res = sm.fit_resample(X_train_scaled, y_train)

print("Before SMOTE:", np.bincount(y_train))
print("After SMOTE:", np.bincount(y_train_res))

# ---------------- Tuned XGBoost ----------------
model = XGBClassifier(
    n_estimators=350,      # increased trees
    learning_rate=0.05,    # smaller learning rate (more stable)
    max_depth=8,           # deeper trees
    scale_pos_weight=1.2,  # slight push towards attack class
    subsample=0.8,
    colsample_bytree=0.8,
    random_state=42,
    eval_metric='logloss'
)

model.fit(X_train_res, y_train_res)

# ---------------- Threshold tuning ----------------
y_probs = model.predict_proba(X_test_scaled)[:, 1]

threshold = 0.25   # LOWER threshold to increase recall
y_pred = (y_probs > threshold).astype(int)

# ---------------- Evaluation ----------------
print("Accuracy:", accuracy_score(y_test, y_pred))
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))

# ---------------- Save ----------------
with open("model/xgb_model.pkl", "wb") as f:
    pickle.dump(model, f)

with open("model/encoders.pkl", "wb") as f:
    pickle.dump(encoders, f)

with open("model/scaler.pkl", "wb") as f:
    pickle.dump(scaler, f)

print("Tuned Model Saved Successfully!")