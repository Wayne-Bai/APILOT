import numpy as np
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_selection import SelectFromModel
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load the dataset
data = load_iris()
X, y = data.data, data.target

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Create a RandomForest Classifier
clf = RandomForestClassifier(n_estimators=100, random_state=42)

# Create a SelectFromModel object that will use the random forest classifier to select features
# based on their importance weights
selector = SelectFromModel(estimator=clf)

# Create a pipeline that includes feature selection and classification
pipeline = Pipeline([
    ('feature_selection', selector),
    ('classification', clf)
])

# Train the model
pipeline.fit(X_train, y_train)

# Evaluate the model
predictions = pipeline.predict(X_test)
accuracy = accuracy_score(y_test, predictions)

print(f"Model accuracy: {accuracy:.2f}")
print("Selected features:", selector.get_support(indices=True))
