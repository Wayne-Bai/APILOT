import numpy as np
import pandas as pd
from sklearn.datasets import make_classification
from sklearn.model_selection import cross_val_score, StratifiedKFold
from sklearn.svm import SVC
from sklearn.feature_selection import RFE
from sklearn.pipeline import Pipeline

# Generate a synthetic dataset for demonstration
X, y = make_classification(n_samples=100, n_features=20, n_informative=5, n_redundant=2, random_state=42)

# Define the estimator and the RFE model
svc = SVC(kernel="linear")
rfe = RFE(estimator=svc, n_features_to_select=5, step=1) # Select 5 features

# Wrap in a pipeline for cross-validation
pipeline = Pipeline(steps=[('feature_selection', rfe), ('model', svc)])

# Define cross-validation method
cv = StratifiedKFold(n_splits=5)

# Perform cross-validation and print scores
scores = cross_val_score(pipeline, X, y, cv=cv, scoring='accuracy')

print("Cross-Validation Scores:", scores)
print("Mean Accuracy:", scores.mean())

# Fit the model on the entire dataset to get feature ranking
rfe.fit(X, y)
print("Feature Ranking:", rfe.ranking_)
print("Selected Features:", np.where(rfe.support_)[0])
