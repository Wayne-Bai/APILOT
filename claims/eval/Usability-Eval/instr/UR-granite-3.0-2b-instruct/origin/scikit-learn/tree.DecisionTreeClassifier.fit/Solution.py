from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

# Assuming X is your features and y is your target variable
X = ...
y = ...

# Split the data into training set and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a decision tree classifier
clf = DecisionTreeClassifier()

# Train the classifier using the training set
clf.fit(X_train, y_train)
