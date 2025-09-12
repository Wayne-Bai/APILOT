import numpy as np
import pandas as pd
from sklearn.feature_extraction import FeatureAgglomeration

# Sample data
X = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

# Applying Feature Agglomeration
agglo = FeatureAgglomeration(n_clusters=2)
X_transformed = agglo.fit_transform(X)

print(X_transformed)
