
import sklearn.datasets
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression

# Load a dataset
X, y = sklearn.datasets.load_iris(return_X_y=True)

# Create a logistic regression model
model = LogisticRegression()

# Create the RFE object and rank features
rfe = RFE(model, n_features_to_select=3)
fit = rfe.fit(X, y)

# Print the ranking of features
print(fit.ranking_)
