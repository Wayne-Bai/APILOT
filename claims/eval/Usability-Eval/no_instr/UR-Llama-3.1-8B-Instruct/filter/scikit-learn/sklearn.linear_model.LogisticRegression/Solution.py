# Importing necessary libraries
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import pandas as pd
import numpy as np

# Assume this is your dataset
data = {
    'Exam1': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Exam2': [11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
    'Marks': [1, 2, 3, 4, 5, 4, 5, 2, 2, 3]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Convert DataFrame to numpy array
X = df[['Exam1', 'Exam2']].values
y = df['Marks'].values

# Scale the data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Initialize the Logistic Regression classifier
logreg = LogisticRegression(max_iter=10000)

# Train the model
logreg.fit(X_train, y_train)

# Predict the class labels
y_pred = logreg.predict(X_test)

# Evaluate the model
print('Accuracy:', accuracy_score(y_test, y_pred))
print('Classification Report:\n', classification_report(y_test, y_pred))
print('Confusion Matrix:\n', confusion_matrix(y_test, y_pred))
