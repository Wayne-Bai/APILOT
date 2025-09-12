import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Load your dataset into a Pandas dataframe
df = pd.read_csv("your_data.csv")

# Split the data into features and target variable
X = df.drop("target", axis=1)  # features
y = df["target"]  # target variable

# Create an instance of the LogisticRegression class with the default parameters
logreg = LogisticRegression()

# Train the model using the training data
logreg.fit(X, y)

# Make predictions on the test data
y_pred = logreg.predict(X_test)

# Evaluate the performance of the model using accuracy score, classification report, and confusion matrix
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
print(classification_report(y_test, y_pred))
print(confusion_matrix(y_test, y_pred))
