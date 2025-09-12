
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import pandas as pd

# Load the data
df = pd.read_csv("data.csv")

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(df.drop("target", axis=1), df["target"], test_size=0.2)

# Create a decision tree classifier with the default parameters
clf = DecisionTreeClassifier()

# Train the model on the training data
clf.fit(X_train, y_train)

# Use the trained model to make predictions on the testing data
y_pred = clf.predict(X_test)

# Print the accuracy score
print("Accuracy:", clf.score(X_test, y_test))
