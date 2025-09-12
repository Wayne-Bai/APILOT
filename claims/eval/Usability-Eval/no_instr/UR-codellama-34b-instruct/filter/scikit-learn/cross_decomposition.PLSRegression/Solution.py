
import numpy as np
from sklearn.cross_decomposition import PLSRegression

# Generate some sample data
X = np.random.rand(100, 5)
y = np.random.rand(100)

# Perform the PLS regression
pls = PLSRegression(n_components=2)
pls.fit(X, y)

# Predict values for a new dataset
new_data = np.random.rand(50, 5)
predictions = pls.predict(new_data)
