
from sklearn.feature_selection import RFECV
from sklearn.model_selection import KFold
from sklearn.linear_model import LogisticRegression
import numpy as np

# Load dataset
X, y = load_boston(return_X_y=True)

# Create a Recursive Feature Elimination object with cross-validation
rfe = RFECV(LogisticRegression(), step=1, cv=KFold(5))

# Fit the model and select features
rfe.fit(X, y)
selected_features = rfe.support_

# Print the selected features
print("Selected Features:", selected_features)
