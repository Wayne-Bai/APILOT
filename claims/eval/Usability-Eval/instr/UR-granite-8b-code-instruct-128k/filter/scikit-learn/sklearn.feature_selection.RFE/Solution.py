
from sklearn import datasets
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import make_classification

# Import the dataset
iris = datasets.load_iris()
X = iris.data
y = iris.target

# Create the model
model = LogisticRegression()

# Use recursive feature elimination to select the most important features
rfe = RFE(model, 3)
fit = rfe.fit(X, y)

# Print the ranking of the features
print("Feature ranking:", fit.ranking_)
print("Features selected:", fit.support_)
print("Feature names:", fit.feature_names_in_)
