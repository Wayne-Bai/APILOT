
# Importing required libraries
import numpy as np
from sklearn.neighbors import LocalOutlierFactor

# Generating sample data
X = np.random.randn(100, 2)

# Fitting the Local Outlier Factor model
lof = LocalOutlierFactor()
y_pred = lof.fit_predict(X)

# Identifying the soft boundary
X_scores = lof.negative_outlier_factor_
soft_boundary = np.percentile(X_scores, 10)  # Adjust the percentile as needed

# Printing the soft boundary
print("Soft Boundary Score:", soft_boundary)
