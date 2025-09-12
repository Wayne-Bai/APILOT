from sklearn.cross_decomposition import PartialLeastSquares
from sklearn.linear_model import LinearRegression
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Load the Boston housing dataset
boston = load_boston()
X, y = boston.data, boston.target

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a Partial Least Squares transformer
pls = PartialLeastSquares()

# Fit the transformer to the training data
pls.fit(X_train, y_train)

# Transform the training and testing data
X_train_transformed = pls.transform(X_train)
X_test_transformed = pls.transform(X_test)

# Create a Linear Regression regressor
lr = LinearRegression()

# Fit the regressor to the transformed training data
lr.fit(X_train_transformed, y_train)

# Make predictions on the transformed testing data
y_pred = lr.predict(X_test_transformed)

# Calculate the mean squared error
mse = mean_squared_error(y_test, y_pred)

# Print the mean squared error
print("Mean Squared Error:", mse)
