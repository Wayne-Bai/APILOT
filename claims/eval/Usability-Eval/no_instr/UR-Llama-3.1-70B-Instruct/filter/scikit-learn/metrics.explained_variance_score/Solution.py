# Import necessary libraries
from sklearn.metrics import explained_variance_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import datasets
import numpy as np

# Load a dataset (e.g., diabetes dataset)
diabetes = datasets.load_diabetes()

# Split the dataset into features (X) and target (y)
X = diabetes.data
y = diabetes.target

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a Linear Regression model
model = LinearRegression()

# Train the model on the training data
model.fit(X_train, y_train)

# Predict on the testing data
y_pred = model.predict(X_test)

# Calculate the explained variance regression score
evs = explained_variance_score(y_test, y_pred)

print("Explained Variance Regression Score: ", evs)

# Optional: Calculate the explained variance regression score with multioutput
y_test_2d = y_test.reshape(-1, 1)
y_pred_2d = y_pred.reshape(-1, 1)
evs_multioutput = explained_variance_score(y_test_2d, y_pred_2d, multioutput='raw_values')
print("Explained Variance Regression Score with multioutput: ", evs_multioutput)
