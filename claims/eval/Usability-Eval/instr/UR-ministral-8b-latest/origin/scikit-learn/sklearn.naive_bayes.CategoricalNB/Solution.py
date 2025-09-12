import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import BernoulliNB  # For categorical features
from sklearn.metrics import accuracy_score

# Sample data: Assuming input is a DataFrame 'df' with categorical features and a target column 'target'
data = {
    'feature1': ['cat', 'dog', 'cat', 'dog'],
    'feature2': ['apple', 'banana', 'apple', 'banana'],
    'feature3': ['x', 'y', 'x', 'y'],
    'target': [0, 1, 0, 1]
}
df = pd.DataFrame(data)

# Split data into features (X) and target (y)
X = df.drop('target', axis=1)
y = df['target']

# Convert categorical features to binary matrices (one-hot encoding)
X = pd.get_dummies(X)

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Initialize Bernoulli Naive Bayes classifier
model = BernoulliNB()

# Train the model
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")
