# First, import the necessary libraries
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

# Assuming you have your features in X and labels in y
# Splitting the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Creating an instance of DecisionTreeClassifier
clf = DecisionTreeClassifier(random_state=42)

# Training the classifier with the training data
clf.fit(X_train, y_train)

# Now, you can use the trained classifier to make predictions
# For example, predicting labels for testing data
y_pred = clf.predict(X_test)
