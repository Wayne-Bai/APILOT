from sklearn.calibration import CalibratedClassifierCV
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import IsotonicRegression
from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split

# Load dataset
data = fetch_openml('adult', as_frame=True)
X, y = data.data, data.target

# Split the data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create instance of logistic regression
logreg = LogisticRegression()

# Create instance of Isotonic Regression for calibration
isotonic = IsotonicRegression()

# Create a CalibratedClassifierCV with Isotonic Regression
calibrated_isotonic = CalibratedClassifierCV(base_estimator=logreg, method='isotonic')
calibrated_logit = CalibratedClassifierCV(base_estimator=logreg, method='logit')

# Fit the models
calibrated_isotonic.fit(X_train, y_train)
calibrated_logit.fit(X_train, y_train)

# Predict probabilities
probabilities_isotonic = calibrated_isotonic.predict_proba(X_test)
probabilities_logit = calibrated_logit.predict_proba(X_test)
