
import numpy as np
from sklearn.linear_model import PLSRegression
from sklearn.cross_decomposition import PLSTransformer
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Load Boston Housing dataset
X, y = load_boston(return_X_y=True)

# Split dataset into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize PLS transformer
pls = PLSTransformer()

# Fit PLS transformer to training data
pls.fit(X_train)

# Transform test data using PLS transformer
X_transformed = pls.transform(X_test)

# Initialize PLS regressor
pls_regressor = PLSRegression()

# Fit PLS regressor to transformed training data
pls_regressor.fit(X_transformed, y_train)

# Predict on test set using PLS regressor
predictions = pls_regressor.predict(X_transformed)

# Evaluate performance of PLS regressor
mse = mean_squared_error(y_test, predictions)
print("Mean squared error: {:.2f}".format(mse))
