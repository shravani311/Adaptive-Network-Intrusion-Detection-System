import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.utils import class_weight
from preprocess import load_data, preprocess_features
import numpy as np

# ---------------- Load data ----------------
X_train, y_train = load_data("dataset/KDDTrain+.txt")
X_test, y_test = load_data("dataset/KDDTest+.txt")

# ---------------- Preprocess features ----------------
X_train_scaled, X_test_scaled, encoders, scaler = preprocess_features(X_train, X_test)

# ---------------- Compute class weights ----------------
weights = class_weight.compute_class_weight(
    class_weight='balanced',
    classes=np.unique(y_train),
    y=y_train
)
class_weights = {i : weights[i] for i in range(len(weights))}

# ---------------- Train Random Forest ----------------
rf = RandomForestClassifier(
    n_estimators=100,
    random_state=42,
    class_weight=class_weights
)
rf.fit(X_train_scaled, y_train)

# ---------------- Evaluate ----------------
y_pred = rf.predict(X_test_scaled)
print("Random Forest Accuracy:", accuracy_score(y_test, y_pred))
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))

# ---------------- Save model, encoders, scaler ----------------
with open("model/rf_model.pkl", "wb") as f:
    pickle.dump(rf, f)

with open("model/encoders.pkl", "wb") as f:
    pickle.dump(encoders, f)

with open("model/scaler.pkl", "wb") as f:
    pickle.dump(scaler, f)

print("Model, encoders, and scaler saved successfully!")
