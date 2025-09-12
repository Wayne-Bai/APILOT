
import numpy as np
from sklearn.cross_decomposition import CCA
from sklearn.datasets import make_classification

# Generate sample dataset
n_samples = 1000
n_features = 5
X, y = make_classification(n_samples=n_samples, n_classes=2, n_informative=n_features)

# Split dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

# Perform canonical correlation analysis
cca = CCA(n_components=2, transform='full', reg=None)
x_cca = cca.fit(X_train, X_test).transform(X_train, X_test)
