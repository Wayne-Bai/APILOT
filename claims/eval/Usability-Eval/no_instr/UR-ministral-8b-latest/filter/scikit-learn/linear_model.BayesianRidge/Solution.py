from sklearn.calibration import CalibratedClassifierCV
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.datasets import make_classification
from sklearn.linear_model import BayesianRidge
from sklearn.model_selection import train_test_split
import numpy as np

# Make a simple dataset
X, y = make_classification(n_samples=1000, n_features=20, random_state=42)

# Encode the target variable to integer labels
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(y)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Fit a Bayesian ridge model
model = BayesianRidge()
model.fit(X_train, y_train)

# Predict on the test set
y_pred = model.predict(X_test)

# Print out the predictions
print("Predictions:", y_pred)

# Convert predictions to original labels
y_pred_labels = label_encoder.inverse_transform(y_pred)

# Calculate accuracy
accuracy = np.mean(y_pred_labels == label_encoder.inverse_transform(y_test))
print("Accuracy:", accuracy)
