
# Importing the necessary library
from sklearn.tree import DecisionTreeClassifier

# Creating the decision tree classifier
clf = DecisionTreeClassifier()

# Training the classifier
clf.fit(X_train, y_train)

# Making predictions
predictions = clf.predict(X_test)
