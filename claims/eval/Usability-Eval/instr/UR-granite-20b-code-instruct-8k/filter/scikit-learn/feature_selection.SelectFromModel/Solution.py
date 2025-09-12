from sklearn.feature_selection import SelectFromModel
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.datasets import load_iris

# Load the iris dataset as an example
iris = load_iris()
X, y = iris.data, iris.target

# Build a logistic regression model
lr = LogisticRegression()

# Create a meta-transformer with SelectFromModel
sfm = SelectFromModel(lr)

# Create a pipeline with the meta-transformer and logistic regression model
pipeline = make_pipeline(sfm, lr)

# Fit the pipeline to the data
pipeline.fit(X, y)
