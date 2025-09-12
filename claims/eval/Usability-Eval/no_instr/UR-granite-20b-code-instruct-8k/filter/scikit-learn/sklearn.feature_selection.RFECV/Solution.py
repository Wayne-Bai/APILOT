from sklearn.feature_selection import RFECV
from sklearn.datasets import make_classification
from sklearn.svm import SVC
# create a dataset
X, y = make_classification(n_samples=1000, n_features=20, n_informative=2, n_redundant=10, random_state=0, shuffle=False)
# create a base model
model = SVC(kernel='linear', C=1)
# instantiate the RFECV model
rfe = RFECV(estimator=model, step=1, cv=5)
# fit the model
rfe.fit(X, y)
# print the selected features
print(rfe.support_)
print(rfe.ranking_)
