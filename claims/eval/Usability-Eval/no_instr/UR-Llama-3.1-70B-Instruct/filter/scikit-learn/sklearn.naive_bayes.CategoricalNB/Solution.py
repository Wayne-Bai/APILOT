# Import necessary libraries
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.naive_bayes import CategoricalNB
from sklearn.preprocessing import OrdinalEncoder
import numpy as np
import pandas as pd

# Load the dataset
data = pd.DataFrame({
    'Feature1': np.random.choice(['A', 'B', 'C'], 100),
    'Feature2': np.random.choice(['Male', 'Female'], 100),
    'Feature3': np.random.choice(['Yes', 'No'], 100),
    'Label': np.random.choice(['Positive', 'Negative'], 100)
})

# Define features (X) and target (y)
X = data[['Feature1', 'Feature2', 'Feature3']]
y = data['Label']

# Encode categorical features using OrdinalEncoder
encoder = OrdinalEncoder()
X_encoded = encoder.fit_transform(X)

# Split dataset into training set and test set
X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.1, random_state=1)

# Create a Naive Bayes classifier
clf = CategoricalNB(alpha=0.1)

# Train the model
clf.fit(X_train, y_train)

# Predict the labels of the test set
y_pred = clf.predict(X_test)

# Evaluate the model
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
