
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

# Load dataset
df = pd.read_csv("diabetes.csv")

# Preprocess data
X = df.drop(columns=["Outcome"])
y = df["Outcome"]

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Build decision tree classifier
clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)

# Make predictions on testing set
predictions = clf.predict(X_test)

# Evaluate performance
accuracy = clf.score(X_test, y_test)
print(f"Accuracy: {accuracy}")
