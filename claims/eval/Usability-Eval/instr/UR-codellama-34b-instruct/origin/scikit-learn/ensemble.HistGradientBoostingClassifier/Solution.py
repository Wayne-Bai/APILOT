from sklearn.experimental import enable_hist_gradient_boosting
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.model_selection import train_test_split
import pandas as pd

# Load your dataset
df = pd.read_csv('your_data.csv')

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(df.drop('target', axis=1), df['target'], test_size=0.2)

# Create a histogram-based gradient boosting classification tree
clf = HistGradientBoostingClassifier(random_state=42)

# Train the model on the training data
clf.fit(X_train, y_train)

# Use the model to make predictions on the testing data
y_pred = clf.predict(X_test)

# Evaluate the model using accuracy score
accuracy = clf.score(X_test, y_test)
print("Accuracy:", accuracy)
