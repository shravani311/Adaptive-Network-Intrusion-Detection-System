from preprocess import load_data, preprocess_features

X_train, y_train = load_data("dataset/KDDTrain+.txt")
X_test, y_test = load_data("dataset/KDDTest+.txt")

X_train, X_test = preprocess_features(X_train, X_test)

# Convert to normal Python floats
sample = [float(x) for x in X_test[0]]
print(sample)
