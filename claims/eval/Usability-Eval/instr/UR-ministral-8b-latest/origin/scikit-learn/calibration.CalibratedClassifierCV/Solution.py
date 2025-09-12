import numpy as np
from sklearn.calibration import CalibratedClassifierCV
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import StratifiedKFold
from sklearn.datasets import make_classification

# Generate a sample classification dataset
X, y = make_classification(n_samples=1000, n_features=20, random_state=42)

# Define the logistic regression model
logistic_model = LogisticRegression(solver='liblinear')

# Calibrate the predicted probabilities using isotonic regression
calibrated_model = CalibratedClassifierCV(estimator=logistic_model, method='isotonic', cv=5)

# Fit the model to the data
calibrated_model.fit(X, y)

# Predict probabilities for the training data
probabilities = calibrated_model.predict_proba(X)[:, 1]

# Output the probabilities
print(probabilities)
