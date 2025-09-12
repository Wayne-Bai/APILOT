# Importing the scikit-learn library and the GradientBoostingClassifier
from sklearn.ensemble import GradientBoostingClassifier

# Create a Gradient Boosting Classifier instance
clf = GradientBoostingClassifier(n_estimators=100, learning_rate=1.0, max_depth=1, random_state=0)

# Assume we have the training data in X_train and y_train
# Fit the classifier to the data
clf.fit(X_train, y_train)

# Assume we have the test data in X_test
# Use the trained classifier to predict the labels of X_test
y_pred = clf.predict(X_test)
