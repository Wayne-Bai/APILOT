from sklearn.naive_bayes import ComplementNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix

# Assuming `X` as features and `y` as labels
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a Complement Naive Bayes classifier
nb_clf = ComplementNB()

# Train the classifier
nb_clf.fit(X_train, y_train)

# Predict the labels for the test set
y_pred = nb_clf.predict(X_test)

# Evaluate the classifier
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))
