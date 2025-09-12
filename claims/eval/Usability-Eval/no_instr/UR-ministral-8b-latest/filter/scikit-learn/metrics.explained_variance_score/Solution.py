import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import explained_variance_score

# Generate some example data
np.random.seed(42)
X = np.random.rand(100, 2)  # 100 data points with 2 features
y = np.random.rand(100)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a linear regression model
model = LinearRegression()

# Fit the model on the training data
model.fit(X_train, y_train)

# Make predictions on the test data
y_pred = model.predict(X_test)

# Calculate the explained variance score
evs = explained_variance_score(y_test, y_pred)

print(f"Explained Variance Score: {evs:.4f}")
