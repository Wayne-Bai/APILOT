from sklearn.model_selection import train_test_split
from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier
from sklearn.calibration import CalibratedClassifierCV
from sklearn.metrics import brier_score_loss
import matplotlib.pyplot as plt

# Generate a synthetic dataset
X, y = make_classification(n_samples=1000, n_features=20, n_classes=2, random_state=42)

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Instantiate a RandomForest classifier
rf = RandomForestClassifier(n_estimators=100, random_state=42)

# Fit the model
rf.fit(X_train, y_train)

# Calibrate the model with isotonic regression
calibrated_rf_iso = CalibratedClassifierCV(base_estimator=rf, method='isotonic', cv=5)
calibrated_rf_iso.fit(X_train, y_train)

# Calibrate the model with logistic regression
calibrated_rf_log = CalibratedClassifierCV(base_estimator=rf, method='sigmoid', cv=5)
calibrated_rf_log.fit(X_train, y_train)

# Predict probabilities
probs_rf = rf.predict_proba(X_test)[:, 1]
probs_rf_iso = calibrated_rf_iso.predict_proba(X_test)[:, 1]
probs_rf_log = calibrated_rf_log.predict_proba(X_test)[:, 1]

# Calculate Brier scores
brier_rf = brier_score_loss(y_test, probs_rf)
brier_rf_iso = brier_score_loss(y_test, probs_rf_iso)
brier_rf_log = brier_score_loss(y_test, probs_rf_log)

print(f"Brier score (No calibration): {brier_rf:.3f}")
print(f"Brier score (Isotonic calibration): {brier_rf_iso:.3f}")
print(f"Brier score (Logistic calibration): {brier_rf_log:.3f}")

# Plot reliability diagrams
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.hist(probs_rf, bins=10, range=(0, 1), edgecolor='k', alpha=0.7, label='No Calibration')
plt.hist(probs_rf_iso, bins=10, range=(0, 1), edgecolor='k', alpha=0.5, label='Isotonic Calibration')
plt.hist(probs_rf_log, bins=10, range=(0, 1), edgecolor='k', alpha=0.3, label='Logistic Calibration')
plt.title('Probability Histograms')
plt.legend()

plt.subplot(1, 2, 2)
plt.plot([0, 1], [0, 1], 'k:', label='Perfectly calibrated')
plt.plot(probs_rf, brier_score_loss(y_test, probs_rf,))
plt.plot(probs_rf_iso, brier_score_loss(y_test, probs_rf_iso))
plt.plot(probs_rf_log, brier_score_loss(y_test, probs_rf_log))
plt.title('Calibration Plots')
plt.xlabel('Mean Predicted Probability')
plt.ylabel('Fraction of Positives')

plt.tight_layout()
plt.show()
