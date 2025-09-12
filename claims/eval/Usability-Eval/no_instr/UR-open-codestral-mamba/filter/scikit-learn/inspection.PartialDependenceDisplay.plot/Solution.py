import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_diabetes
from sklearn.inspection import plot_partial_dependence
from sklearn.tree import DecisionTreeRegressor

# Load the diabetes dataset
diabetes = load_diabetes()

# Use a pre-defined dataset, the california housing dataset
X = diabetes.data
y = diabetes.target

# We'll train a decision tree regressor and plot the partial dependence plot of the first feature
regressor = DecisionTreeRegressor(random_state=0, max_depth=4)

# fit the model
regressor.fit(X, y)

# now plot the PDP for the first feature
plot_partial_dependence(regressor, X, [0])
plt.show()
