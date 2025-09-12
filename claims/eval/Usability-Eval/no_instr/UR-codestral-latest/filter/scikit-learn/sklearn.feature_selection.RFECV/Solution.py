from sklearn.feature_selection import RFECV
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import StratifiedKFold
import numpy as np

# Assuming that X is your feature matrix and y is your target vector
# Let's use a RandomForestClassifier as the base estimator
estimator = RandomForestClassifier()

# Here, we're using StratifiedKFold cross-validator to split the data into 5 folds
# with shuffling and random_state for reproducibility
cv = StratifiedKFold(5, shuffle=True, random_state=42)

# Applying Recursive Feature Elimination with cross-validation
selector = RFECV(estimator, step=1, cv=cv, scoring='accuracy')
selector = selector.fit(X, y)

# Outputting the ranking of features
ranking = selector.ranking_
print("Features sorted by their rank:")
print(sorted(zip(map(lambda x: round(x, 4), selector.grid_scores_), X.columns), reverse=True))
