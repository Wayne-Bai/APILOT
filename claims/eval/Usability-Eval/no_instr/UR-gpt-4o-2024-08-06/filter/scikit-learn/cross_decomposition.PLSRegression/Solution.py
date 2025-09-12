# Import necessary libraries from scikit-learn
from sklearn.cross_decomposition import PLSRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np

# Example data
# X is the feature matrix and y is the target variable
X = np.random.rand(100, 10)  # 100 samples, 10 features
y = np.random.rand(100, 2)   # 100 samples, 2 target variables

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize PLSRegression model
n_components = 2  # Number of PLS components
pls = PLSRegression(n_components=n_components)

# Fit the model to the training data
pls.fit(X_train, y_train)

# Predict target variables using the test dataset
y_pred = pls.predict(X_test)

# Evaluate the model performance
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Output the results
print("Mean Squared Error:", mse)
print("R-squared:", r2)
