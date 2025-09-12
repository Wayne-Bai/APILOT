import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.calibration import calibration_curve
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Load dataset
iris = datasets.load_iris()
X = iris.data
y = iris.target

# Add noisy features to make the problem harder
random_state = np.random.RandomState(seed=42)
n_samples, n_features = X.shape
X = np.c_[X, random_state.randn(n_samples, 200 * n_features)]

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train a RandomForestClassifier
clf = RandomForestClassifier(n_estimators=1000, random_state=42)
clf.fit(X_train, y_train)

# Predict probabilities
y_prob = clf.predict_proba(X_test)
y_prob = y_prob[:, 1]

# Compute true and predicted probabilities for calibration curve
prob_true, prob_pred = calibration_curve(y_test, y_prob, n_bins=10)

# Plot calibration curve
plt.figure(figsize=(10, 10))
plt.plot([0, 1], [0, 1], "k:", label="Perfectly calibrated")
plt.plot(prob_pred, prob_true, "s-", label="RandomForestCalibrated")
plt.xlabel("Predicted probabilities")
plt.ylabel("True probabilities")
plt.title("Calibration plot")
plt.legend(loc="lower right")
plt.show()
