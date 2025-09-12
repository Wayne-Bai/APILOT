# Importing the necessary libraries
from sklearn.cross_decomposition import PLSRegression
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Generating a random regression problem
X, y = make_regression(n_samples=100, n_features=5, n_targets=1, noise=0.5)

# Splitting the data into training and testing subsets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Instantiating the PLSRegression model
pls = PLSRegression(n_components=2)

# Fitting the model to the data
pls.fit(X_train, y_train)

# Making predictions
y_pred = pls.predict(X_test)

# Calculate mean squared error of the predictions
mse = mean_squared_error(y_test, y_pred)

# Printing the mean squared error
print('Mean Squared Error:', mse)
