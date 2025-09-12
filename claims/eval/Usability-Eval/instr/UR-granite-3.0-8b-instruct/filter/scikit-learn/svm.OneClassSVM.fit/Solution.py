from sklearn.neighbors import LocalOutlierFactor
import numpy as np

# Assuming X is your set of samples
X = np.array([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11]])

# Initialize the Local Outlier Factor (LOF) model
lof = LocalOutlierFactor(n_neighbors=20, contamination='auto')

# Fit the model to the data
lof.fit_predict(X)

# Get the outlier scores
outlier_scores = lof.negative_outlier_factor_

# Print the outlier scores
print(outlier_scores)
