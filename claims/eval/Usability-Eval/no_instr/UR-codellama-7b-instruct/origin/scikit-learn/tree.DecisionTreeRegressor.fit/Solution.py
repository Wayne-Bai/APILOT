
from sklearn.tree import DecisionTreeRegressor

# Load your data
X = ... # feature matrix
y = ... # target vector

# Build a decision tree regressor from the training set (X, y)
regressor = DecisionTreeRegressor(random_state=42)
regressor.fit(X, y)
