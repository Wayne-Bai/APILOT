from sklearn.metrics import explained_variance_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.datasets import load_boston
import numpy as np

# Load the dataset
data = load_boston()
X = data.data
y = data.target

# Split the data into training and testing set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a linear regression model
regressor = LinearRegression()

# Train the model
regressor.fit(X_train, y_train)

# Make predictions using the testing set
y_pred = regressor.predict(X_test)

# Calculate the Explained Variance Score
score = explained_variance_score(y_test, y_pred)

print("Explained Variance Score:", score)
