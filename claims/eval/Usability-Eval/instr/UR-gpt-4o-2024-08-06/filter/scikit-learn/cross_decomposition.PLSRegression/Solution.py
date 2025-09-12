# Import necessary libraries from scikit-learn
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.cross_decomposition import PLSRegression
from sklearn.metrics import mean_squared_error, r2_score

# Generate synthetic data for demonstration
np.random.seed(0)
X = np.random.normal(size=(100, 10))  # 100 samples, 10 features
Y = np.random.normal(size=(100, 3))   # 100 samples, 3 target variables

# Split the data into training and testing sets
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=1)

# Initialize the PLSRegression model
n_components = 2  # Number of components to keep
pls = PLSRegression(n_components=n_components)

# Fit the model to the training data
pls.fit(X_train, Y_train)

# Predict the targets for the test set
Y_pred = pls.predict(X_test)

# Evaluate the model’s performance
mse = mean_squared_error(Y_test, Y_pred)
r2 = r2_score(Y_test, Y_pred)

# Output the evaluation metrics
print(f'Mean Squared Error: {mse:.2f}')
print(f'R^2 Score: {r2:.2f}')
