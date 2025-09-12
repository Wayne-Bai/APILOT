from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.inspection import plot_partial_dependence

# Load the Boston housing dataset
boston = load_boston()
X, y = boston.data, boston.target

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Calculate the partial dependence of a feature (e.g., 'RM')
plot_partial_dependence(model, X_train, features=[0], response_method='predict', n_jobs=1)
