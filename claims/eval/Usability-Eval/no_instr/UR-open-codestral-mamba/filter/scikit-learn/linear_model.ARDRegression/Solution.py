from sklearn.datasets import load_boston
from sklearn.linear_model import BayesianRidge
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Load the Boston dataset
boston = load_boston()

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(boston.data, boston.target, test_size=0.3, random_state=42)

# Create a BayesianRidge object
br = BayesianRidge()

# Fit the model
br.fit(X_train, y_train)

# Make predictions on the test set
y_pred = br.predict(X_test)

# Compute the mean squared error of the predictions
mse = mean_squared_error(y_test, y_pred)

print(f'Mean Squared Error: {mse}')
