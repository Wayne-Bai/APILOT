import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Load the iris dataset and split it into training and testing sets
iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris.data[:, :2], iris.target, test_size=0.3)

# Train a linear regression model on the training data
model = LinearRegression().fit(X_train, y_train)

# Compute the partial dependence of each feature on the response variable
pd_feature1 = model.predict(X_test[:, 0])
pd_feature2 = model.predict(X_test[:, 1])

# Plot the partial dependence plots
import matplotlib.pyplot as plt

plt.figure(figsize=(8, 6))
sns.kdeplot(pd_feature1, shade=True, label="Feature 1")
plt.xlabel("Partial Dependence of Feature 1 on Response Variable")
plt.ylabel("Density")
plt.title("Partial Dependence Plot for Feature 1")

plt.figure(figsize=(8, 6))
sns.kdeplot(pd_feature2, shade=True, label="Feature 2")
plt.xlabel("Partial Dependence of Feature 2 on Response Variable")
plt.ylabel("Density")
plt.title("Partial Dependence Plot for Feature 2")
