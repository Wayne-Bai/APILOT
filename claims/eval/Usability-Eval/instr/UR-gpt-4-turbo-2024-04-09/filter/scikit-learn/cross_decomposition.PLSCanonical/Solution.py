import numpy as np
from sklearn.cross_decomposition import PLSRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Sample data generation
np.random.seed(0)
n_samples = 100
n_features = 10

X = np.random.normal(size=(n_samples, n_features))
y = np.dot(X, np.random.normal(size=n_features)) + np.random.normal(size=n_samples)

# Scaling features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Splitting the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Partial Least Squares Regression
pls = PLSRegression(n_components=2)
pls.fit(X_train, y_train)

# Predicting the outputs
y_pred = pls.predict(X_test)

# Displaying the result
print("Predicted values:", y_pred.flatten())
