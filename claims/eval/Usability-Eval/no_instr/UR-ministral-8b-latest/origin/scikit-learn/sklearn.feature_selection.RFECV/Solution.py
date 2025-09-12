import numpy as np
from sklearn.datasets import load_iris
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import StratifiedKFold

# Load example dataset
iris = load_iris()
X, y = iris.data, iris.target

# Define the estimator to use for feature selection
estimator = LogisticRegression(max_iter=200)

# Set up the RFE model
rfe = RFE(estimator, n_features_to_select=2, step=1)  # Select 2 features initially

# Set up the cross-validator
cv = StratifiedKFold(n_splits=5)  # 5-fold cross-validation

# Set up the scikit-learn pipeline
import sklearn.pipeline
pipeline = sklearn.pipeline.make_pipeline(rfe, estimator)

# Evaluate model
scores = cross_val_score(pipeline, X, y, cv=cv)

print("CV Accuracy Scores:", scores)
print("Average CV Accuracy:", np.mean(scores))
