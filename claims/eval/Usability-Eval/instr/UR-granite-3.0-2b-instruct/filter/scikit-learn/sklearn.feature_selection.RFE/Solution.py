from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris

# Load dataset
iris = load_iris()
X, y = iris.data, iris.target

# Initialize the model
model = LogisticRegression()

# Initialize RFE
rfe = RFE(model, 3)  # Assuming you want to select top 3 features

# Fit RFE
rfe.fit(X, y)

# Print the ranking of features
print("Feature ranking:")
for feature_idx in range(X.shape[1]):
    if rfe.ranking_[feature_idx] > 0:
        print(f"{iris.feature_names[feature_idx]}: {rfe.ranking_[feature_idx]}")
