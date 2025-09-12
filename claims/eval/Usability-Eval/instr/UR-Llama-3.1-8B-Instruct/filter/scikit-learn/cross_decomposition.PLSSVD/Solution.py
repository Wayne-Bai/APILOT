# Import necessary libraries
from sklearn.decomposition import PCA
from sklearn.decomposition import FactorAnalysis
from sklearn.decomposition import TruncatedSVD
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

# Load iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# Split data into training and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Using PCA for dimensionality reduction
pca = PCA(n_components=2)  # Reduce data to 2 features
X_train_pca = pca.fit_transform(X_train)
X_test_pca = pca.transform(X_test)

# Using Factor Analysis for dimensionality reduction
fa = FactorAnalysis(n_components=2)  
X_train_fa = fa.fit_transform(X_train)
X_test_fa = fa.transform(X_test)

# Using Truncated SVD for dimensionality reduction
svd = TruncatedSVD(n_components=2)  
X_train_svd = svd.fit_transform(X_train)
X_test_svd = svd.transform(X_test)
