
# Import necessary libraries from scikit-learn
from sklearn.datasets import make_friedman1
from sklearn.feature_selection import RFE, mutual_info_regression
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import numpy as np

# Generate a random dataset
X, y = make_friedman1(n_samples=50, n_features=10, random_state=0)

# Create a linear regression estimator
estimator = LinearRegression()

# Create a recursive feature elimination object with 5 features to select
selector = RFE(estimator, 5, step=1)

# Train the recursive feature elimination object
selector = selector.fit(X, y)

# Get the support and ranking from the selector
support = selector.support_
ranking = selector.ranking_

print("Support: ", support)
print("Feature Ranking: ", ranking)

# Mutual Information
mi = mutual_info_regression(X, y)
print('Mutual Information: ', mi)

# Recursive Feature Elimination with Cross Validation
from sklearn.model_selection import cross_val_score
scores = cross_val_score(selector, X, y, cv=5)
print('Cross Validation scores: ', scores)

# RMSE on Train Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
X_train_selected = selector.fit_transform(X_train, y_train)
X_test_selected = selector.transform(X_test)
estimator.fit(X_train_selected, y_train)
y_pred = estimator.predict(X_test_selected)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
print('RMSE: ', rmse)
