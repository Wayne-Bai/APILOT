import numpy as np
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression
# Assuming X is the features and y is the target variable

# Create the model
model = LogisticRegression()

# Initialize the recursive feature elimination with the model
rfe = RFE(model, 5)

# Fit the model to the data
fit = rfe.fit(X, y)

# Print the ranking of the features
print("Feature ranking:", fit.ranking_)
