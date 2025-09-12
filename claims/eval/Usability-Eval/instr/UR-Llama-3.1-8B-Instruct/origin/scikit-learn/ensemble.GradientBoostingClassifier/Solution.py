# Importing the necessary libraries
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_wine
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import f1_score

# Loading the Wine dataset
wine = load_wine()

# Features and target
X = wine.data
y = wine.target

# Scaled the features using StandardScaler
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split the dataset into a training set and a test set
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Initialize a HistGradientBoostingClassifier
hgb = HistGradientBoostingClassifier(random_state=42)

# Training the model
hgb.fit(X_train, y_train)

# Predicting the test set results
y_pred = hgb.predict(X_test)

# Evaluate the model using accuracy score, classification report, confusion matrix, and f1 score
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy: ", accuracy)
print("Classification Report:")
print(classification_report(y_test, y_pred))
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))
f1 = f1_score(y_test, y_pred, average='macro')
print("F1 score: ", f1)
