import numpy as np
from sklearn.tree import DecisionTreeRegressor, ExtraTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Generate some example data
np.random.seed(42)
X = np.random.rand(100, 2)  # 100 samples, 2 features
y = np.dot(X, np.array([1.5, -2.0])) + np.random.randn(100) * 0.5  # y = 1.5*x1 - 2.0*x2 + noise

# Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Initialize an extremely randomized tree regressor
ext_tree_reg = ExtraTreeRegressor(n_estimators=100, random_state=42)

# Fit the model
ext_tree_reg.fit(X_train, y_train)

# Make predictions
y_pred = ext_tree_reg.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error: {mse}')

