import numpy as np
from sklearn.calibration import CalibrationDisplay
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.calibration import calibration_curve

# Generate synthetic data
X, y = make_classification(n_samples=1000, n_features=20, 
                           n_informative=2, n_redundant=10,
                           random_state=42)

# Split data into train/test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a classifier model
model = LogisticRegression(max_iter=1000)

# Train the model
model.fit(X_train, y_train)

# Predict probabilities on the test set
prob_pos = model.predict_proba(X_test)[:, 1]

# Compute true and predicted probabilities for calibration curve
# The method by default divides the [0,1] interval into 5 bins
true_prob, pred_prob = calibration_curve(y_test, prob_pos, n_bins=5)

# Display the calibration curve
print("True probabilities:", true_prob)
print("Predicted probabilities:", pred_prob)
