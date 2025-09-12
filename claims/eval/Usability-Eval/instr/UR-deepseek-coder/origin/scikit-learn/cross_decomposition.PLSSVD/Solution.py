from sklearn.cross_decomposition import PLSRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import numpy as np

# Example dataset
X = np.random.rand(100, 20)
y = np.random.rand(100, 1)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize the features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Initialize and fit the PLSRegression model
pls = PLSRegression(n_components=2)
pls.fit(X_train, y_train)

# Predict on the test set
y_pred = pls.predict(X_test)

# Print the predicted values
print(y_pred)
