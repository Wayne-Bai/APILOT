import pandas as pd
from sklearn.datasets import fetch_openml

# Fetching the dataset from openml by name
boston = fetch_openml(name='boston', version=1)
X = pd.DataFrame(data=boston['data'], columns=boston['feature_names'])
y = boston['target']

# Display the first few rows of the data
print(X.head())
print(y[:5])
