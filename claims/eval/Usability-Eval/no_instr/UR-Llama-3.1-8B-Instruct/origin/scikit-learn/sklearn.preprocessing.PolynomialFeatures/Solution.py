# Import necessary libraries from scikit-learn
from sklearn.preprocessing import PolynomialFeatures

# Import numpy for numerical operations
import numpy as np

# Define input feature matrix
X = np.array([[2, 3], [4, 5], [6, 7]])

# Specify the desired degree
degree = 2

# Create a PolynomialFeatures instance
poly_features = PolynomialFeatures(degree=degree)

# Fit the instance to the feature matrix and get the polynomial features
X_poly = poly_features.fit_transform(X)

# Print the original feature matrix
print("Original Feature Matrix:")
print(X)

# Print the polynomial feature matrix
print("\nPolynomial Feature Matrix:")
print(X_poly)

# Create a DataFrame to view the polynomial features
import pandas as pd
df = pd.DataFrame(X_poly, columns=poly_features.get_feature_names_out())
print("\nPolynomial Features (Dataframe):")
print(df)

