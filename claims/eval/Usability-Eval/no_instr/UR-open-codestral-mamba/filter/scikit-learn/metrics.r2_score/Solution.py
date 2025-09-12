from sklearn.metrics import r2_score
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split

# Generate a random regression problem
X, y = make_regression(n_samples=100, n_features=2, noise=0.5)

# Split the data into training/testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# A simple linear model
from sklearn.linear_model import LinearRegression
model = LinearRegression()

# Train the model using the training sets
model.fit(X_train, y_train)

# Make predictions using the testing set
y_pred = model.predict(X_test)

# The coefficient of determination: 1 is perfect prediction
print('Coefficient of determination R^2: %.2f' % r2_score(y_test, y_pred))
