from sklearn.feature_selection import RFECV
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import StratifiedKFold

# Assuming X is your feature matrix and y is your target vector

# The estimator for which we are calculating RFECV
estimator = LogisticRegression(solver='liblinear')

# Stratified K-Fold cross validator
cv = StratifiedKFold(10)

# RFECV object
selector = RFECV(estimator, step=1, cv=cv, scoring='accuracy')

# Fit the RFE model on feature data
selector = selector.fit(X, y)

# Print selected features
print("Features selected: ", X.columns[selector.support_])
