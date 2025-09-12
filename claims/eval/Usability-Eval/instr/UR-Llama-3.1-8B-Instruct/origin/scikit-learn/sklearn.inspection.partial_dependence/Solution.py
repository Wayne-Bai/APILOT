# Import necessary libraries
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.datasets import load_boston
from sklearn.metrics import mean_squared_error
import numpy as np
import matplotlib.pyplot as plt
from sklearn.inspection import partial_dependence
from sklearn.inspection import partial_dependence_plot

# Load the Boston housing dataset
boston = load_boston()

# Split the dataset into features (X) and the target (y)
X = boston.data
y = boston.target

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a new instance of the model
model = RandomForestRegressor(n_estimators=100, random_state=42)

# Train the model on the training data
model.fit(X_train, y_train)

# Create partial dependence plots, excluding one variable
variables = [0, 2, 5] # you can replace these with your desired features, CO relevance CE socio info none abort ed ol crim disp Zimmer  age inde 

# Use partial dependence function along with each feature:
best_indexes = []
for index in variables:
    dep, axes = partial_dependence(model, X, feature_names=boston.feature_names, n_configurations=100)
    feature = boston.feature_names[index]
    best_indexes.append(index)
    print(feature)
    # Display the partial dependence plot
    partial_dependence_plot(index, model, X, feature_names=boston.feature_names)

# create subplots for each feature to see impact:
fig, ax = plt.subplots(1, len(variables), figsize=(20,4))
for i, index in enumerate(best_indexes):
    dep, axes = partial_dependence(model, X, feature_names=boston.feature_names, n_configurations=100)
    feature = boston.feature_names[index]
    
    ax[i].plot(dep[axes[index]])
    ax[i].set_title(feature)
    
plt.tight_layout()
plt.show()
