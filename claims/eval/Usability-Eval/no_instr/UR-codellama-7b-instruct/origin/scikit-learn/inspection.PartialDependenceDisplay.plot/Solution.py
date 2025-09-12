import numpy as np
from sklearn import datasets
from sklearn.inspection import partial_dependence
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Load the boston housing dataset
boston = datasets.load_boston()

# Split the dataset into training and test sets
X_train, X_test, y_train, y_test = train_test_split(boston.data, boston.target, test_size=0.2)

# Create a linear regression model on the training data
model = LinearRegression().fit(X_train, y_train)

# Plot partial dependence plots for each feature of the dataset
for i in range(boston.data.shape[1]):
    partial_dependence(model, X_train[:, i], i)
