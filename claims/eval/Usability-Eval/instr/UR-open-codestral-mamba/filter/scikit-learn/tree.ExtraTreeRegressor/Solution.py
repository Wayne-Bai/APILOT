# Import required libraries
from sklearn.datasets import make_regression
from sklearn.ensemble import ExtraTreesRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Generate a random regression problem
X, y = make_regression(n_samples=1000, n_features=30, noise=1.0)

# Split the dataset into a training set and a test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define the extreme randomized tree regressor model
er_model = ExtraTreesRegressor(n_estimators=100, random_state=42)

# Fit the model with the training data
er_model.fit(X_train, y_train)

# Make predictions with the test set
y_pred=er_model.predict(X_test)

# Evaluate the model performance
print('Mean Squared Error:', mean_squared_error(y_test, y_pred))
print('R2 Score:', r2_score(y_test, y_pred))
