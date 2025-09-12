# Importing necessary libraries
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import ExtraTreesRegressor
import numpy as np
from sklearn.metrics import mean_squared_error
from sklearn.inspection import permutation_importance
import matplotlib.pyplot as plt

# Generate a sample dataset
np.random.seed(0)
X = np.random.rand(100, 10)
y = 3 * X[:, 0] + 2 * X[:, 1] + np.random.rand(100)

# Split the dataset into a training set and a test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize features by removing the mean and scaling to unit variance
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Initialize an Extra Trees regressor
model = ExtraTreesRegressor(n_estimators=10, 
                            random_state=42, 
                            n_jobs=-1).fit(X_train_scaled, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test_scaled)

# Evaluate the model using the mean squared error
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")

# Get feature importances
importances = model.feature_importances_
feature_names = [f"Feature {i}" for i in range(X.shape[1])]

# Plot the feature importances
plt.bar(feature_names, importances)
plt.xlabel("Feature Index")
plt.ylabel("Importance")
plt.title("Feature Importances")
plt.show()

# Perform permutation importance
importances_permutation = permutation_importance(model, X_test_scaled, y_test, 
                                                 n_repeats=10, random_state=42).importances_mean

# Plot the permutation importances
plt.bar(feature_names, importances_permutation)
plt.xlabel("Feature Index")
plt.ylabel("Importance")
plt.title("Permutation Importances")
plt.show()
