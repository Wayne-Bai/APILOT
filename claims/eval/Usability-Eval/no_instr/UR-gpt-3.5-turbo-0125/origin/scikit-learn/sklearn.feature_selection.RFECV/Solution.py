
from sklearn.feature_selection import RFECV
from sklearn.model_selection import KFold
from sklearn.linear_model import LogisticRegression

# Initialize the model
model = LogisticRegression()

# Initialize the cross-validation generator
kf = KFold(n_splits=5, shuffle=True)

# Initialize the RFECV
rfecv = RFECV(estimator=model, step=1, cv=kf)

# Fit RFECV
rfecv.fit(X, y)

# Print the selected features
print("Optimal number of features : %d" % rfecv.n_features_)
print("Selected features indices : %s" % rfecv.support_)
print("Selected features ranking : %s" % rfecv.ranking_)
