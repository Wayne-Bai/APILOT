
from sklearn.naive_bayes import MultinomialNB
import pandas as pd

# Load dataset
data = pd.read_csv("your_dataset.csv")
X = data[["feature1", "feature2", ..., "featureN"]]
y = data["target"]

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the Naive Bayes classifier with the Multinomial distribution
clf = MultinomialNB()

# Train the model on the training data
clf.fit(X_train, y_train)

# Use the trained model to make predictions on the testing data
y_pred = clf.predict(X_test)

# Evaluate the performance of the model
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
