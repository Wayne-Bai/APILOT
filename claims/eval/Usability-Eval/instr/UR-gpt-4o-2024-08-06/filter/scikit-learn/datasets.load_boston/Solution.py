from sklearn.datasets import fetch_openml
import pandas as pd

# Load the Boston housing dataset
boston = fetch_openml(name="boston", version=1, as_frame=True)

# Accessing the data and target
X = boston.data
y = boston.target

# Print the first few entries to verify
print("Features:\n", X.head())
print("\nTarget:\n", y.head())
