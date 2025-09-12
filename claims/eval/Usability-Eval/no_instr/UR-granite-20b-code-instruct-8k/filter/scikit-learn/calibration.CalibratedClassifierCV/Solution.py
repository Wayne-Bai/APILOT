
# Import necessary libraries
from sklearn.calibration import CalibratedClassifierCV
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import make_classification

# Generate a random binary classification problem
X, y = make_classification(n_samples=1000, n_features=20, n_informative=2, n_redundant=10, random_state=42)

# Train a logistic regression model
lr = LogisticRegression()
lr.fit(X, y)

# Perform probability calibration with isotonic regression
calibrated_lr = CalibratedClassifierCV(lr, method='isotonic', cv='prefit')
calibrated_lr.fit(X, y)
