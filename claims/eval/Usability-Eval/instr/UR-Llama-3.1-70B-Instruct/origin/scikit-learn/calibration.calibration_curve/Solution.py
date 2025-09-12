from sklearn.calibration import CalibrationDisplay
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import numpy as np

# Generate a binary classification data
X, y = make_classification(n_samples=1000, n_features=20, n_informative=15, n_redundant=5, n_repeated=0, n_classes=2, n_clusters_per_class=1, random_state=42)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a logistic regression model on the data
model = LogisticRegression(random_state=42)
model.fit(X_train, y_train)

# Predict the probabilities for the testing data
y_pred_proba = model.predict_proba(X_test)[:, 1]

# Create bins for the calibration curve
n_bins = 10
bins = np.linspace(0, 1, n_bins)

# Create a calibration display
display = CalibrationDisplay.from_predictions(y_test, y_pred_proba, n_bins=n_bins, ax=None)

# Draw the calibration plot
plt.figure(figsize=(10, 8))
display.plot()
plt.show()
