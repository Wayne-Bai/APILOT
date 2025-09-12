from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import explained_variance_score

# Generate a sample regression dataset
X, y = make_regression(n_samples=100, n_features=2)

# Split the dataset into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Define the model
model = LinearRegression()

# Fit the model to the training data
model.fit(X_train, y_train)

# Make predictions on the test data
y_pred = model.predict(X_test)

# Calculate the Explained Variance Regression Score
evsr = explained_variance_score(y_test, y_pred)
print(f"Explained Variance Regression Score: {evsr}")
