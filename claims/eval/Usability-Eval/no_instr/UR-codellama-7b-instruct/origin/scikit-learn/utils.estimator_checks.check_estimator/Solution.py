
import sklearn

# Load the example dataset
iris = load_iris()
X = iris.data[:, :2]  # we only take the first two features.
y = iris.target

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Fit a classification model to the training data
model = LogisticRegression()
model.fit(X_train, y_train)

# Evaluate the trained model on the testing set
y_pred = model.predict(X_test)
print("Accuracy: ", accuracy_score(y_test, y_pred))
