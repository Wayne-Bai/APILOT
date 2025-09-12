import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Load the iris dataset
iris = load_iris()
X = iris.data[:, :2]  # we only take the first two features.
y = iris.target

# Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Create a linear regression object and fit the data
reg = LinearRegression().fit(X_train, y_train)

# Generate predictions for the test set
y_pred = reg.predict(X_test)

# Plot the learning curve
plt.plot(range(10), y_pred, 'bo-', label='Predicted')
plt.plot(range(10), y_train, 'ro-', label='Training')
plt.legend()
plt.show()
