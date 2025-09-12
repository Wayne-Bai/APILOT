
from sklearn.feature_selection import RFECV
from sklearn.model_selection import StratifiedKFold
from sklearn.linear_model import LogisticRegression

# Assuming X_train and y_train are your training features and target
estimator = LogisticRegression()
cv = StratifiedKFold(n_splits=5)
rfecv = RFECV(estimator=estimator, step=1, cv=cv, scoring='accuracy')
rfecv.fit(X_train, y_train)

selected_features = X_train.columns[rfecv.support_]
print('Selected features:', selected_features)
