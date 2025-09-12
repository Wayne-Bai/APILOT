
import numpy as np
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression

# Load your dataset
X = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])  # Replace with your dataset features
y = np.array([0, 1, 0])  # Replace with your target variable

# Create the RFE object and rank features
model = LogisticRegression()
rfe = RFE(model, n_features_to_select=1)  # You can specify the number of features to select
rfe.fit(X, y)

# Print the ranking of features
print("Feature ranking:", rfe.ranking_)
