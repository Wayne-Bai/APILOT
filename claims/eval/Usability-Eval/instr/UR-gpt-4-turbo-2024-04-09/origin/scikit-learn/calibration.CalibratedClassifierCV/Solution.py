from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.calibration import CalibratedClassifierCV
from sklearn.metrics import brier_score_loss

# Generate synthetic data
X, y = make_classification(n_samples=1000, n_features=20, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train an SVM classifier
svm = SVC(probability=False, random_state=42)
svm.fit(X_train, y_train)

# Calibrate classifier using isotonic regression
calibrated_isotonic = CalibratedClassifierCV(base_estimator=svm, method='isotonic')
calibrated_isotonic.fit(X_train, y_train)
prob_pos_isotonic = calibrated_isotonic.predict_proba(X_test)[:, 1]

# Calibrate classifier using logistic regression
calibrated_logistic = CalibratedClassifierCV(base_estimator=svm, method='sigmoid')
calibrated_logistic.fit(X_train, y_train)
prob_pos_logistic = calibrated_logistic.predict_proba(X_test)[:, 1]

# Brier score evaluation
brier_score_isotonic = brier_score_loss(y_test, prob_pos_isotonic)
brier_score_logistic = brier_score_loss(y_test, prob_pos_logistic)

print(f"Brier score with Isotonic Calibration: {brier_score_isotonic:.4f}")
print(f"Brier score with Logistic Calibration: {brier_score_logistic:.4f}")
