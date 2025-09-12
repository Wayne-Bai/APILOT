# Import necessary libraries from scikit-learn
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import numpy as np

# Generate some sample data
np.random.seed(0)
X = np.random.rand(100, 1)
y = 3 + 2 * X + np.random.randn(100, 1)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize a linear regression model
model = LinearRegression()

# Train the model
model.fit(X_train, y_train)

# Get the predicted values
y_pred = model.predict(X_test)

# Calculate the explained variance regression score
mse = mean_squared_error(y_test, y_pred)
explained_variance = 1 - (mse / np.var(y_test))
explained_variance_regression_score = explained_variance
print('Explained Variance Regression Score:', explained_variance_regression_score)
