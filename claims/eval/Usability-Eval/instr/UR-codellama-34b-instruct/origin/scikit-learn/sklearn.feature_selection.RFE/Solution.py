
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression

# Load your dataset
X = ...  # feature matrix
y = ...  # target variable

# Initialize the RFE object
rfe = RFE(n_features_to_select=5, step=0.1)

# Fit the model with the entire dataset
model = LogisticRegression()
model.fit(X, y)

# Use the RFE object to rank features
ranked_features = rfe.ranking(X, y, model)

# Print the ranked features
print(ranked_features)
