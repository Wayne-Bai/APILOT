from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

# Assuming X is the features and y is the target variable
X = ...
y = ...

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the Complement Naive Bayes classifier
complement_nb = MultinomialNB(class_prior=None)

# Fit the classifier to the training data
complement_nb.fit(X_train, y_train)

# Make predictions on the testing set
y_pred = complement_nb.predict(X_test)

# Print the classification report
print(classification_report(y_test, y_pred))
