import numpy as np
from sklearn.datasets import make_classification
from sklearn.feature_selection import RFECV
from sklearn.model_selection import StratifiedKFold
from sklearn.ensemble import RandomForestClassifier

# Create a sample classification dataset
X, y = make_classification(n_samples=100, n_features=25, n_informative=3, n_redundant=2, random_state=42)

# Create the RFE object and compute a cross-validated score.
model = RandomForestClassifier()  # Using RandomForest as the base model
min_features_to_select = 1  # Minimum number of features to consider
rfecv = RFECV(estimator=model, step=1, cv=StratifiedKFold(5),
              scoring='accuracy', min_features_to_select=min_features_to_select)

# Fit RFECV
rfecv.fit(X, y)

# Print summary
print("Optimal number of features : %d" % rfecv.n_features_)
print("Mask of selected features:", rfecv.support_)

# Plot number of features VS. cross-validation scores
import matplotlib.pyplot as plt
plt.figure()
plt.xlabel("Number of features selected")
plt.ylabel("Cross validation score (nb of correct classifications)")
plt.plot(range(min_features_to_select, len(rfecv.grid_scores_) + min_features_to_select),
         rfecv.grid_scores_)
plt.show()
