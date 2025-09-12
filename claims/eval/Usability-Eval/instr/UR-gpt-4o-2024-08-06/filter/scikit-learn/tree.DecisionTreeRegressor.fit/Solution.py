from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
import numpy as np

# Generating a simple dataset for example purposes
np.random.seed(0)
X = np.random.rand(100, 1)  # feature matrix with 100 samples and 1 feature
y = X.ravel() * 2 + np.random.normal(0, 0.1, X.shape[0])  # target variable

# Splitting the dataset into a training set and a test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Building the decision tree regressor
regressor = DecisionTreeRegressor(random_state=0)

# Fitting the model on the training data
regressor = regressor.fit(X_train, y_train)

# Optionally, you can make predictions and evaluate the model here
y_pred = regressor.predict(X_test)

# Printing the predictions
print(y_pred)
