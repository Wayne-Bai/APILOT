from sklearn.linear_model import RidgeCV
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split

# Generate a sample regression dataset
X, y = make_regression(n_samples=100, n_features=20, noise=0.1)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Fit a RidgeCV model
model = RidgeCV(alphas=[0.1, 1.0, 10.0], cv=5, store_cv_results=True)
model.fit(X_train, y_train)

# Print the best alpha found by RidgeCV
print("Best alpha:", model.alpha_)

# Evaluate the model on the test set
predictions = model.predict(X_test)
print("Mean Squared Error:", ((y_test - predictions) ** 2).mean())
