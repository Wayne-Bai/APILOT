from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LassoLarsIC
from sklearn.metrics import mean_squared_error

# Load the Boston dataset
boston = datasets.load_boston()

# Split the dataset into features and target variable
X = boston.data
y = boston.target

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the LassoLarsIC model with BIC (Bayesian Information Criterion)
model = LassoLarsIC(criterion='bic')

# Fit the model to the training data
model.fit(X_train, y_train)

# Predict the target variable for the testing set
y_pred = model.predict(X_test)

# Calculate the mean squared error of the predictions
mse = mean_squared_error(y_test, y_pred)

# Print the mean squared error
print('Mean Squared Error:', mse)
