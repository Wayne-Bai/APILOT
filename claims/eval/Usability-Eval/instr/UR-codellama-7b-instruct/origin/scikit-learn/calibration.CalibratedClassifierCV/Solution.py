import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# Load the dataset
df = pd.read_csv("your_data.csv")

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(df[["feature1", "feature2", "feature3"]], df["target"], test_size=0.2, random_state=42)

# Train a logistic regression model on the training data
lr = LogisticRegression()
lr.fit(X_train, y_train)

# Predict the probabilities of the positive class for the testing data
y_pred_proba = lr.predict_proba(X_test)[:, 1]

# Evaluate the performance of the logistic regression model
print("Accuracy: ", accuracy_score(y_test, y_pred_proba))
print("Classification Report: \n", classification_report(y_test, y_pred_proba))
