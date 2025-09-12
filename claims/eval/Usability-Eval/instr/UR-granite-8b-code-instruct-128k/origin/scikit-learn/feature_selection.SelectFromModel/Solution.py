from sklearn.feature_selection import SelectFromModel
from sklearn.linear_model import LinearRegression
import numpy as np

# Assume X is your feature matrix and y is your target vector
X = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
y = np.array([1, 2, 3, 4])

# Create a linear regression model
model = LinearRegression()
model.fit(X, y)

# Create a SelectFromModel instance with the model as the parameter
selector = SelectFromModel(model, threshold=0.1)

# Fit the selector to the data
selector.fit(X, y)

# Transform the data to select the features
X_selected = selector.transform(X)

# Print the selected features
print(X_selected)
