
import matplotlib.pyplot as plt
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Generate a synthetic dataset for demonstration purposes
X, y = make_regression(n_samples=100, n_features=5, noise=0.1)

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a linear regression object and fit the model to the training data
model = LinearRegression()
model.fit(X_train, y_train)

# Predict the response for the test data
y_pred = model.predict(X_test)

# Evaluate the performance of the model using R-squared score
r2 = r2_score(y_test, y_pred)
print("R-squared score:", r2)

# Plot the learning curve for the model
plt.plot(range(1, 100), model.coef_)
plt.xlabel("Training set size")
plt.ylabel("Coefficients")
plt.title("Learning Curve")
plt.show()
