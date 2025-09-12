# Import necessary modules from scikit-learn
from sklearn.cross_decomposition import PLSRegression
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_regression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
import numpy as np

# Generate synthetic regression dataset
X, y = make_regression(n_samples=100, n_features=10, noise=0.1, random_state=42)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize features by removing the mean and scaling to unit variance
scaler = StandardScaler()

# Define the Partial Least Squares Regression model
# The n_components can be adjusted based on the desired number of latent variables
pls = PLSRegression(n_components=2)

# Create a pipeline to standardize features and apply PLS regression
pipeline = make_pipeline(scaler, pls)

# Fit model to training data
pipeline.fit(X_train, y_train)

# Make predictions on the test set
y_pred = pipeline.predict(X_test)

# Evaluate the model (e.g., using R^2 score)
r2_score = pipeline.score(X_test, y_test)

# Output the predicted values and the R^2 score for the model
print("Predicted values:", y_pred)
print("R^2 score:", r2_score)
