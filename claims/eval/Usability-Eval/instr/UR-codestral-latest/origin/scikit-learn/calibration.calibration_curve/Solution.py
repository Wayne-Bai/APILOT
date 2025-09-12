from sklearn.calibration import CalibratedClassifierCV
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import brier_score_loss

# Sample data
X, y = ...  # your data here

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a base classifier
base_clf = LogisticRegression()
base_clf.fit(X_train, y_train)

# Train a calibrated classifier
calibrated_clf = CalibratedClassifierCV(base_clf, cv='prefit')
calibrated_clf.fit(X_train, y_train)

# Compute true and predicted probabilities for a calibration curve
y_prob = calibrated_clf.predict_proba(X_test)[:, 1]
true_prob, bins = brier_score_loss(y_test, y_prob, return_bounds=True)

print("True probabilities:", true_prob)
print("Predicted probabilities:", y_prob)
