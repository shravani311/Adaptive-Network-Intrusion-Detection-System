import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler

def load_data(filepath):
    """
    Load raw dataset from txt file and return features (X) and labels (y).
    """
    df = pd.read_csv(filepath, header=None)

    # Column names for KDD99 / NSL-KDD dataset
    columns = [
        'duration','protocol_type','service','flag','src_bytes','dst_bytes',
        'land','wrong_fragment','urgent','hot','num_failed_logins',
        'logged_in','num_compromised','root_shell','su_attempted',
        'num_root','num_file_creations','num_shells','num_access_files',
        'num_outbound_cmds','is_host_login','is_guest_login','count',
        'srv_count','serror_rate','srv_serror_rate','rerror_rate',
        'srv_rerror_rate','same_srv_rate','diff_srv_rate',
        'srv_diff_host_rate','dst_host_count','dst_host_srv_count',
        'dst_host_same_srv_rate','dst_host_diff_srv_rate',
        'dst_host_same_src_port_rate','dst_host_srv_diff_host_rate',
        'dst_host_serror_rate','dst_host_srv_serror_rate',
        'dst_host_rerror_rate','dst_host_srv_rerror_rate',
        'label','difficulty'
    ]

    df.columns = columns

    # Convert label: normal = 0, attack = 1
    df['label'] = df['label'].apply(lambda x: 0 if x == 'normal' else 1)

    # Drop unnecessary column
    X = df.drop(['label', 'difficulty'], axis=1)
    y = df['label']

    return X, y

def preprocess_features(X_train, X_test):
    """
    Encode categorical features and scale numerical features.
    Returns:
    - X_train_scaled
    - X_test_scaled
    - encoders dictionary (for categorical columns)
    - scaler object
    """
    # Identify categorical columns
    categorical_cols = X_train.select_dtypes(include=['object']).columns
    encoders = {}

    # Encode categorical columns
    for col in categorical_cols:
        le = LabelEncoder()
        X_train[col] = le.fit_transform(X_train[col])
        X_test[col] = le.transform(X_test[col])
        encoders[col] = le  # save encoder for later use in app.py

    # Scale numerical features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    return X_train_scaled, X_test_scaled, encoders, scaler

# Quick test block
if __name__ == "__main__":
    X, y = load_data("dataset/KDDTrain+.txt")
    print("Loaded data shape:", X.shape)
    X_train_scaled, X_test_scaled, encoders, scaler = preprocess_features(X, X)
    print("Preprocessing successful!")
    print("Number of categorical columns encoded:", len(encoders))
