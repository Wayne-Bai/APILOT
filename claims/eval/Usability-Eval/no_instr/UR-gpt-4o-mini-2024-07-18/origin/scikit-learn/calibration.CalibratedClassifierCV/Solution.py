from sklearn.calibration import CalibratedClassifierCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_classification

# Create a synthetic dataset
X, y = make_classification(n_samples=1000, n_features=20, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize a random forest classifier
base_classifier = RandomForestClassifier(n_estimators=100, random_state=42)

# Calibrate the classifier using isotonic regression
calibrated_classifier_isotonic = CalibratedClassifierCV(base_classifier, method='isotonic', cv='prefit')

# Fit the base classifier
base_classifier.fit(X_train, y_train)

# Fit the calibrated classifier
calibrated_classifier_isotonic.fit(X_test, y_test)

# Predict probabilities
prob_isotonic = calibrated_classifier_isotonic.predict_proba(X_test)

# Calibrate the classifier using logistic regression
calibrated_classifier_logistic = CalibratedClassifierCV(base_classifier, method='sigmoid', cv='prefit')

# Fit the calibrated classifier
calibrated_classifier_logistic.fit(X_test, y_test)

# Predict probabilities
prob_logistic = calibrated_classifier_logistic.predict_proba(X_test)
