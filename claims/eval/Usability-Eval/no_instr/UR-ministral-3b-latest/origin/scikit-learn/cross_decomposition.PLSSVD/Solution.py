import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import TruncatedSVD

# Example dataset
data = np.array([[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9],
                 [10, 11, 12]])

# Fitting Partial Least Squares (SVD)
svd = TruncatedSVD(n_components=1)  # Setup SVD for 1 component

svd.fit(data)

# Transform original data
transformed_data = svd.transform(data)

print("Transformed Data:\n", transformed_data)
