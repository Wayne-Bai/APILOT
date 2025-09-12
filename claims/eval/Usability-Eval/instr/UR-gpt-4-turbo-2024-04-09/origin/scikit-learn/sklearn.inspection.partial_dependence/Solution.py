import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_boston
from sklearn.ensemble import RandomForestRegressor
from sklearn.inspection import plot_partial_dependence
from sklearn.model_selection import train_test_split

# Load the data
X, y = load_boston(return_X_y=True)
feature_names = load_boston()['feature_names']

# Create the training and testing datasets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Create the model: Random Forest Regressor
model = RandomForestRegressor(n_estimators=100, random_state=0)
model.fit(X_train, y_train)

# Specify the features you are interested in for the partial dependence plot
features = ['RM', 'LSTAT']  # RM: average number of rooms per dwelling, LSTAT: lower status of the population

fig, ax = plt.subplots(figsize=(12, 8))
display = plot_partial_dependence(model, X_train, features=features, feature_names=feature_names, ax=ax)
display.figure_.suptitle('Partial Dependence of house value on room number and status')
display.figure_.subplots_adjust(hspace=0.3)

plt.show()
