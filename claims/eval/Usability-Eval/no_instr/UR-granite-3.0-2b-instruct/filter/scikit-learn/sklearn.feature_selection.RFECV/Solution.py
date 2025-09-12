from sklearn.feature_selection import RFE
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier
import numpy as np

# Assuming X is your feature matrix and y is your target variable
X = np.random.rand(100, 10)  # replace with your feature matrix
y = np.random.randint(2, size=100)  # replace with your target variable

# Initialize the model
model = RandomForestClassifier()

# Initialize Recursive Feature Elimination with Cross-Validation
rfe = RFE(model, n_features_to_select=5)  # select 5 features

# Fit the model with cross-validation
scores = cross_val_score(rfe, X, y, cv=5)

# Print the mean cross-validation score
print("Mean Cross-Validation Score: ", np.mean(scores))
