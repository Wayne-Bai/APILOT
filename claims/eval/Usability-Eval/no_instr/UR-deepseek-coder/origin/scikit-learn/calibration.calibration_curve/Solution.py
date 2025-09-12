import numpy as np
import matplotlib.pyplot as plt
from sklearn.calibration import calibration_curve
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Generate a binary classification dataset
X, y = make_classification(n_samples=1000, n_features=20, n_informative=2, n_redundant=10, random_state=42)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train a binary classifier (RandomForestClassifier in this case)
classifier = RandomForestClassifier(n_estimators=100, random_state=42)
classifier.fit(X_train, y_train)

# Predict probabilities for the test set
y_prob = classifier.predict_proba(X_test)[:, 1]

# Compute the calibration curve
true_prob, pred_prob = calibration_curve(y_test, y_prob, n_bins=10)

# Plot the calibration curve
plt.figure(figsize=(10, 6))
plt.plot(pred_prob, true_prob, marker='o', linewidth=1, label='Calibration Curve')
plt.plot([0, 1], [0, 1], linestyle='--', label='Perfectly Calibrated')
plt.xlabel('Predicted Probability')
plt.ylabel('True Probability in each bin')
plt.title('Calibration Curve')
plt.legend()
plt.show()
