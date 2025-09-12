
from sklearn.tree import DecisionTreeClassifier
from sklisten.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import pandas as pd

# Load dataset
df = pd.read_csv('...')

# Split dataset into training and test sets
X_train, X_test, y_train, y_test = train_test_split(df[['feature1', 'feature2']], df['target'], test_size=0.2, random_state=42)

# Create and train decision tree classifier
clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)

# Predict on test set
y_pred = clf.predict(X_test)

# Evaluate performance
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy:.3f}')
