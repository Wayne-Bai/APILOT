import numpy as np
from sklearn.datasets import load_boston

boston = load_boston()

print(boston.keys())

# This will print all the keys of the boston dictionary, including the target variable and feature names.

print(boston.data.shape)

# This will print the shape of the data, which is the number of samples and the number of features.

print(boston.target.shape)

# This will print the shape of the target variable, which is the number of samples.

print(boston.feature_names)

# This will print the names of the features.

print(boston.DESCR)

# This will print the full description of the dataset, including information about the features, target variable, and dataset statistics.