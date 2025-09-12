from sklearn.neighbors import LocalOutlierFactor
import numpy as np

# Assuming X is your set of samples
X = np.array([[1, 2], [2, 1], [3, 2], [4, 3], [5, 4], [6, 5], [7, 6], [8, 7], [9, 8], [10, 9]])

# Initialize the LocalOutlierFactor (LOF) model
lof = LocalOutlierFactor(n_neighbors=20, contamination='auto')

# Fit the model and predict the outlier factor for each sample
y_pred = lof.fit_predict(X)

# The outlier_factor attribute of the fit_predict method contains the outlier scores
outlier_scores = lof.outlier_factor_

# The soft boundary is where the outlier scores are close to 1
soft_boundary = np.where(outlier_scores > 0.9)

print("Soft boundary samples:", soft_boundary)
