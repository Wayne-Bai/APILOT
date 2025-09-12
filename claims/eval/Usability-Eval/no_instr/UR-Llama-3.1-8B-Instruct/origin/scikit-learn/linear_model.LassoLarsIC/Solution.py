# Import necessary libraries
from sklearn.linear_model import LassoLars, LassoLarsIC
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
import numpy as np
import matplotlib.pyplot as plt

# Load diabetes dataset
diabetes = load_diabetes()
X = diabetes.data
y = diabetes.target

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define a function to plot coefficients
def plot_coefficients(model, title):
    plt.figure(figsize=(10,6))
    plt.bar(model.coef_.indices, model.coef_)
    plt.xlabel('Feature Index')
    plt.ylabel('Coefficient Value')
    plt.title(title)
    plt.show()

# Fit LassoLars model with BIC
model_bic = LassoLarsIC(criterion='bic')
model_bic.fit(X_train, y_train)
print("Model with BIC:", model_bic.score(X_test, y_test))
plot_coefficients(model_bic, 'Coefficients with BIC')

# Fit LassoLars model with AIC
model_aic = LassoLarsIC(criterion='aic')
model_aic.fit(X_train, y_train)
print("Model with AIC:", model_aic.score(X_test, y_test))
plot_coefficients(model_aic, 'Coefficients with AIC')
