
from sklearn.decomposition import PLSRegression
import numpy as np

# sample data
X = np.array([[1, 2], [3, 4], [5, 6]])
y = np.array([7, 8, 9])

# fit the PLS model
pls_model = PLSRegression(n_components=2)
pls_model.fit(X, y)

# use the transformed data to predict the target variable
predictions = pls_model.transform(X)
print(predictions)
