from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import numpy as np

# Load your dataset
X = ...  # feature data
y = ...  # target variable

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Scale the data using StandardScaler
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train a histogram-based gradient boosting classification tree on the scaled data
clf = HistGradientBoostingClassifier()
clf.fit(X_train_scaled, y_train)

# Use the trained model to make predictions on the test set
y_pred = clf.predict(X_test_scaled)
