from sklearn.cross_decomposition import PLSRegression
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Load the Boston housing dataset
boston = load_boston()
X = boston.data
y = boston.target

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the PLSRegression transformer and regressor
pls = PLSRegression(n_components=2)

# Fit the transformer and regressor to the training data
pls.fit(X_train, y_train)

# Transform the training and test data using the transformer
X_train_pls = pls.transform(X_train)
X_test_pls = pls.transform(X_test)

# Predict the target values for the test data using the regressor
y_pred = pls.predict(X_test_pls)

# Calculate the mean squared error of the predictions
mse = mean_squared_error(y_test, y_pred)

print("Mean Squared Error:", mse)
