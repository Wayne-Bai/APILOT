
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklintor import RFECV
import numpy as np

# Load data
X = ... # features
y = ... # target variable

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Create a linear regression model with RFECV
rfecv = RFECV(LinearRegression(), step=1, cv=5)
rfecv.fit(X_train, y_train)

# Get the ranking of features
ranking = rfecv.ranking_

# Print the ranking of features
print(ranking)
